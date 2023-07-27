from flask import Blueprint

main = Blueprint('main', __name__)

from src.routes import add_lamp
from src.routes import get_lamps
from src.routes import focus_on_the_lamp
from src.routes import control_all_lamps
from src.routes import dead_lamp
from src.routes import night_lamp
