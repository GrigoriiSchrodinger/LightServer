from flask import Flask

from src.routes import main

app = Flask(__name__)
app.register_blueprint(main)


if __name__ == '__main__':
    app.run(port=9000, host='0.0.0.0')

from src.lamps.lamps_manager import LampsControl

f = LampsControl("192.168.238", 0)

print(f.get_status())