# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# RaspberryPi Pico RP2040 Mechanical Keyboard

import time

import board
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from digitalio import DigitalInOut, Direction, Pull

from map import KEY, MEDIA, SEQ, keymaps_v2

print("---Pico Pad Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)


def run_sequence(kbd: Keyboard, sequence: list):
    for key in sequence:
        kbd.press(key)
        time.sleep(0.1)
        kbd.release(key)
        time.sleep(0.1)


pins = [
    board.GP7,
    board.GP6,
    board.GP20,
    board.GP21,
    board.GP10,
    board.GP9,
    board.GP8,
    board.GP19,
    board.GP11,
    board.GP13,
    board.GP22,
    board.GP18,
]

switches = {}

for i in range(len(pins)):
    switches[i] = DigitalInOut(pins[i])
    switches[i].direction = Direction.INPUT
    switches[i].pull = Pull.UP

switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for button in range(len(pins)):
        if switch_state[button] == 0:
            if not switches[button].value:
                keymap = keymaps_v2[button]
                try:
                    if keymap["type"] == KEY:
                        kbd.press(*keymap["key"])
                    elif keymap["type"] == SEQ:
                        run_sequence(
                            kbd,
                            keymap["key"],
                        )
                    elif keymap["type"] == MEDIA:
                        cc.send(keymap["key"])
                except ValueError:
                    pass
                switch_state[button] = 1

        if switch_state[button] == 1:
            if switches[button].value:
                keymap = keymaps_v2[button]
                try:
                    if keymap["type"] == KEY:
                        kbd.release(*keymap["key"])
                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01)
