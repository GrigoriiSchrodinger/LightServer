import threading

import yeelight
from yeelight import Bulb


class LampsControl:
    def __init__(self, ip_lamp: str):
        self._connect = Bulb(ip_lamp)

    def check(self):
        try:
            self._connect.get_properties()
            return True
        except yeelight.main.BulbException:
            return False

    def get_status(self):
        return self._connect.get_properties()["power"]

    def on(self):
        turn_on_thread = threading.Thread(target=self._connect.turn_on)
        turn_on_thread.start()

    def off(self):
        turn_off_thread = threading.Thread(target=self._connect.turn_off)
        turn_off_thread.start()




