import json
import threading
import yeelight

from yeelight import Bulb


class LampsControl:
    def __init__(self, ip_lamp: str, dead: int):
        self._connect = Bulb(ip_lamp)
        self._dead = dead

    def check(self):
        try:
            self._connect.get_properties()
            return True
        except yeelight.main.BulbException:
            return False

    def get_status(self):
        return self._connect.get_properties()

    def set_config(self, json_data):
        self._connect.turn_on()

        if 'bright' in json_data:
            brightness = int(json_data['bright'])
            self._connect.set_brightness(brightness)

        if 'rgb' in json_data:
            rgb = json_data['rgb']
            self._connect.set_rgb(rgb["red"], rgb["green"], rgb["blue"])

        if 'ct' in json_data:
            color_temp = int(json_data['ct'])
            self._connect.set_color_temp(color_temp)

    def on(self):
        def dead_lith():
            with open('src/utils/config_light.json', 'r') as file:
                json_data = json.load(file)
                self.set_config(json_data['dead'])

        def life_lith():
            with open('src/utils/config_light.json', 'r') as file:
                json_data = json.load(file)
                self.set_config(json_data['day'])

        if self._dead == 1:
            turn_on_thread = threading.Thread(target=dead_lith)
            turn_on_thread.start()

        elif self._dead == 0:
            turn_on_thread = threading.Thread(target=life_lith)
            turn_on_thread.start()

    def off(self):
        turn_off_thread = threading.Thread(target=self._connect.turn_off)
        turn_off_thread.start()

    def on_night(self):
        def dead_lith():
            with open('src/utils/config_light.json', 'r') as file:
                json_data = json.load(file)
                self.set_config(json_data['dead'])

        def life_lith():
            with open('src/utils/config_light.json', 'r') as file:
                json_data = json.load(file)
                self.set_config(json_data['night'])

        if self._dead == 1:
            turn_on_thread = threading.Thread(target=dead_lith)
            turn_on_thread.start()

        elif self._dead == 0:
            turn_on_thread = threading.Thread(target=life_lith)
            turn_on_thread.start()
