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
from adafruit_led_animation.animation.customcolorchase import CustomColorChase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.color import CYAN

CYCLE_TIME = 60

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
comet_1 = Comet(pixels, speed=0.075, color=COLOR_2, bounce=False, ring=True)
comet_2 = Comet(pixels, speed=0.075, color=COLOR_1, bounce=False, ring=True)
custom_color_chase_1 = CustomColorChase(
    pixels, speed=CYCLE_TIME, colors=[COLOR_1, COLOR_2], size=15, spacing=0
)
custom_color_chase_2 = CustomColorChase(
    pixels, speed=CYCLE_TIME, colors=[COLOR_2, COLOR_1], size=15, spacing=0
)
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
    custom_color_chase_1,
    custom_color_chase_2,
    pulse_1,
    pulse_2,
    solid_1,
    solid_2,
    sparkle_1,
    sparkle_2,
    sparkle_pulse_1,
    sparkle_pulse_2,
    advance_interval=CYCLE_TIME,
    auto_clear=True,
    random_order=True,
)

while True:
    animations.animate()
