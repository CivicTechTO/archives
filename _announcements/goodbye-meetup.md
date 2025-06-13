---
title: Goodbye, Meetup
author: "[[Gabe Sawhney]]"
date: 2024-11-11
redirect_from: /2024/11/11/goodbye-meetup/
---
**_Summary: Civic Tech Toronto has (at long last) stopped using Meetup, and has moved to Guild for event pages and Publer for social media post scheduling._**

Like many civic tech groups, we’ve been promoting our events on Meetup for years.  For the past few years, though, we’ve been underwhelmed by the service, considering the cost. So when Meetup emailed us this summer to say that our service fees were going up by 80%, we decided it was time to move.

Over the past couple of months we’ve tried out a bunch of different services, and we’ve landed on a set that — so far — are working well for us. We’re sharing this info, because we think there might be other civic tech groups in a similar spot. We hope it’s helpful!

## What we need

Civic Tech Toronto runs a weekly hybrid hacknight in Toronto. We want people to be able to RSVP in a way that makes sense, whether they plan to attend in-person or online.

We’re moving away from a Meetup premium (not Pro) account, which we’ve been paying just over Cdn$300/yr for.

## Meetup wasn’t just one thing

It wasn’t the first time we’d done this research. It’s tricky to move away from Meetup because it’s not just an event subscription and RSVP tool; it’s how a lot of our participants first discovered Civic Tech Toronto. There’s no single tool which can replace Meetup: we knew that in moving away from Meetup, we’d need to step up our event promotion, to make up for the loss of discoverability.

Besides Meetup, we previously would sporadically promote our events through social media (previously Twitter, more recently LinkedIn).

## Moving to Guild

As of this month, we’ve moved to [Guild](http://guild.host/) for our event pages. Guild was the tool we found which most elegantly handled hybrid events. It’s simple, and does exactly what we need it to. It was created specifically for tech community groups, by someone who ran them for years. (Coincidentally, there’s a local connection here: Guild’s founder, Taz Singh, was the founder of TorontoJS. He’s now living in the UK, but still has ties to Toronto, and happened to drop in to one of our hacknights in-person a few weeks ago!)

Guild is free for community groups _by design_. It has a very clean interface and easy to use — a far cry from what Meetup has become!

[Lu.ma](http://lu.ma/) has been getting a lot of attention lately. It seems like a nice platform, but it doesn’t support hybrid events. We’re still considering using it to promote our events, but with Guild as the primary event pages.

## Social media post scheduling

Previously, we relied on Meetup for discoverability. We posted on social media (Twitter, and later LinkedIn) sporadically, as it was a manual process for volunteers. The social media landscape is more fragmented now, and we wanted to bring more consistency to our event promo, which led us to look at social media post scheduling tools.

Most tools in this category are geared to marketers, and priced accordingly. Our needs are relatively basic, and our willingness to pay is comparatively low. We evaluated tools based on: which social media channels they support, ease of use, and cost. Our finalists were [Buffer](http://buffer.com/) and [Publer](http://publer.io/). We tested both and found they both worked well, but Publer was about half the price for what we needed. Once the trial is over, we expect to be paying about Cdn$33/month, for 6 social media channels: LinkedIn, Facebook, Instagram, Threads, Bluesky, Mastodon. (We’ll see how it goes, and maybe adjust those in the future.) It still strikes me as expensive for what we get, but we haven’t yet found a cheaper tool that does what we need. (Suggestions welcomed!)

## Saying goodbye to Meetup

Besides the easy discoverability we got through Meetup, and the over 7000 subscribers we have there, we realized that the other valuable thing we’ll lose by leaving Meetup is the archive of past event pages. These are the best available record of the 468+ events we’ve run over the past 9.5 years — leaving Meetup means we’ll want to grab the content of these pages and post it on our own website.

Sonal discovered that it’s possible to export Meetup page content using their [GraphQL Playground](https://www.meetup.com/api/playground/#graphQl-playground). Our website is currently running WordPress, so I’m currently working with the data in a spreadsheet, in order to generate a bunch of WordPress Pages using the [CSV Importer plugin](https://wordpress.org/plugins/csv-importer/). It’s a slow process, but in the end we’ll have consistent and structured data for past events, and our event pages have videos from YouTube embedded.

All of this has taken some time, and as a volunteer group we can only move so fast. We did need to pay for one more 6-month renewal to our Meetup subscription to give us time to make the transition without being rushed. We managed to avoid paying Meetup’s newly-increased rate by clicking to “cancel” our subscription: it then offered us a renewal at the previous rate.

Our Meetup account is paid up until March 2025. For the month of November we’re using it to point people to our Guild pages, and from December on we plan to stop posting events on Meetup, to see if it results in a drop-off of new participants. Our current plan is to not renew Meetup again.

## Update (Dec 12 2024): ramping up

I’ve been impressed by how quickly people have found us on Guild. Now (early December), about two months after beginning to post our events on Guild — and less than a week into _only_ posting our events on Guild — we have 254 members on Guild. That’s a lot less than the 7179 we have on Meetup, but our peak number of _active_ members on Meetup (in the past 3 years, which is all the data that’s available) was 393, in September 2024. Seems like we might catch up to that by the spring. 

(I’ll update the graph below occasionally…)

![](/assets/images/announcements/goodbye-meetup/guild-followers-vs-date-graph.png)
![](/assets/images/announcements/goodbye-meetup/meetup-total-and-active-members-graph.png)


And we’re doing ok on Bluesky too: with only 9 posts, [@civictechto.bsky.social](https://bsky.app/profile/civictechto.bsky.social) currently has 174 followers. 

_(Thanks to Casey Watts, whose [similar blog post](https://www.caseywatts.com/blog/event-pages-2024/) was an inspiration for this one!)_