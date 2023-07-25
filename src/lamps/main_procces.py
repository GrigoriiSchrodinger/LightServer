import time
import random

from yeelight import Bulb


def execute_function_thread():
    bulb = Bulb("192.168.0.238")
    for x in range(1):
        bulb.turn_on(effect="sudden")
        time.sleep(random.random())
        bulb.turn_off()
        time.sleep(random.random())
