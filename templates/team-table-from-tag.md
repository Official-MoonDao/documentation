<%*  
const dv = app.plugins.plugins["dataview"].api;  
const query = 'TABLE WITHOUT ID file.link as Member, roles as Roles, member_since as "Member Since", Bio FROM #moondao/member and -"templates" SORT member_since ASC SORT choice(contains(roles,"Astronaut"), 1, choice(contains(roles,"Rocketeer"), 2, choice(contains(roles,"Moon Settler"), 3, choice(contains(roles,"Explorer"), 4, "other")))) ASC';  
let out = await dv.queryMarkdown(query)  
tR += out.value
%>