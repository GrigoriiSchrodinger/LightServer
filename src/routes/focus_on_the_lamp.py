from flask import request, jsonify
from . import main
from ..lamps.lamps_manager import LampsControl
from ..storage.database import LampsManager


@main.route('/focus', methods=['POST'])
def focus_lamp():
    data = {'ip': request.form.get("ip")}
    bulb = LampsManager()
    info_lamps = bulb.get_lamps()

    for lamp in info_lamps:
        if lamp[0] != data["ip"]:
            bulb_control = LampsControl(lamp[0], lamp[3])
            bulb_control.off()

    for lamp in info_lamps:
        if lamp[0] == data["ip"]:
            bulb_control = LampsControl(data["ip"], lamp[3])
            bulb_control.on()

    return jsonify({'message': 'Success'}), 200
