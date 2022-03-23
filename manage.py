from app import create_app
from flask_script import Manager
from config import config

config_class = config['development']
app = create_app(config_class)
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
