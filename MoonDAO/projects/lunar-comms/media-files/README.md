This folder is used to store media files that act as attachments in other notes. 
Any file that is not a text file (images, pdfs, audio, video) is an attachment if it is embedded in another note with the syntax.

Obsidian supports relative or absolute links, and `[[Wikilinks]]` syntax. For media to appear in GitHub's markdown web viewer, however, media must be embedded with the following syntax: `![alt text](lunar-comms/media-files/filename)`

## Configuring your local vault
Please configure your Obsidian settings to place new attachments in the `media-files` folder.

(The instructions below are a functional example of embedding images by pasting them here, and having Obsidian set up to save the image to `/media-files`)

### 1. Open `Files & Links` settings
Open your local Obsidian vault settings and choose the _Files & Links_ tab.

![](Pasted%20image%2020230811210329.png)

### 2. Configure attachment settings
Set the default location for new attachments to be _In the folder specified below_. Then specify `media-files` as the attachment folder path.

![](Pasted%20image%2020230811210521.png)