# Map for 3 row 4 column
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode

from jiggler import Jiggler

MEDIA = 1
KEY = 2
SEQ = 3
JIGGLE = 4

jiggler = Jiggler(4, 0.3)

keymaps_v2 = [
    {"type": KEY, "key": [Keycode.ALT, Keycode.ONE]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.TWO]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.THREE]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.FOUR]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.FIVE]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.SIX]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.SEVEN]},
    {"type": KEY, "key": [Keycode.ALT, Keycode.EIGHT]},
    {"type": MEDIA, "key": ConsumerControlCode.SCAN_PREVIOUS_TRACK},
    {"type": MEDIA, "key": ConsumerControlCode.PLAY_PAUSE},
    {"type": JIGGLE, "key": jiggler.start},
    {"type": JIGGLE, "key": jiggler.stop},
]


# keymaps_v2 = [
#     {"type": KEY, "key": [Keycode.ALT, Keycode.ONE]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.TWO]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.THREE]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.FOUR]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.FIVE]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.SIX]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.SEVEN]},
#     {"type": KEY, "key": [Keycode.ALT, Keycode.EIGHT]},
#     {"type": MEDIA, "key": ConsumerControlCode.SCAN_PREVIOUS_TRACK},
#     {"type": MEDIA, "key": ConsumerControlCode.PLAY_PAUSE},
#     {"type": MEDIA, "key": ConsumerControlCode.MUTE},
#     {"type": MEDIA, "key": ConsumerControlCode.SCAN_NEXT_TRACK},
# ]
