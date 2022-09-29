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
from adafruit_led_animation.color import CYAN

# Define custom colors here
CUSTOM_PINK = (216, 0, 166)

# LED attributes
pixel_brightness = 0.5
pixel_num = 30
pixel_pin = board.GP22

pixels = neopixel.NeoPixel(
    pixel_pin, pixel_num, brightness=pixel_brightness, auto_write=False
)

# Animations
solid_1 = Solid(pixels, color=CYAN)
solid_2 = Solid(pixels, color=CUSTOM_PINK)
color_cycle = ColorCycle(pixels, speed=5.0, colors=[CYAN, CUSTOM_PINK])
chase_1 = Chase(pixels, speed=0.1, color=CUSTOM_PINK, size=2, spacing=3)
chase_2 = Chase(pixels, speed=0.1, color=CYAN, size=2, spacing=3)
comet_1 = Comet(pixels, speed=0.075, color=CUSTOM_PINK, bounce=False)
comet_2 = Comet(pixels, speed=0.075, color=CYAN, bounce=False)
pulse_1 = Pulse(pixels, speed=0.1, color=CYAN, period=5)
pulse_2 = Pulse(pixels, speed=0.1, color=CUSTOM_PINK, period=5)

animations = AnimationSequence(
    solid_1,
    solid_2,
    color_cycle,
    chase_1,
    chase_2,
    comet_1,
    comet_2,
    pulse_1,
    pulse_2,
    advance_interval=60,
    auto_clear=True,
    random_order=True,
)

while True:
    animations.animate()
