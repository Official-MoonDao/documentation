#!/usr/bin/env python3
"""Build the static site that GitHub Pages serves at docs.moondao.com.

The standalone documentation site is deprecated. In-app docs live in
Official-MoonDao/MoonDAO at ui/content/docs and are served at
https://moondao.com/docs. GitHub Pages cannot emit an HTTP 301, so each
published URL is a static HTML stub (meta refresh + location.replace) and
unknown URLs fall through to 404.html, which preserves the path in JS.

Quartz slug rules, matched to the app's ui/lib/docs/slug.ts:
spaces become hyphens (a double space becomes --); @ ' ( ) . _ stay.
Two Quartz slugs are not reproduced as routes on the app and are remapped.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

DOCS_ROOT = "https://moondao.com/docs"
CNAME = "docs.moondao.com"
VAULT = Path("MoonDAO/docs")

# Quartz URLs the app deliberately does not reproduce. See
# INTENTIONAL_SLUG_CHANGES in Official-MoonDao/MoonDAO ui/lib/docs/slug.ts.
ALIASES = {
    "Reference/Glossary-(dynamic)": "Reference/Glossary-dynamic",
    "Reference/Nested-Docs/MoonDAO\u2019s-Quarterly-Rewards": (
        "Reference/Nested-Docs/MoonDAOs-Quarterly-Rewards"
    ),
    "Reference/Nested-Docs/MoonDAO's-Quarterly-Rewards": (
        "Reference/Nested-Docs/MoonDAOs-Quarterly-Rewards"
    ),
}


def slugify_segment(segment: str) -> str:
    return segment.replace(" ", "-")


def slugify_md_path(rel_md: str) -> str:
    rel = rel_md.replace("\\", "/")
    if rel.lower().endswith(".md"):
        rel = rel[:-3]
    parts = [slugify_segment(part) for part in rel.split("/") if part and part not in (".", "..")]
    return "/".join(parts)


def destination_for_slug(slug: str) -> str:
    """Absolute docs URL for a Quartz slug. Empty slug and `index` are the root."""
    if slug in ("", "index"):
        return DOCS_ROOT
    mapped = ALIASES.get(slug, slug)
    return f"{DOCS_ROOT}/{mapped}"


def frontmatter_slug(text: str) -> str | None:
    """Return a frontmatter `slug:` value without leading/trailing slashes.

    `slug: /` is the docs root and returns an empty string. Missing slug returns None.
    """
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    for line in text[3:end].splitlines():
        if not line.startswith("slug:"):
            continue
        raw = line.split(":", 1)[1].strip().strip("'\"")
        return raw.strip("/")
    return None


def html_escape(value: str) -> str:
    return value.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def page_html(target: str) -> str:
    """Static stub. JS keeps query and hash; meta refresh covers no-JS clients."""
    escaped = html_escape(target)
    js = json.dumps(target)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>MoonDAO docs have moved</title>
  <link rel="canonical" href="{escaped}">
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="0; url={escaped}">
  <script>
    (function () {{
      var dest = {js};
      window.location.replace(dest + (window.location.search || "") + (window.location.hash || ""));
    }})();
  </script>
</head>
<body>
  <p>MoonDAO documentation has moved. Continue to <a href="{escaped}">{escaped}</a>.</p>
</body>
</html>
"""


def not_found_html() -> str:
    aliases = json.dumps(ALIASES, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>MoonDAO docs have moved</title>
  <link rel="canonical" href="{DOCS_ROOT}">
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="0; url={DOCS_ROOT}">
  <script>
    var DOCS_REDIRECT_ALIASES = {aliases};
    function docsRedirectUrl(pathname) {{
      var path = pathname || "/";
      try {{
        path = decodeURIComponent(path);
      }} catch (e) {{}}
      path = String(path).replace(/\\\\/g, "/");
      path = path.replace(/\\/index\\.html$/i, "");
      path = path.replace(/\\.html$/i, "");
      path = path.replace(/\\/+$/g, "");
      path = path.replace(/^\\/+/g, "");
      var parts = path.split("/");
      if (parts.some(function (part) {{ return part === "" || part === "." || part === ".."; }})) {{
        return "{DOCS_ROOT}";
      }}
      if (path.indexOf(":") !== -1 || path.indexOf("//") !== -1) {{
        return "{DOCS_ROOT}";
      }}
      if (DOCS_REDIRECT_ALIASES[path]) path = DOCS_REDIRECT_ALIASES[path];
      if (!path) return "{DOCS_ROOT}";
      return "{DOCS_ROOT}/" + path.split("/").map(function (segment) {{
        return encodeURIComponent(segment).replace(/%40/g, "@").replace(/%28/g, "(").replace(/%29/g, ")").replace(/%7E/gi, "~");
      }}).join("/");
    }}
    window.location.replace(docsRedirectUrl(window.location.pathname) + (window.location.search || "") + (window.location.hash || ""));
  </script>
</head>
<body>
  <p>MoonDAO documentation has moved. Continue to <a href="{DOCS_ROOT}">{DOCS_ROOT}</a>.</p>
</body>
</html>
"""


def collect_slugs(vault: Path) -> dict[str, str]:
    """Map output slug (no .html) to destination URL."""
    pages: dict[str, str] = {"": DOCS_ROOT}
    folders: set[str] = set()

    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault).as_posix()
        if any(part.startswith(".") or part.startswith("_") for part in Path(rel).parts):
            continue
        slug = slugify_md_path(rel)
        if slug == "index":
            pages[""] = DOCS_ROOT
        else:
            pages[slug] = destination_for_slug(slug)
            parent = str(Path(slug).parent).replace("\\", "/")
            while parent not in ("", "."):
                folders.add(parent)
                next_parent = str(Path(parent).parent).replace("\\", "/")
                if next_parent == parent:
                    break
                parent = next_parent

        alias = frontmatter_slug(path.read_text(encoding="utf-8"))
        if alias:
            pages.setdefault(alias, destination_for_slug(alias))

    for folder in folders:
        pages.setdefault(folder, destination_for_slug(folder))
    return pages


def write_site(vault: Path, out: Path) -> dict[str, str]:
    if out.resolve() == Path.cwd().resolve():
        raise SystemExit("refusing to use the repository root as --out")
    pages = collect_slugs(vault)
    if out.exists():
        for child in sorted(out.rglob("*"), reverse=True):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                child.rmdir()
    out.mkdir(parents=True, exist_ok=True)

    for slug, target in pages.items():
        # <slug>.html is what GitHub Pages serves at /<slug> and /<slug>.html.
        dest = out / "index.html" if slug == "" else out / f"{slug}.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page_html(target), encoding="utf-8")

    # Folder URLs such as /Network/ are served from <folder>/index.html.
    # Keep the sibling <folder>.html file too, so /Network and /Network.html
    # redirect even if Pages does not fall through to the directory index.
    for slug, target in pages.items():
        if not slug:
            continue
        child_prefix = slug + "/"
        if any(other.startswith(child_prefix) for other in pages):
            index = out / slug / "index.html"
            index.parent.mkdir(parents=True, exist_ok=True)
            index.write_text(page_html(target), encoding="utf-8")

    (out / "404.html").write_text(not_found_html(), encoding="utf-8")
    (out / "CNAME").write_text(CNAME + "\n", encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    return pages


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=VAULT)
    parser.add_argument("--out", type=Path, default=Path("site"))
    args = parser.parse_args()
    pages = write_site(args.vault, args.out)
    print(f"wrote {len(pages)} redirect pages to {args.out}")


if __name__ == "__main__":
    main()
