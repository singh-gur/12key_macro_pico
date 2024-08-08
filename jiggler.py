import time

import usb_hid
from adafruit_hid.mouse import Mouse


class Jiggler:
    def __init__(self, shift: int, wait: float) -> None:
        self.shift = shift
        self.wait = wait
        self.state = False
        self.mouse = Mouse(usb_hid.devices)

    def tick(self):
        if self.state:
            self.mouse.move(x=self.shift, y=self.shift)
            time.sleep(self.wait)
            self.mouse.move(x=self.shift, y=-self.shift)
            time.sleep(self.wait)
            self.mouse.move(x=-self.shift, y=-self.shift)
            time.sleep(self.wait)
            self.mouse.move(x=-self.shift, y=self.shift)
            time.sleep(self.wait)

    def toggle(self):
        self.state = not self.state
        return self.state

    def start(self):
        self.state = True

    def stop(self):
        self.state = False
