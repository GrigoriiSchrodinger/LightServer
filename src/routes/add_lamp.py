from flask import request, abort, jsonify
from . import main
from ..lamps.lamps_manager import LampsControl
from ..storage.database import LampsManager


@main.route('/', methods=['POST'])
def add_lamp():
    data = {'ip': request.form.get("ip"), 'name': request.form.get("name")}

    bulb = LampsControl(data["ip"])
    if bulb.check():
        lamps_manager = LampsManager()
        lamps_manager.add_lamp(ip=data["ip"], name=data["name"], status=bulb.get_status())
        return jsonify({'message': 'Success'}), 200
    else:
        abort(400, "IP fail")

