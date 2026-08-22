---
description: A dataview supported youtube description constructor. Inserted meetup reference will populate the necessary structured text for youtube video descriptions.
reference: "[[556]]"
---
`=this.reference.topic`

📍 `=this.reference.venue`

---

Meetup #`=this.reference.number` with `=this.reference.speakers`

===

Recorded: `= dateformat(this.reference.date, "DD")`

Topic: `=this.reference.topic`

`=this.reference.description `

(insert any links here)

===

Speakers:

`= choice(length(this.reference.speakers) > 1, join(map(this.reference.speakers, (x) => x.title + " – " + x.description), "<br/><br/>"), map(this.reference.speakers, (x) => x.title + " – " + x.description))`

===

`= [[about us]].contents`
