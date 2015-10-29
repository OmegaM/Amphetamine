#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Created with Pycharm IDEA

@Create on 2015/10/28 0028 13:06

@Amphetamine testcase_model.py

@author : OmegaMiao"""

import common
from datetime import datetime
from .. import db
from teststep_model import TestStep


class TestCase(db.Model):
    __tablename__ = 'testcase'

    PlatForm = common.PlatForm

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    testCaseId = db.Column(db.String(30), nullable=False, unique=True)
    caseDescription = db.Column(db.String(255), nullable=False, unique=False)
    projectId = db.Column(db.String(30), nullable=False, unique=True)
    projectName = db.Column(db.String(30), nullable=False, unique=True)
    platform = db.Column(db.Enum(*PlatForm), nullable=False, default='WEB')
    runMode = db.Column(db.Boolean, default=None)
    testSet = db.Column(db.String(30), nullable=True, default=None)
    createTime = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    updateTime = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    teststeps = db.relationship('TestStep', backref='testcase', lazy='dynamic')

    def __repr__(self):
        return "<TestCase  %r %r %r %r>" % (self.id, self.testCaseId, self.caseDescription, self.platform)
