#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 20:45 By OmegaMiao

    __init__.py.py
"""


import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config
from flask.ext.mail import Mail
from flask_debugtoolbar import DebugToolbarExtension


loginManager = LoginManager()

amphetamine_app = Flask(__name__)
amphetamine_app.config.from_object(config['dev'])
db = SQLAlchemy(amphetamine_app)
loginManager.init_app(amphetamine_app)

# init logger with console
console = logging.StreamHandler()

# add file handler, only used for my mac...
file_handler = logging.FileHandler(config['my_mac_abs_dir'])

formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

console.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger = amphetamine_app.logger

logger.addHandler(console)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

# init mail
mail = Mail(amphetamine_app)
# init debug toolbar
toolbar = DebugToolbarExtension(amphetamine_app)

from controllers.index_controller import amphetamine_app
from controllers.main_controller import amphetamine_app
from controllers.show_testcase_controller import amphetamine_app
from controllers.error_controller import amphetamine_app
from controllers.download_controller import amphetamine_app

from .utils.amphetamineUtils import assets
from models.mian_model import Amphetamine
