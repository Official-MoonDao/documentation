[MoonDAO](https://www.moondao.com) documentation, planning, project notes, and other reference material.
Markdown files in `MoonDAO/docs` are used to generate MoonDAO's [public documentation](https://docs.moondao.com).

This repository is compatible with [Obsidian](https://help.obsidian.md/Home).

[![build-and-deploy](https://github.com/Official-MoonDao/moondao-vault/actions/workflows/build-and-deploy.yaml/badge.svg?branch=main)](https://github.com/Official-MoonDao/moondao-vault/actions/workflows/build-and-deploy.yaml)

## Making changes
These docs are a collection of markdown files so you can use any text editor to make changes.
The recommended way to work with this repository is by cloning it and [opening the folder as an Obsidian vault](https://help.obsidian.md/Files+and+folders/Manage+vaults#Create+vault+from+an+existing+folder).

The official documentation in `MoonDAO/docs` use Obsidian-flavored [backlinks](https://help.obsidian.md/Plugins/Backlinks) and [frontmatter properties](https://help.obsidian.md/Editing+and+formatting/Properties) that add extra functionality when using Obsidian to read and edit files.

### Keeping private files private
1. **Add a file or directory (incl. wildcards) to `.gitignore`** to exclude them from the repository altogether. This instructs git to ignore any changes to matching files when it looks for updates to your local repository. This is global for the whole repository, and affects everyone who clones the repo too.
2. **Add `draft: true` to the file's frontmatter** to sync the file to the repository but do not allow it to be published on the generated docs site.
3. **Clone this repo as a subdirectory of an existing vault** to use your own Obsidian workspace alongside this vault without syncing your files to this repo. In order to sync changes, pulls and pushes must be done from this repository, but all changes outside this repo's root directory will be ignored.

### Look and feel
By default, local Obsidian customizations (in the `.obsidian` folder) are not synced to the repo. Use whatever plugins and themes you want for your cloned repo.

The site generated from `MoonDAO/docs` is customized in a roundabout way since this repo is meant for only MoonDAO files but Quartz relies on files cloned from [the official repo](https://github.com/jackyzha0/quartz) for [configuration](https://quartz.jzhao.xyz/configuration). We only install and invoke Quartz on the CI/CD runner so Quartz files are not stored in our repo. To get around this problem of keeping "dead" code from Quartz in our repo, we only store modified quartz files in this repo and overwrite the default files during the GitHub Actions workflow. That way we only keep relevant, customized files in the repo. All files in `.site-config/` are copied to the Quartz root during a build.  It's literally a recursive copy. The site can be completely configured by making modifications to Quartz files and merging them to the `.site-config` directory here.

## Publishing changes
The documentation site is automatically built and deployed after every new commit to the main branch.
Clone this repository, make changes, and submit a [Pull Request](https://github.com/Official-MoonDao/moondao-vault/compare) to contribute.

The documentation site is generated with [Quartz](https://quartz.jzhao.xyz/authoring-content). A markdown file in `MoonDAO/docs` can be excluded from the site by adding `draft: true` to the YAML frontmatter.

```yaml
---
title: Example Title
draft: true
tags:
  - example-tag
---
```

At this time, Quartz only supports some of Obsidian's core plugins (e.g. Backlinks, Callouts, Graph View, Mermaid diagrams, etc.). [Click here for a full list of features supported by Quartz](https://quartz.jzhao.xyz/features/). Community plugins like [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) will not be rendered properly on the generated site and just show up as raw text.

## Staying up to date
Be sure to regularly sync your local repository like any other git repo. Avoid change conflicts by working on a separate branch from `main`, and occasionally merge `main` to your working branch.

The **[Obsidian Git](https://github.com/denolehov/obsidian-git)** community plugin adds some shortcuts and convenience tools for backing up your work to git directly from Obsidian. Clone the repository and pull/push changes with conventional git commands. The plugin streamlines automatic commits and syncing to the remote.
