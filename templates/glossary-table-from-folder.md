<%*  
const dv = app.plugins.plugins["dataview"].api;  
const query = 'TABLE WITHOUT ID file.link as Term, Definition, Related, aliases as AKA FROM "reference/Glossary" and -"templates"';  
let out = await dv.queryMarkdown(query)  
tR += out.value
%>