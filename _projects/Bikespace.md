---
title: Bikespace
excerpt: BikeSpace is a free web app run by volunteers from Civic Tech Toronto that allows users to report issues with bicycle parking in Toronto.
project_pitch: TBD
categories:
  - active
  - open
  - from-breakout
project_website: https://bikespace.ca/
hacknight:
  - "[[419]]"
  - "[[122]]"
  - "[[123]]"
  - "[[152]]"
  - "[[175]]"
tags:
  - type/project
  - topic/transport
  - topic/cycling
project_github: https://github.com/bikespace/bikespace
project_slack: https://civictechto.slack.com/archives/C61CZLA5V
dateActiveFirst: 2017-06-27
social:
  website: https://bikespace.ca/
  email: bikespaceto@gmail.com
  github: https://github.com/bikespace
feature: true
online: true
launched: true
fromBreakout: true
source: airtable original
status_community: open/active
status_archive: reviewing
team:
  - "[[Jake Miller]]"
  - "[[Sonal Ranjit]]"
  - "[[Ollie Sheldrick]]"
  - "[[Ben Coleman]]"
---

## Summary

BikeSpace is a free web app run by volunteers from Civic Tech Toronto that allows users to report issues with bicycle parking in Toronto (e.g. broken post and rings, locked abandoned bikes, and areas where bicycle parking is not provided). Since it was originally launched in partnership with the City of Toronto in 2018, it has collected over 1,000 user reports of bicycle parking issues. The goal of the web app is to support data-driven solutions to bicycle parking needs by crowd-sourcing reports from people in Toronto.

These reports are all viewable on an interactive dashboard that city planners, researchers, and property owners can use to identify bike parking that needs to be installed or fixed. The data is also available via an open API.

The BikeSpace project also aims to provide information about bicycle parking in Toronto, and has a map of known bicycle parking locations on its homepage, which was made using City of Toronto Open Data.

## Issue: Bicycle Parking

We believe that cycling — and its benefits for convenience, health, and the climate — should be accessible to everyone. Unfortunately, a lack of secure, easy-to-access bicycle parking and the fear of bike theft are significant barriers for cyclists. 

A 2019 City of Toronto survey found that improving regular and secure bicycle parking were top needs among cyclists [^1], and other research has found that a lack of bicycle parking is a particularly significant barrier for women who want to cycle [^2].

Secure and convenient bicycle parking helps to prevent theft, which can discourage people from cycling. A recent study in California found that after theft of their bicycle, 45% of people cycled less often or stopped altogether [^3]. The study found that this rate was higher at 83% for occasional cyclists, and E-bike users were more likely to switch back to non-sustainable transit after theft.

E-bikes and cargo bikes are particularly compelling alternatives to driving — and therefore powerful options to reduce the risks and impacts of climate change — but are most in need of secure bicycle parking due to their higher value as well as their space and charging needs.

Bicycle parking at home is also a significant challenge for many people in Toronto, especially in apartment buildings. Data from the City of Toronto’s RentSafeTO program shows that only 3% of units in Toronto have bicycle parking facilities with the capacity required by current zoning rules [^4]. 57% of units have no access to on-site bicycle parking at all, a rate that increases to over 75% for units located in Toronto’s Neighbourhood Improvement Areas.

## Project Approach

Around 2017, the City of Toronto approached Civic Tech Toronto with the idea of making an app to crowdsource locations where bicycle parking needed to be installed, improved, or repaired. The City paid for app hosting and a part-time project manager, but otherwise the design and development was all volunteer-run. 

The BikeSpace project served as a notable and early example in Canada of how government could work hand in hand with the civic tech community. At its peak, there were about 20 regular volunteer contributors in various technical and non-technical roles, and some civic tech volunteers in Edmonton also got in touch to make their own version of the app.

The app launched around summer 2018, and collected reports for a couple years. However, it stopped being actively maintained, and the web hosting (which at that point was being paid for by Code for Canada) was cut off in mid-2021.

A couple years later, one of the original volunteers started organizing to get the BikeSpace app running again. The BikeSpace reporting app was re-launched in August 2023 and the dashboard was re-launched in Jan 2024, with additional work through to May to add features and make it mobile-friendly. BikeSpace now has around 5-8 regular contributors, and the volunteer team continues to work on additional app improvements, community outreach, and making an improved map of where to find bicycle parking in Toronto.

Two significant challenges with BikeSpace today are keeping an all-volunteer team organized and motivated and providing an online service using free services (except for its donated domain name). The project has an open organizational structure where documentation and frequent onboarding allows for volunteers to contribute more or less, depending on their time available. The wider Civic Tech Toronto community also plays an essential role in fostering a community of support for the project team and bringing in new contributors. The app is also architected to minimize costs and “moving parts”, leaning heavily on front-end code and only using server resources for back-end data.

The project uses various City of Toronto open data on bicycle parking locations to help in reporting damaged parking to the City as well as on an easy-to-use map on its homepage. Other open data on the City’s safe cycling network and apartment buildings helps to provide useful context for BikeSpace research work.

Since its inception, there have been over 1,000 bicycle parking issues reported using the BikeSpace app, and the project has brought greater attention to the issue of bicycle parking through community outreach and media coverage. It has also provided an invaluable opportunity for many volunteers with technical, civic engagement, user design, and advocacy skills to work together and contribute something back to people in Toronto.

## Project Impact

When BikeSpace originally launched, issues with existing bicycle parking could only be reported to 311 via phone or email. The app provided a much more accurate and simple way to report bicycle parking issues, with a handful of quick questions. Since then, the City has launched an online 311 portal in 2021 and a mobile 311 app in 2022, giving more options for members of the public to report abandoned bicycles and broken post and rings.

The BikeSpace app still provides a quick and simple way to report issues not yet covered by 311, including reporting issues related to privately-owned bicycle parking, reporting bicycle racks as full, and requesting new bicycle parking installations from the City. The City continues to feature BikeSpace as a reporting option on their own bicycle parking webpage [^5], and it remains the simplest way to report bicycle parking issues in Toronto, with over 1,000 issues reported to-date.

In the fall of 2018, the post-launch report to the City estimated that over 1,800 volunteer hours had been contributed to the BikeSpace project, with an estimated value of over $50,000. The number of hours contributed has only grown since then, with a significant public benefit arising from the contributions of skilled volunteers.

The BikeSpace app has received media coverage from the CBC, CP24, UofT News, Daily Hive, and the Two Wheeled Politics blog, helping to increase awareness and public discussion around the issue of safe and convenient bicycle parking.


[^1]: Nanos Research. (2019). City of Toronto Cycling Study. City of Toronto. Retrieved November 29, 2024, from https://www.toronto.ca/wp-content/uploads/2021/04/8f76-2019-Cycling-Public-Option-Survey-City-of-Toronto-Cycling.pdf.
[^2]: Manaugh, K., Boisjoly, G., & El-Geneidy, A. (2017). Overcoming barriers to cycling: understanding frequency of cycling in a University setting and the factors preventing commuters from cycling on a regular basis. Transportation, 44, 871-884.
[^3]: Cohen, A., Nelson, T., Zanotto, M., Fitch-Polse, D. T., Schattle, L., Herr, S., & Winters, M. (2024). The impact of bicycle theft on ridership behavior. International Journal of Sustainable Transportation, 1-11. https://www.tandfonline.com/doi/full/10.1080/15568318.2024.2350946
[^4]: Municipal Licensing & Standards. (2024). Apartment Building Registration [Data set]. City of Toronto. Retrieved October 13, 2024, from https://open.toronto.ca/dataset/apartment-building-registration/
[^5]: https://www.toronto.ca/services-payments/streets-parking-transportation/cycling-in-toronto/bicycle-parking/