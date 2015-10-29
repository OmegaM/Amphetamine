#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Created with Pycharm IDEA

@Create on 2015/10/28 0028 13:03

@Amphetamine teststep_form.py

@author : OmegaMiao"""

from flask_wtf import Form
from ..models.testcase_model import TestCase
from wtforms import SelectField, StringField, IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class EditTestStepForm(Form):
    validRequiredMessage = u"该字段为必填项"
    validMaxLengthMessage = u"超过了字符限制"

    testCaseId = QuerySelectField(label='TestCaseId',
                                  query_factory=TestCase.query.all,
                                  get_pk=lambda a: a.id, get_label=lambda a: a.testCaseId)

    step = IntegerField(label='Step',
                        validators=[DataRequired(message=validRequiredMessage)])

    stepDescription = StringField(label='Description ',
                                  validators=[DataRequired(message=validRequiredMessage),
                                              Length(min=1, max=255, message=validMaxLengthMessage)])

    pageName = StringField(label='PageName',
                           validators=[DataRequired(message=validRequiredMessage),
                                       Length(min=1, max=30, message=validMaxLengthMessage)])

    byType = SelectField(label='ByType', choices=[('XPATH', 'XPATH'), ('ID', 'ID')])

    byExpression = StringField(label='Expression',
                               validators=[DataRequired(message=validRequiredMessage),
                                           Length(min=1, max=255, message=validMaxLengthMessage)])

    pageObjectName = StringField(label='PageObjectName ',
                                 validators=[DataRequired(message=validRequiredMessage),
                                             Length(min=1, max=30, message=validMaxLengthMessage)])

    actionKeyword = SelectField(label='Action',
                                choices=[('CLICK', 'CLICK'), ('INPUT', 'INPUT'), ('NAVIGATE', 'NAVIGATE')])

    testData = StringField(label='TestData ',
                           validators=[DataRequired(message=validRequiredMessage),
                                       Length(min=1, max=30, message=validMaxLengthMessage)])

    testExpectValue = StringField(label='TestExpectValue ',
                                  validators=[DataRequired(message=validRequiredMessage),
                                              Length(min=1, max=30, message=validMaxLengthMessage)])

    officalData = StringField(label='OfficalData ',
                              validators=[DataRequired(message=validRequiredMessage),
                                          Length(min=1, max=30, message=validMaxLengthMessage)])

    officalExpectValue = StringField(label='OfficalExpectValue  ',
                                     validators=[DataRequired(message=validRequiredMessage),
                                                 Length(min=1, max=30, message=validMaxLengthMessage)])
