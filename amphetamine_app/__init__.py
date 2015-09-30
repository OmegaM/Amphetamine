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


loginManager = LoginManager()

amphetamine_app = Flask(__name__)
amphetamine_app.config.from_object(config['dev'])
db = SQLAlchemy(amphetamine_app)
loginManager.init_app(amphetamine_app)

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logger = amphetamine_app.logger
logger.addHandler(console)
logger.setLevel(logging.DEBUG)

# mail
mail = Mail(amphetamine_app)

from controllers.main_controller import amphetamine_app
from models.mian_model import Amphetamine
