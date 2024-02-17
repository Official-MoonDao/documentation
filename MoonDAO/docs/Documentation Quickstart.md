---
tags:
  - docs/onboarding
---
MoonDAO's documentation, planning, project notes, and other reference material is organized in an [Obsidian vault](<[Obsidian vault](https://help.obsidian.md/Home)>). This vault is the source data for [docs.moondao.com](https://docs.moondao.com) through [Obsidian Publish](https://obsidian.md/publish). As an Obsidian vault, all documentation is saved as plain-text files styled with [a flavor of Markdown syntax](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown).

The source files for [docs.moondao.com](https://docs.moondao.com) and other archived documentation are publicly available at [github.com/Official-MoonDao/moondao-vault](https://github.com/Official-MoonDao/moondao-vault).
# Using the vault
The vault is best experienced locally with the Obsidian app.
1. Clone or fork this repository `git clone git@github.com:Official-MoonDao/moondao-vault.git`
2. [Download and install Obsidian](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian)
3. Start Obsidian, choose `Open folder as vault` and select the `moondao-vault` directory from step 1.
## Recommended Plugins
For the best experience, enable the recommended plugins.
### Core Plugins
The following [core plugins](https://help.obsidian.md/Plugins/Core+plugins) are recommended:
- [Backlinks](https://help.obsidian.md/Plugins/Backlinks)
- [Bookmarks](https://help.obsidian.md/Plugins/Bookmarks)
- [Graph view](https://help.obsidian.md/Plugins/Graph+view)
- [Outgoing links](https://help.obsidian.md/Plugins/Outgoing+links)
- [Sync](https://help.obsidian.md/Obsidian+Sync/Introduction+to+Obsidian+Sync)
- [Templates](https://help.obsidian.md/Plugins/Templates)
### Community Plugins
The following [community plugins](https://obsidian.md/plugins) are recommended:
- [Dataview](https://obsidian.md/plugins?id=dataview)
- [Obsidian Git](https://obsidian.md/plugins?id=obsidian-git)
- [Plugin Update Tracker](https://obsidian.md/plugins?id=obsidian-plugin-update-tracker)

Be sure to [turn on community plugins](https://help.obsidian.md/Extending+Obsidian/Community+plugins) in your main settings.
## Keeping your vault up to date
The [Obsidian Git](https://github.com/denolehov/obsidian-git) plugin streamlines automatic commits and syncing to the remote branch.
The vault must be set up as a git repository to use this plugin. If you cloned or forked the repo from GitHub, you're all set.

Nearly all the regular git practices have corresponding commands in Obsidian from the plugin. Pull changes from the main branch with Command Palette → `Obsidian Git: Pull`.
# Contributing to the docs
The documentation vault and website are decoupled. Changes to the vault's source files only propagate to the site through a manual Publish step.
## Submitting changes to the vault
The `main` branch is protected. All changes must be submitted as [Pull Requests](https://github.com/Official-MoonDao/moondao-vault/pulls) into `main`.
