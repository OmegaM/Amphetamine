#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 21:00 By OmegaMiao

    mian_model.py
"""


import common
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from amphetamine_app import db, loginManager, logger


class Amphetamine(db.Model):

    __tablename__ = 'amphetamine'

    ActionType = common.ActionType
    ByElementType = common.ByElementType

    id = db.Column(db.Integer, primary_key=True)
    element_desc = db.Column(db.String(255), nullable=True, unique=False)
    element_key = db.Column(db.String(255), nullable=True, unique=False)
    element_value = db.Column(db.String(255), nullable=True, unique=False)
    by_element_type = db.Column(db.Enum(*ByElementType), nullable=False,default='XPATH')
    action = db.Column(db.Enum(*ActionType), nullable=False, default='READ')
    step = db.Column(db.Integer, nullable=True, unique=False)
    child = db.Column(db.Integer, nullable=True, unique=False)
    child_desc = db.Column(db.String(255), nullable=True, unique=False)
    parent = db.Column(db.Integer, nullable=True, unique=False)
    parent_desc = db.Column(db.String(255), nullable=True, unique=False)
    row = db.Column(db.Integer, nullable=True, unique=False)
    is_enable = db.Column(db.Boolean, default=True)
    is_passed = db.Column(db.Boolean, default=False)
    modify_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        return "<Amphetamine  %r %r %r %r>" % (self.id, self.element_desc, self.element_key, self.element_value)