from flask import request, jsonify
from . import main
from ..lamps.lamps_manager import LampsControl
from ..storage.database import LampsManager


@main.route('/focus', methods=['POST'])
def focus_lamp():
    data = {'ip': request.form.get("ip")}
    bulb = LampsManager()

    for info_lamp in bulb.get_lamps():
        bulb_control = LampsControl(info_lamp[0])
        if info_lamp[0] == data["ip"]:
            bulb_control.on()
        else:
            bulb_control.off()

    return jsonify({'message': 'Success'}), 200
