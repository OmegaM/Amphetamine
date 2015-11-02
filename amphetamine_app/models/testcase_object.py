#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/11/1 15:29 By OmegaMiao

    testcase_object.py
"""


class TestCaseClass(object):
    def __init__(self, testcase_list, platform, projectId, systemTime, env, testSet=""):
        self.testcases = testcase_list
        self.platform = platform
        self.projectId = projectId
        self.testSet = testSet
        self.systemTime = systemTime
        self.env = env


class TestCaseObject(object):
    def __init__(self, testcaseId):
        self.testcaseId = testcaseId
