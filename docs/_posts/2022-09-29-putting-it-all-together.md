---
cover-img: assets/images/a-team.jpg
date: 2022-09-29 06:00:00 +1300
layout: post
readtime: true
title: "Putting it all together"
---

Now that the printed parts are dry, I have a few things to do:

* Fit test
* Soldering the connector wires to the LED strip
* Fitting the LED strip inside the enclosure
* Fitting the diffustion paper in the enclosure

## Fit Test

![Fit test]( {{ 'assets/images/fit-test-sprayed.jpg' | relative_url }} )

I am so happy with how the project is looking. The spray paint did not add any noticeable thickness to the pieces so the fit is still not that snug. Looks like I will have to use Blu-Tack or similar to hold the cover in place. That is not a big deal as long as it's not visible. Blu-Tack means the cover can be easily removed at any time to allow access to the internals.

## Soldering the Connector Wires

I soldered some female connector wires on the input end of the LED strip to allow it to easily be attached to the Pico. I soldered some male connector wires on the output end of the LED strip to allow it to easily be extended in the future:

![LED strip soldered]( {{ 'assets/images/led-strip-soldered.jpg' | relative_url }} )

## Fitting the LED Strip

I carefully bent the LED strip at the locations of corners inside the enclosure. I did a quick fit test to make sure there were the correct number of LEDs per side and that the LED strip supports would not get in the way of the LEDs. Once I was happy, I removed the backing from strip to reveal the adhesive and stuck it to the walls of the enclosure. This is the result:

![LED strip fitted]( {{ 'assets/images/led-strip-fitted.jpg' | relative_url }} )

It's looking very clean if I do say so myself.

## Diffusion Paper and Cover

I cut a piece of diffusion paper (lol just joking - it's normal A4 printer paper) to size, and placed it on the inner lip of the enclosure. Next, I placed the cover on top. Are you ready for it? This is the first time everything has been put together and pretty much exactly represents the completed project:

...

<div style="text-align: center"><img src="{{ site.baseurl }}/assets/images/wait-for-it.gif"></div>

...

![Fully assembled]( {{ 'assets/images/put-together-lights-off.jpg' | relative_url }} )

Beautiful.

I wrote some basic code to get a rainbow displaying on the LED strip to see what it looks like diffusing through the paper:

![Rainbow]( {{ 'assets/images/put-together-lights-on.jpg' | relative_url }} )

I'm a little disappointed with how much you can see the LEDs through the paper but there is not much I can do about that at this stage. I really need more vertical clearance between the LEDS and the paper but that would require another 3D print. I could look at printing the diffuser with some white filament in the future but don't have any on hand.

I'm sure this won't bother anyone else but I find that I tend to get critical of everything when I have been working on a project for so long 😩. Oh well, I am 93% happy.
