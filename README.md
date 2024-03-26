[MoonDAO](https://moondao.com) documentation, planning, project notes, and other reference material.
Markdown files in `MoonDAO/docs` are used to generate MoonDAO's [public documentation](https://docs.moondao.com)
# How To Update MoonDAO’s Documentation  

MoonDAO’s documentation is stored in [markdown format](https://www.markdownguide.org/basic-syntax/) in a Github repository and also makes use of Obsidian-flavored [backlinks](https://help.obsidian.md/Plugins/Backlinks) and [frontmatter properties](https://help.obsidian.md/Editing+and+formatting/Properties). These markdown files are presented in [our documentation](https://docs.moondao.com/) using [Quartz](https://quartz.jzhao.xyz/authoring-content).  
To propose an edit to the documentation, follow the steps below.  
  
**1.** [Create a Github account](https://github.com/) and sign in  
  
**2.**  [Follow this link](https://github.com/Official-MoonDao/documentation/fork) to create a copy of the documents (also called a ‘fork’ of the ‘repo’). You may optionally change the name and description of the repo, or just continue with the default values.  
	*Note: Before making changes, ensure your fork is updated with the original repository to avoid merge conflicts. If your fork is behind, indicated by 'This branch is [# of commits] commits behind Official-MoonDao/documentation:main', update it by selecting 'Update Branch' under the 'Sync Fork' dropdown..*  
  
**3.** Click the green ‘CODE’ dropdown button, select the ‘Codespaces’ tab, and click the “Create Codespace On Main” button. The codespace will be opened in a new tab.  
	Note: Experienced or frequent users may consider use of [Obsidian](https://obsidian.md/) as a local editor paired with commands in the CLI to sync branches and open pull requests*  
  
**4.** In the explorer window, navigate to MoonDAO>Docs and click the markdown file you intend to edit and implement the desired updates, or create a new entry by clicking the ‘New File’ button at the top of the left navigation menu.  
	*Note: All markdown files located within the ‘docs’ folder will be displayed in the navigation menu in our documentation. To add a file without adding it in the navigation menu, ensure it’s added into the ‘reference’ folder. To remove a file from the front-end entirely (while keeping reference to it in the repo), place it within the ‘archive’ folder.  
  
**5.** After the changes are finalized, navigate to the source control view (CTRL+SHIFT+G), enter a summary description of the change in the ‘message’ input field and click the green ‘COMMIT’ button

**6.** In the modal that asks, ‘Would you like to stage all your changes and commit them directly?, select ‘yes’, click the green ‘SYNC CHANGES’ button, and in the modal popup, select ‘OK’  
  
**7.** Go back to the previous tab, refresh the page, and under the ‘contribute’ dropdown, click ‘Open Pull Request’. You’ll be prompted to review the changes before again clicking the green ‘Open Pull Request’ button  
  
**8.** Optionally, enter a detailed description of the changes in the longtext field and again click the green ‘Open Pull Request’ button. ‘And that’s it! Simply wait for a member of our team to review and approve the changes