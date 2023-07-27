from flask import request, jsonify
from . import main
from ..lamps.lamps_manager import LampsControl
from ..storage.database import LampsManager


@main.route('/all', methods=['POST'])
def control_all():
    data = {'action': request.form.get("action")}
    bulb = LampsManager()
    info_lamps = bulb.get_lamps()

    if data["action"] == "off":
        for lamp in info_lamps:
            bulb_control = LampsControl(lamp[0], lamp[3])
            bulb_control.off()

    elif data["action"] == "on":
        for lamp in info_lamps:
            bulb_control = LampsControl(lamp[0], lamp[3])
            bulb_control.on()

    return jsonify({'message': 'Success'}), 200
