---
cover-img: "assets/images/this-is-fine.jpg"
date: 2022-09-24 06:00:00 +1200
layout: post
readtime: true
tags: [3D printing, Octoprint, Cura]
title: "What have I gotten myself into?"
---

They say that you learn from your mistakes. I learned a lot today.

I wanted to print this cable chain to tidy up the wiring at the back of the printer:

![Cable chain]({{ 'assets/images/cable-chain.jpg' | relative_url }} )

There are a couple of models in this [Thingiverse][thingiverse] thing that need many copies of it printed. I thought it would be a good idea to print as many of them in a single print batch as possible, so I do not have to set up the same print 19 times. I imported the model into Cura and used the multiply function to get the required number of pieces:

![Cura layout]({{ 'assets/images/cura-multiple.png' | relative_url }} )

This looked great so I started the print and went on my merry way. The print was supposed to take around 9 hours. I checked back in after around an hour and already suspected something was wrong. The quality on each of the pieces just wasn't what I expected it to be.

After around 5 hours, things were looking very bad. Some of the pieces were very messy and looked like they had clouds of fine spaghetti plastic on their top. I decided to cancel the print. The pieces would not have been usable and I didn't want to waste even more filament.

I thought about this for a while and realised what the likely problem is. The printer was printing a single layer at a time for all pieces on the print bed. It would print a layer for the first piece, then a layer for the second, and so on. Once all pieces had their first layer printed, it would return to do the second layer on the first piece. The print head was moving so much between all the pieces, leading to the stringing I was seeing. I wonderered if there was a way to print each piece in its entirety before moving on to the next one. I would still be printing one piece at a time but would not need to do all the set up if I were printing a single piece on the print bed at a time.

Turns out there is a setting in Cura for that: Special Modes -> Print Sequence -> One at a Time.

The "downside" with that setting is that you cannot print as many models on the bed, because the print head needs enough clearance when moving between pieces so nothing gets bumped around. I found that I was able to fit 6 of the smaller model on the bed at a time.

I kicked off the next print and immediately saw a problem. For some reason, the first layer was a complete mess. The extruder did not seem to working properly at all. Basically, it looked like the printer stopped working altogether...

<div style="text-align: center"><img src="{{ site.baseurl }}/assets/images/why.gif"></div>

Took me a while to figure out the cause of this one. I noticed an issue at the top of the stepper motor that feeds filament into the bowden tube. There were specs of filament on it and the filament itself had notches taken out of it from the teeth on the stepper motor. This was almost certainly caused by all of the extrusion and retraction of the filament from the disaster of the previous print. I checked the 'Maximum Retraction Count' setting in Cura and it was set to 100. That is WAY too high and it's no suprise I wrecked the filament. I reduced that setting to 5, started a new print and things were back to normal.

![I need a drink]({{ 'assets/images/i-need-a-drink.jpg' | relative_url }} )

The plan for tomorrow is to print the cover of my brother's present. Hopefully it's a more successful day...

[thingiverse]: https://www.thingiverse.com/thing:3769941
