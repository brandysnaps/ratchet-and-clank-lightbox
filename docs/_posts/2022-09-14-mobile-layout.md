---
date: 2022-09-14 06:00:00 +1200
layout: post
readtime: true
title: "Fixing the mobile layout"
---
Having a look at the mobile layout for the website reveals a couple of issues:

![Mobile issues]({{ site.baseurl }}/assets/images/mobile_issues.png)

Firstly, the main site heading is covered by the centered avatar. There is also a random navigation button up the top right that has nothing in it.

I decided to shorten the main site title to `R&C Lightbox` as there are other references to the full name elsewhere. That addresses the first issue but unfortunately I was not able to find a fast and good solution to the second problem. My opitons would be to update the beautiful-jekyll theme with custom logic for mobile, or create an issue on the project itself asking the author to fix it. I am short on time so will leave it as is for now. If I do end up adding any other page types to the site, this will not be an issue as the navigation button will no longer be empty.
