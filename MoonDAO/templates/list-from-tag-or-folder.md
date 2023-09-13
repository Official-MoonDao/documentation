<%*  
const dv = app.plugins.plugins["dataview"].api;  
const query = 'list From ' + tp.system.prompt('tag or folder', true);  
let out = await dv.queryMarkdown(query)  
tR += out.value
%>