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

    element_desc = StringField(label='ElementDesc',
                           validators=[DataRequired(message=validRequiredMessage),
                                       Length(min=1, max=255, message=validMaxLengthMessage)])

    element_key = StringField(label='ElementKey',
                              validators=[DataRequired(message=validRequiredMessage),
                                       Length(min=1, max=255, message=validMaxLengthMessage)])

    element_value = StringField(label='ElementValue',
                             validators=[DataRequired(message=validRequiredMessage),
                                         Length(min=1, max=255, message=validMaxLengthMessage)])

    by_element_type = SelectField(label='ByElementType',
                                  choices=[('XPATH', 'xpath'), ('ID', 'id'), ('NAME', 'name')])

    action = SelectField(label='Action',
                         choices=[('READ', 'read'), ('INPUT', 'input'), ('CLICK', 'click')])

    step = IntegerField(label='Step',
                        validators=[DataRequired(message=validRequiredMessage)])

    child = SelectField(label='Child',
                        choices=map(lambda x: (x, 'C'+str(x)), [x for x in range(10)]), coerce=int)

    child_desc = StringField(label='ChildDesc',
                             validators=[DataRequired(message=validRequiredMessage),
                                         Length(min=1, max=255, message=validMaxLengthMessage)])
    parent = SelectField(label='Parent',
                         choices=[(x, 'P'+str(x)) for x in range(10)], coerce=int)
    parent_desc = StringField(label='ParentDesc',
                              validators=[DataRequired(message=validRequiredMessage),
                                          Length(min=1, max=255, message=validMaxLengthMessage)])
    row = IntegerField(label='Row',
                       validators=[DataRequired(message=validRequiredMessage)])




