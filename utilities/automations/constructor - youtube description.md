---
description: A dataview supported youtube description constructor. Inserted hacknight reference will populate the necessary structured text for youtube video descriptions.
reference: "[[89]]"
---

Hacknight #`=this.reference.number` with `=this.reference.speakers`: `=this.reference.topic`

---

Recorded `= dateformat(this.reference.date, "DD")`

Topic: `=this.reference.topic` 

`=this.reference.description `

`=this.reference.link_mentions `


Speakers:
`= choice(length(this.reference.speakers) > 1, join(map(this.reference.speakers, (x) => x.title + " – " + x.description), "<br/><br/><br/>"), map(this.reference.speakers, (x) => x.title + " – " + x.description))`


`= [[about us]].contents`

