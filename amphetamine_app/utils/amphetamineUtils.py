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
    jsonobj = json.dumps(jsList)
    for item in json.loads(jsonobj):
        test_case[item[0]] = item[1]
    return test_case