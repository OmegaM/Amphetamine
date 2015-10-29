#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 21:49 By OmegaMiao

    testcase_form.py
"""

from flask_wtf import Form
from wtforms import SelectField, StringField, IntegerField
from wtforms.validators import DataRequired, Length


class EditTestCaseForm(Form):
    validRequiredMessage = u"该字段为必填项"
    validMaxLengthMessage = u"超过了255个字符"

    platform = SelectField(label='Platform',
                           choices=[('WEB', 'Web'), ('ANDROID', 'Android'), ('IOS', 'Ios')])

    testCaseId = StringField(label='TestCaseId',
                             validators=[DataRequired(message=validRequiredMessage),
                                         Length(min=1, max=30, message=validMaxLengthMessage)])

    caseDescription = StringField(label='CaseDescription',
                                  validators=[DataRequired(message=validRequiredMessage),
                                              Length(min=1, max=255, message=validMaxLengthMessage)])

    projectId = StringField(label='ProjectId',
                            validators=[DataRequired(message=validRequiredMessage),
                                        Length(min=1, max=30, message=validMaxLengthMessage)])

    projectName = StringField(label='ProjectName',
                              validators=[DataRequired(message=validRequiredMessage),
                                          Length(min=1, max=30, message=validMaxLengthMessage)])

    testSet = StringField(label='ProjectName',
                          validators=[DataRequired(message=validRequiredMessage),
                                      Length(min=1, max=30, message=validMaxLengthMessage)])
