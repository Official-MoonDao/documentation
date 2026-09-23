#!/usr/bin/env python3
"""Check the generated docs.moondao.com redirect site."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_redirect_site import (  # noqa: E402
    DOCS_ROOT,
    destination_for_slug,
    slugify_md_path,
    write_site,
)


def assert_true(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit(message)


def read(path: Path) -> str:
    assert_true(path.is_file(), f"missing {path}")
    return path.read_text(encoding="utf-8")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refresh: str | None = None
        self.canonical: str | None = None
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta" and (values.get("http-equiv") or "").lower() == "refresh":
            self.refresh = values.get("content")
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")
        if tag == "a":
            href = values.get("href")
            if href:
                self.hrefs.append(href)


def assert_targets(html: str, target: str, label: str) -> None:
    parsed = PageParser()
    parsed.feed(html)
    assert_true(parsed.refresh == f"0; url={target}", f"{label} meta refresh is {parsed.refresh!r}")
    assert_true(parsed.canonical == target, f"{label} canonical is {parsed.canonical!r}")
    assert_true(target in parsed.hrefs, f"{label} link is {parsed.hrefs!r}")
    assert_true(f"var dest = {json.dumps(target)};" in html, f"{label} script dest is not {target}")
    assert_true("location.search" in html and "location.hash" in html, f"{label} drops query or hash")


def check_tree(out: Path) -> None:
    assert_targets(read(out / "index.html"), DOCS_ROOT, "root")
    assert_true(
        f"{DOCS_ROOT}/index" not in read(out / "index.html"),
        "root must not redirect to /docs/index",
    )

    citizen = "Network/How-to-Become-a-Citizen"
    team = "Network/How-to-Create-Your-Team"
    faq = "Network/NetworkFAQ"
    for slug in (citizen, team, faq, "Governance/Constitution", "Projects/Project-System"):
        assert_targets(read(out / f"{slug}.html"), f"{DOCS_ROOT}/{slug}", slug)

    assert_targets(read(out / "Network" / "index.html"), f"{DOCS_ROOT}/Network", "Network folder")
    assert_targets(read(out / "About" / "index.html"), f"{DOCS_ROOT}/About", "About folder")

    glossary = read(out / "Reference" / "Glossary-(dynamic).html")
    assert_targets(glossary, f"{DOCS_ROOT}/Reference/Glossary-dynamic", "glossary alias")

    rewards = read(out / "Reference" / "Nested-Docs" / "MoonDAO\u2019s-Quarterly-Rewards.html")
    assert_targets(
        rewards,
        f"{DOCS_ROOT}/Reference/Nested-Docs/MoonDAOs-Quarterly-Rewards",
        "apostrophe alias",
    )

    sweep = "Legal/Ticket-to-Zero-G-NFT/Ticket-to-Zero-G-NFT--Sweepstakes-Rules"
    assert_targets(read(out / f"{sweep}.html"), f"{DOCS_ROOT}/{sweep}", "double-space slug")

    deprize = "Legal/DePrize-Terms-and-Conditions"
    assert_targets(read(out / f"{deprize}.html"), f"{DOCS_ROOT}/{deprize}", "deprize")

    assert_targets(
        read(out / "privacy-policy.html"),
        f"{DOCS_ROOT}/privacy-policy",
        "frontmatter slug",
    )
    assert_targets(
        read(out / "website-terms-and-conditions.html"),
        f"{DOCS_ROOT}/website-terms-and-conditions",
        "terms slug",
    )

    bio = read(out / "Reference" / "Bios" / "@ryand2d.html")
    assert_targets(bio, f"{DOCS_ROOT}/Reference/Bios/@ryand2d", "at-sign slug")

    cname = (out / "CNAME").read_text(encoding="utf-8").strip()
    assert_true(cname == "docs.moondao.com", f"unexpected CNAME {cname!r}")
    assert_true((out / "404.html").is_file(), "missing 404.html")
    assert_true((out / ".nojekyll").is_file(), "missing .nojekyll")

    not_found = read(out / "404.html")
    assert_true("function docsRedirectUrl" in not_found, "404.html missing docsRedirectUrl")
    assert_true("Glossary-dynamic" in not_found, "404.html missing glossary remap")
    assert_true("MoonDAOs-Quarterly-Rewards" in not_found, "404.html missing rewards remap")
    parsed = PageParser()
    parsed.feed(not_found)
    assert_true(parsed.refresh == f"0; url={DOCS_ROOT}", f"404 meta refresh is {parsed.refresh!r}")


def check_js(out: Path) -> None:
    script = read(out / "404.html")
    start = script.index("var DOCS_REDIRECT_ALIASES")
    end = script.index("window.location.replace")
    snippet = script[start:end]
    cases = {
        "/": DOCS_ROOT,
        "/Network/How-to-Become-a-Citizen": f"{DOCS_ROOT}/Network/How-to-Become-a-Citizen",
        "/Network/How-to-Become-a-Citizen/": f"{DOCS_ROOT}/Network/How-to-Become-a-Citizen",
        "/Network/How-to-Become-a-Citizen.html": f"{DOCS_ROOT}/Network/How-to-Become-a-Citizen",
        "/Reference/Glossary-(dynamic)": f"{DOCS_ROOT}/Reference/Glossary-dynamic",
        "/Reference/Nested-Docs/MoonDAO%E2%80%99s-Quarterly-Rewards": (
            f"{DOCS_ROOT}/Reference/Nested-Docs/MoonDAOs-Quarterly-Rewards"
        ),
        "/Reference/Bios/@ryand2d": f"{DOCS_ROOT}/Reference/Bios/@ryand2d",
        "/privacy-policy": f"{DOCS_ROOT}/privacy-policy",
        "/this/was/never/a/page": f"{DOCS_ROOT}/this/was/never/a/page",
        "/../../etc/passwd": DOCS_ROOT,
        "/https://evil.example": DOCS_ROOT,
    }
    payload = json.dumps({"snippet": snippet, "cases": cases})
    node = r"""
const fs = require("fs");
const input = JSON.parse(fs.readFileSync(0, "utf8"));
eval(input.snippet);
for (const [path, expected] of Object.entries(input.cases)) {
  const actual = docsRedirectUrl(path);
  if (actual !== expected) {
    console.error(path + " -> " + actual + " expected " + expected);
    process.exit(1);
  }
}
"""
    result = subprocess.run(
        ["node", "-e", node],
        input=payload,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr or result.stdout or "node redirect check failed")


def check_slug_helpers() -> None:
    assert_true(
        slugify_md_path("Network/How to Become a Citizen.md") == "Network/How-to-Become-a-Citizen",
        "citizen slug mismatch",
    )
    assert_true(
        slugify_md_path("Legal/Ticket to Zero-G NFT/Ticket to Zero-G NFT  Sweepstakes Rules.md")
        == "Legal/Ticket-to-Zero-G-NFT/Ticket-to-Zero-G-NFT--Sweepstakes-Rules",
        "double space slug mismatch",
    )
    assert_true(destination_for_slug("index") == DOCS_ROOT, "index destination")
    assert_true(destination_for_slug("") == DOCS_ROOT, "empty destination")


def main() -> None:
    check_slug_helpers()
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if out is None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "site"
            write_site(ROOT / "MoonDAO" / "docs", out)
            check_tree(out)
            check_js(out)
    else:
        check_tree(out)
        check_js(out)
    print("redirect site ok")


if __name__ == "__main__":
    main()
