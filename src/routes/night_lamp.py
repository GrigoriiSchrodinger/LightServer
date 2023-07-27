from flask import request, jsonify
from . import main
from ..lamps.lamps_manager import LampsControl
from ..storage.database import LampsManager


@main.route('/night', methods=['get'])
def night_lamp():
    bulb = LampsManager()
    info_lamps = bulb.get_lamps()

    for lamp in info_lamps:
        bulb_control = LampsControl(lamp[0], lamp[3])
        bulb_control.on_night()

    return jsonify({'message': 'Success'}), 200
