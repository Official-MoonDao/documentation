---
tags: docs/team
id: team
title: Our Team
description: Get to know our growing team of Contributors.
keywords:
  [
    Contributors,
    Team,
    Core Team,
    Progressive Governance,
    Titles,
    Astronauts,
    Cosmonauts,
    Rocketeers,
    Moon Settlers,
    Earthlings,
    Subject Roles,
  ]
sidebar_label: Team
sidebar_position: 8
---
This page is editable for our members, if they would like to include a bio about who they are and what brought them to this project.

## MoonDAO Members
See [Roles](Roles.md) for a description of each role.

```dataview
TABLE WITHOUT ID file.link as Member, roles as Roles, member_since as "Member Since", Bio
FROM #moondao/member and -"templates"
SORT member_since ASC
SORT choice(contains(roles,"Astronaut"), 1, choice(contains(roles,"Rocketeer"), 2, choice(contains(roles,"Moon Settler"), 3, choice(contains(roles,"Explorer"), 4, "other")))) ASC
```
