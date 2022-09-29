# Pre-programmed LED strip animations for Ratchet & Clank lightbox
#
# Author: Brandon Farrell
# 29/09/2022

import board
import neopixel
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.color import RED

pixel_brightness = 0.5
pixel_num = 30
pixel_pin = board.GP22

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=pixel_brightness, auto_write=False)

blink = Blink(pixels, speed=0.5, color=RED)
