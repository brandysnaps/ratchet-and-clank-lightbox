---
date: 2022-09-30 06:00:00 +1300
layout: post
readtime: true
tags: [LEDs, Pico, Raspberry Pi]
title: "Programming the LED strip"
---

Now that everything is sitting where it should be, one of the last things to do is pre-program the Pico with some LED animations based on the pink and blue colour scheme my brother likes:

<img src="{{ site.baseurl }}/assets/images/neon.jpg" height=183>

I am using the `adafruit_led_animation` library for the colours and animations. The first step is to include the required classes from the library, like so:

```python
import board
import neopixel
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
```

The next thing to do is check is if the library provides out-of-the-box colours matching what I have in mind. I found that the `CYAN` colour from `adafruit_led_animation.color` is exactly what I want. Unfortunately, the `PINK`, `MAGENTA` and `PURPLE` colours do not match what I had in mind. Instead, I did some Googling and found a pink I liked. These are the "blue" and "pink" RGB values:

<table>
  <tr>
    <td>
      <img src="{{ 'assets/images/colour-pink.png' | relative_url }}" alt="Not found" />
    </td>
    <td>
      <img src="{{ 'assets/images/colour-cyan.png' | relative_url }}" alt="Not found" />
    </td>
  </tr>
</table>

I set up these colours in the code:

```python
from adafruit_led_animation.color import CYAN

# Define colors here
COLOR_1 = CYAN
COLOR_2 = (216, 0, 166)  # Pink
```

Next, I went through each of the animation types in the [CircuitPython LED Animations][circuitpython-led-animations] document and selected the options I thought looked the best. For example:

```python
chase_1 = Chase(pixels, speed=0.1, color=COLOR_2, size=2, spacing=3)
color_cycle = ColorCycle(pixels, speed=5.0, colors=[COLOR_1, COLOR_2])
comet_1 = Comet(pixels, speed=0.075, color=COLOR_2, bounce=False)
pulse_1 = Pulse(pixels, speed=0.1, color=COLOR_1, period=5)
```

Lastly, I had to configure an `AnimationSequence` to cycle through all of the animations I set up. I decided to let the animations be chosen at random, and for each animation to play for 60 seconds:

```python
animations = AnimationSequence(
    chase_1,
    chase_2,
    color_cycle,
    comet_1,
    comet_2,
    pulse_1,
    pulse_2,
    solid_1,
    solid_2,
    sparkle_1,
    sparkle_2,
    sparkle_pulse_1,
    sparkle_pulse_2,
    advance_interval=60,
    auto_clear=True,
    random_order=True,
)
```

Here is the complete code for reference:

```python
# Pre-programmed LED strip animations for Ratchet & Clank lightbox
#
# API documentation: https://docs.circuitpython.org/projects/led-animation/en/latest/
#
# Author: Brandon Farrell
# 29/09/2022

import board
import neopixel
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.color import CYAN

# Define colors here
COLOR_1 = CYAN
COLOR_2 = (216, 0, 166)  # Pink

# LED attributes
pixel_brightness = 0.5
pixel_num = 30
pixel_pin = board.GP22

pixels = neopixel.NeoPixel(
    pixel_pin, pixel_num, brightness=pixel_brightness, auto_write=False
)

# Animations
chase_1 = Chase(pixels, speed=0.1, color=COLOR_2, size=2, spacing=3)
chase_2 = Chase(pixels, speed=0.1, color=COLOR_1, size=2, spacing=3)
color_cycle = ColorCycle(pixels, speed=5.0, colors=[COLOR_1, COLOR_2])
comet_1 = Comet(pixels, speed=0.075, color=COLOR_2, bounce=False)
comet_2 = Comet(pixels, speed=0.075, color=COLOR_1, bounce=False)
pulse_1 = Pulse(pixels, speed=0.1, color=COLOR_1, period=5)
pulse_2 = Pulse(pixels, speed=0.1, color=COLOR_2, period=5)
solid_1 = Solid(pixels, color=COLOR_1)
solid_2 = Solid(pixels, color=COLOR_2)
sparkle_1 = Sparkle(pixels, speed=0.05, color=COLOR_1)
sparkle_2 = Sparkle(pixels, speed=0.05, color=COLOR_2)
sparkle_pulse_1 = SparklePulse(
    pixels, speed=0.05, period=5, min_intensity=0, max_intensity=1.0, color=COLOR_1
)
sparkle_pulse_2 = SparklePulse(
    pixels, speed=0.05, period=5, min_intensity=0, max_intensity=1.0, color=COLOR_2
)

animations = AnimationSequence(
    chase_1,
    chase_2,
    color_cycle,
    comet_1,
    comet_2,
    pulse_1,
    pulse_2,
    solid_1,
    solid_2,
    sparkle_1,
    sparkle_2,
    sparkle_pulse_1,
    sparkle_pulse_2,
    advance_interval=60,
    auto_clear=True,
    random_order=True,
)

while True:
    animations.animate()

```

Once the complete code had been successfully uploaded to the Pico, I disconnected it and started packaging it in the box I will give my brother...

<div style="text-align: center"><img src="{{ site.baseurl }}/assets/images/excited.gif"></div>

## QR Code

It's a small thing but excited me nonetheless. I created a QR code linking to the website. I will make the site live tonight.

![QR code]( {{ 'assets/images/qr-code.png' | relative_url }})

[circuitpython-led-animations]: https://learn.adafruit.com/circuitpython-led-animations
