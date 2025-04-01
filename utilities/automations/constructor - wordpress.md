---
description: A dataview supported wordpress description constructor. Inserted hacknight reference will populate the necessary structured text for wordpress page.
reference: "[[486]]"
---

Hacknight #`=this.reference.number` with `=this.reference.speakers`: `=this.reference.topic`

---

`=this.reference.videoUrl `

**Date:** `=this.reference.date `

**Topic:** `=this.reference.topic`

`=this.reference.description `

`=this.reference.link_mentions `


**Speakers:**

`= choice(length(this.reference.speakers) > 1, join(map(this.reference.speakers, (x) => x.name + " – " + x.description), "<br/><br/><br/>"), map(this.reference.speakers, (x) => x.name + " – " + x.description))`


**Venue:** `=this.reference.venue`
