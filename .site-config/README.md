# site-config
The static site generated from this repository is built with [Quartz](https://quartz.jzhao.xyz).
Files in this folder are copied to the root directory of the quartz repo when
it is initialized in the GitHub Actions workflow. If a file already exists
along that path, it is overridden by whatever is included here.

This way we can add new files and override the defaults without maintaining
the whole Quartz repo.
