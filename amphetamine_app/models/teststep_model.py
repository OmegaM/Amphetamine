#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Created with Pycharm IDEA

@Create on 2015/10/28 0028 13:06

@Amphetamine teststep_model.py

@author : OmegaMiao"""

import common
from datetime import datetime
from .. import db


class TestStep(db.Model):
    __tablename__ = 'teststep'

    id = db.Column(db.Integer, primary_key=True)
    testcaseId = db.Column(db.String, db.ForeignKey('testcase.testCaseId'))
    step = db.Column(db.Integer, nullable=False, unique=False)
    stepDescription = db.Column(db.String(255), nullable=True, unique=False)
    pageName = db.Column(db.String(30), nullable=False)
    byType = db.Column(db.String(30), nullable=False)
    byExpression = db.Column(db.String(255))
    pageObjectName = db.Column(db.String(30), nullable=True, default=None)
    actionKeyword = db.Column(db.String(30), nullable=False)
    testData = db.Column(db.String(255), nullable=True)
    testExpectValue = db.Column(db.String(255), nullable=True)
    officalData = db.Column(db.String(255), nullable=True)
    officalExpectValue = db.Column(db.String(255), nullable=True)
    parentId = db.Column(db.Integer, nullable=True, unique=False, default=None)
    parentDesc = db.Column(db.String(30), nullable=True, unique=False, default=None)
    childId = db.Column(db.Integer, nullable=True, unique=False, default=None)
    childDesc = db.Column(db.String(30), nullable=True, unique=False, default=None)
    dataRow = db.Column(db.Integer, nullable=True, unique=False, default=None)
    createTime = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    updateTime = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        return "<TestStep  %r %r %r>" % (self.id, self.testCaseId, self.stepDescription)
