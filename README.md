# MoonDAO documentation (deprecated)

This repository used to publish [docs.moondao.com](https://docs.moondao.com) with [Quartz](https://quartz.jzhao.xyz). That site is retired.

Canonical docs now live in [Official-MoonDao/MoonDAO](https://github.com/Official-MoonDao/MoonDAO) under `ui/content/docs` and are served at [https://moondao.com/docs](https://moondao.com/docs).

## What this repo publishes

GitHub Pages still hosts `docs.moondao.com` (DNS `CNAME` → `official-moondao.github.io`). The `build-and-deploy` workflow no longer builds Quartz. It publishes a static redirect site:

- Known pages, including `/` and `/Network/How-to-Become-a-Citizen`, are HTML stubs. Each stub meta-refreshes and runs `location.replace` to the same path on `https://moondao.com/docs/...`.
- Folder URLs such as `/Network/` redirect to `https://moondao.com/docs/Network`.
- Any other path hits `404.html`, which keeps the path, query string, and hash, and sends the browser to `https://moondao.com/docs/<path>`.
- Two old Quartz slugs that the app does not reproduce are remapped: `Reference/Glossary-(dynamic)` → `Reference/Glossary-dynamic`, and `Reference/Nested-Docs/MoonDAO’s-Quarterly-Rewards` → `Reference/Nested-Docs/MoonDAOs-Quarterly-Rewards`.

GitHub Pages cannot send an HTTP 301. The redirect is immediate HTML (`meta http-equiv="refresh"` plus JavaScript). A `CNAME` file is included in the Pages artifact so the custom domain stays `docs.moondao.com`.

Markdown under `MoonDAO/docs` is only an archive used to generate those redirect stubs. Edits here do not update moondao.com. Change the in-app docs in Official-MoonDao/MoonDAO instead.

## DNS

No registrar change is required. Leave this record in place:

```
docs.moondao.com.  CNAME  official-moondao.github.io.
```

Nameservers are Google Domains (`ns-cloud-b1` through `ns-cloud-b4.googledomains.com`). GitHub Pages already has the custom domain `docs.moondao.com` with HTTPS enforced. Do not point the hostname somewhere else unless you also configure an HTTP redirect there; removing the `CNAME` to `official-moondao.github.io` would take this redirect offline.
