import time

import usb_hid
from adafruit_hid.mouse import Mouse

POSITIONS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


class Jiggler:
    def __init__(self, shift: int, wait: float, times: int) -> None:
        self.shift = shift
        self.wait = wait
        self.state = False
        self.mouse = Mouse(usb_hid.devices)
        self.times = times
        self.__init_times = times
        self.current_position = 0

    def resert_times(self):
        self.times = self.__init_times

    def move_mouse_to_next_position(self):
        position = POSITIONS[self.current_position]
        self.current_position = (self.current_position + 1) % len(POSITIONS)
        self.mouse.move(x=position[0] * self.shift, y=position[1] * self.shift)

    def tick(self):
        if self.state:
            if self.times > 0:
                self.times -= 1
                time.sleep(self.wait)
            else:
                self.resert_times()
                self.move_mouse_to_next_position()

    def toggle(self):
        self.state = not self.state
        return self.state

    def start(self):
        self.state = True

    def stop(self):
        self.state = False
