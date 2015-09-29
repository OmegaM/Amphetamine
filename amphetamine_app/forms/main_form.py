#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 21:49 By OmegaMiao

    main_form.py
"""


from flask_wtf import Form
from wtforms import SelectField, StringField, IntegerField
from wtforms.validators import DataRequired, Length


class EditTestCaseForm(Form):

    validRequiredMessage = u"该字段为必填项"
    validMaxLengthMessage = u"超过了255个字符"

    page_key = StringField(label='PageKey',
                           validators=[DataRequired(message=validRequiredMessage),
                                       Length(min=1, max=255, message=validMaxLengthMessage)])
    page_value = StringField(label='PageValue',
                             validators=[DataRequired(message=validRequiredMessage),
                                         Length(min=1, max=255, message=validMaxLengthMessage)])
    element = StringField(label='Element',
                          validators=[DataRequired(message=validRequiredMessage),
                                      Length(min=1, max=255, message=validMaxLengthMessage)])
    child = SelectField(label='Child', choices=[(x, 'C'+str(x)) for x in range(10)], coerce=int)
    child_desc = StringField(label='ChildDesc',
                             validators=[DataRequired(message=validRequiredMessage),
                                         Length(min=1, max=255, message=validMaxLengthMessage)])
    parent = SelectField(label='Parent', choices=[(x, 'P'+str(x)) for x in range(10)], coerce=int)
    parent_desc = StringField(label='ParentDesc',
                              validators=[DataRequired(message=validRequiredMessage),
                                          Length(min=1, max=255, message=validMaxLengthMessage)])
    branch = IntegerField(label='Branch',
                               validators=[DataRequired(message=validRequiredMessage)])

    action = SelectField(label='Action', choices=[('READ', 'read')])


