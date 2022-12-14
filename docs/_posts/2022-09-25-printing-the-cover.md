---
cover-img: assets/images/cover-finished.jpg
date: 2022-09-25 07:00:00 +1200
layout: post
readtime: true
tags: [3D printing, Octoprint]
title: "Printing the cover"
---

​I kicked the cover print off just after 7 am this morning. I got the slicing sorted in Cura first and then loaded the GCode into Octoprint. I was happy with the first layer and print adhesion:

![First layer]( {{ 'assets/images/cover-first-layer.jpg' | relative_url }} )

I checked in on the print every now and then on my phone, to make sure nothing catastrophic was going on. After a few hours, you could start to see the infill being printed:

![Infill]( {{ 'assets/images/cover-infill.jpg' | relative_url }} )

I managed to grab a screenshot of the GCode viewer just before the last layer was finished:

![Final layer]( {{ 'assets/images/gcode-viewer.png' | relative_url }} )

After 7 hours 28 minutes and 13.18 m of filament, the cover was done!

I waited a while to let the bed cool before very carefully removing the print. The print quality was extremely good and after removing some minor imperfections and stringing, this is the finished result:

![Finished cover]( {{ 'assets/images/cover-finished.jpg' | relative_url }} )

I really want the finished gift to be black. I only have grey and orange filament at the moment so I went and bought some black spray paint from the local hardware store. Yet another thing to learn how to do.

<div style="text-align: center"><img src="{{ site.baseurl }}/assets/images/fresh-prince.gif"></div>

Later in the evening, I spent more time trying to figure out the internals of the enclosure. There is a lot to think about and fit in so I sketched my thoughts out.

The inside of the enclosure will be laid out roughly as follows:

![Enclosure layout]( {{ 'assets/images/enclosure-layout.png' | relative_url }} )

The LED strip will be attached to the internal wall of the enclosure in a clockwise direction, starting at the Raspberry Pi Pico. There will be nine LEDs on each face except for the bottom, where there will only be three. This should not be a problem as the majority of the bottom portion of the cover is solid, meaning no light will come through anyway.

I have included two cylindrical LED strip supports on each side, similar to the Hexaleaf design:

![Hexaleaf design]( {{ 'assets/images/hexaleaf-dimensions.png' | relative_url }} )

Cross-section where there is an LED strip support:

![Enclosure cross-section w/ support]( {{ 'assets/images/enclosure-dimensions-support.png' | relative_url }} )

Cross-section where there is no LED strip support:

![Enclosure cross-section w/o support]( {{ 'assets/images/enclosure-dimensions-no-support.png' | relative_url }} )

Tomorrow I will need to try and get this modelled in Tinkercad.
