---
tags:
  - docs/onboarding
---
MoonDAO's documentation, planning, project notes, and other reference material is organized in an [Obsidian vault](<[Obsidian vault](https://help.obsidian.md/Home)>). This vault is the source data for [docs.moondao.com](docs.moondao.com) through [Obsidian Publish](https://obsidian.md/publish). As an Obsidian vault, all documentation is saved as plain-text files styled with [a flavor of Markdown syntax](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown).

The source files for [docs.moondao.com](docs.moondao.com) and other archived documentation are publicly available at [github.com/Official-MoonDao/moondao-vault](https://github.com/Official-MoonDao/moondao-vault).
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
### Obsidian Sync Plugin
[Obsidian Sync](https://help.obsidian.md/Obsidian+Sync/Introduction+to+Obsidian+Sync) is a first-party (paid) plugin that automatically downloads and uploads file changes to the vault. Files are only synced when Obsidian is running and connected to the internet.

Contact [@philiplinden](@philiplinden.md) to be invited to connect to the official MoonDAO shared remote vault.

>[!warning] Syncing is two-way!
> 1. Be sure to [set up excluded folders](https://help.obsidian.md/Obsidian+Sync/Select+files+and+settings+to+sync#Exclude+folder+from+being+synced) for private files. Obsidian Sync uploads and downloads everything that is not in an _Excluded Folder_.
> 2. Avoid working on the same note at the same time as another user as it may lead to changes being lost during the sync process.
> 3. Avoid syncing settings and hotkeys, as other users may have different preferences than you.

**Recommended settings**
- [x] Sync images
- [ ] Sync audio
- [ ] Sync video
- [x] Sync PDFs
- [x] Sync all other types
- [ ] Main settings
- [ ] Appearance settings
- [ ] Themes
- [ ] Hotkeys
- [x] Active core plugin list
- [ ] Core plugin settings
- [ ] Active community plugin list
- [x] Installed community plugins
### Git
Clone the repository and pull/push changes with conventional git commands from the command line, GitHub CLI, or your preferred git management tool.

Create a new branch (`git checkout -b my-new-branch`) to make your changes. Use regular git practices to sync changes from the main branch.

1. Commit changes to your working branch (`git add`, `git commit`)
2. Switch to the remote and pull changes (`git switch main`, `git pull`)
3. Switch back to the working branch (`git switch my-new-branch`)
4. Merge or rebase onto the main branch (`git merge main` or `git rebase main`)
### Obsidian Git Plugin
The [Obsidian Git](https://github.com/denolehov/obsidian-git) plugin streamlines automatic commits and syncing to the remote branch.
The vault must be set up as a git repository to use this plugin. If you cloned or forked the repo from GitHub, you're all set.

Nearly all the regular git practices have corresponding commands in Obsidian from the plugin. Pull changes from the main branch with Command Palette → `Obsidian Git: Pull`.

>[!warning]
>Using Obsidian Sync and Obsidian Git plugins concurrently is not recommended. Pick one.
# Contributing to the docs
The documentation vault and website are decoupled. Changes to the vault's source files only propagate to the site through a manual Publish step.
## Submitting changes to the vault
The `main` branch is protected. All changes must be submitted as [Pull Requests](https://github.com/Official-MoonDao/moondao-vault/pulls) into `main`.

>[!warning] Obsidian Sync is not sufficient
> When Sync is enabled, all file changes are propagated to all other users sharing the vault with Obsidian Sync. However, these changes are _not_ propagated to the git repository automatically. A pull request is still required.

## Publishing changes to the site
A curated set of notes from the vault are published to the site. Changes, additions, or deletions must be manually "published" by a whitelisted user before the changes appear on the site.

Contact [@philiplinden](@philiplinden.md) to be invited as a whitelisted contributor.
