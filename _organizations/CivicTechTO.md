---
tags:
  - type/organization
---
## Organizers
```dataview
LIST
FROM "people"
WHERE contains(organization, [[CivicTechTO]]) AND contains(file.tags, "#type/organizer")
SORT name asc
```
