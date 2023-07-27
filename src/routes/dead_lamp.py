from flask import request, jsonify
from . import main
from ..storage.database import LampsManager


@main.route('/dead', methods=['POST'])
def dead_lapm():
    data = {'ip': request.form.get("ip")}
    bulb = LampsManager()
    info_lamps = bulb.get_lamps()

    for lamp in info_lamps:
        if lamp[0] == data["ip"] and lamp[3] == 0:
            bulb.update_lamp_dead(ip=lamp[0], dead=1)

        elif lamp[0] == data["ip"] and lamp[3] == 1:
            bulb.update_lamp_dead(ip=lamp[0], dead=0)

    return jsonify({'message': 'Success'}), 200
