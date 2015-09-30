#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 21:00 By OmegaMiao

    mian_model.py
"""


import common
from amphetamine_app import db, loginManager, logger
from datetime import datetime
# import signature package
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class Amphetamine(db.Model):

    __tablename__ = 'amphetamine'

    ActionType = common.ActionType

    id = db.Column(db.Integer, primary_key=True)
    page_key = db.Column(db.String(255), nullable=True, unique=False)
    page_value = db.Column(db.String(255), nullable=True, unique=False)
    element = db.Column(db.String(255), nullable=True, unique=False)
    child = db.Column(db.Integer, nullable=True, unique=False)
    child_desc = db.Column(db.String(255), nullable=True, unique=False)
    parent = db.Column(db.Integer, nullable=True, unique=False)
    parent_desc = db.Column(db.String(255), nullable=True, unique=False)
    branch = db.Column(db.Integer, nullable=True, unique=False)
    action = db.Column(db.Enum(*ActionType), nullable=False, default='READ')
    is_enable = db.Column(db.Boolean, default=True)
    is_passed = db.Column(db.Boolean, default=False)
    modify_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        return "<Amphetamine  %r %r %r %r>" % (self.id, self.page_key, self.page_value, self.element)