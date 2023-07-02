import threading
import time
import random

from yeelight import Bulb
from . import main


@main.route('/')
def hello_world():
    threading.Thread(target=execute_function_thread).start()
    return 'lamp on'


def execute_function_thread():
    bulb = Bulb("192.168.0.238")
    for x in range(10):
        bulb.turn_on(effect="sudden")
        time.sleep(random.random())
        bulb.turn_off()
        time.sleep(random.random())
