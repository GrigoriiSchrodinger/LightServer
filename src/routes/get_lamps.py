from . import main
from ..storage.database import LampsManager


@main.route('/lamps', methods=['GET'])
def get_lamps():
    bulb = LampsManager()
    return bulb.get_lamps()
