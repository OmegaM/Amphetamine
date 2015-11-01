#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/1 14:42 By OmegaMiao

    amphetamineUtils.py
"""

import json


def jsListToPythonDict(jsList):
    test_case = {}
    # jsonobj = json.dumps(jsList)
    for item in jsList:
        test_case[item[0]] = item[1]
    return test_case


def pythonObjectToJSON(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__, indent=2)

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
