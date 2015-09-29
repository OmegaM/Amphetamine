#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 20:52 By OmegaMiao

    config.py
"""


class Config(object):
    SQLALCHEMY_ECHO = False
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    def __init__(self):
        pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/amphetamine'


class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/amphetamine'


config = {
    'dev': DevConfig,
    'test': TestConfig
}