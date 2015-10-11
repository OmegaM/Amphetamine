#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/1 14:42 By OmegaMiao

    amphetamineUtils.py
"""

from flask.ext.assets import Bundle, Environment
from .. import amphetamine_app

bundles = {
    'bootstrap_js': Bundle(
        'js/jquery.js',
        'js/jquery.json.min.js',
        'js/nmp.js',
        'js/bootstrap.min.js',
        'js/bootstrapValidator.min.js'

    ),
    'feature_js': Bundle(
        'js/ampValidation.js',
        'js/updateTestCase.js'
    ),
    'bootstrap_css': Bundle(
        'css/bootstrap.min.css',
        'css/bootstrap-theme.css',
        'css/bootstrapValidator.min.css',
        'css/main.css'
    )
}

assets = Environment(amphetamine_app)
assets.register(bundles)


def jsListToPythonDict(jsList):
    test_case = {}
    # jsonobj = json.dumps(jsList)
    for item in jsList:
        test_case[item[0]] = item[1]
    return test_case

# def updateChangeField(object1, object2Dict):
#     for key1 in object1.__dict__.keys():
#         if key1 != '_sa_instance_state':
#             for key2 in object2Dict.keys():
#                 if key1 != key2:
#                     continue
#                 else:
#                     if object1.__getattr__(key1) != object2Dict[key2]:
#                         object1.__setattr__(key1, object2Dict[key2])
#     print object1.parent_desc
#     return object1
