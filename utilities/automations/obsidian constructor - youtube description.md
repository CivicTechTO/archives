---
description: A dataview supported youtube description constructor. Inserted hacknight reference will populate the necessary structured text for youtube video descriptions.
reference: "[[480]]"
---

Hacknight #`=this.reference.number` with `=this.reference.speakers`: `=this.reference.topic`

---

Recorded `= dateformat(this.reference.date, "DD")`

Topic: `=this.reference.topic` 

`=this.reference.description `


Speakers:

`= choice(length(this.reference.speakers) > 1, join(map(this.reference.speakers, (x) => x.name + " – " + x.description), "<br/><br/><br/>"), map(this.reference.speakers, (x) => x.name + " – " + x.description))`


`= [[about us]].contents`

