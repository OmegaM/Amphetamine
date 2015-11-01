#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/11/1 14:53 By OmegaMiao

    run_testcase_controller.py
"""

from flask import jsonify, request, make_response
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep


@amphetamine_app.route('/run_testcase', methods=['POST'])
def run_testcase():
    if request.method == 'POST':

        run_dict_child = {}
        run_dict = {"testCases": run_dict_child}
        platformSet = set()
        projectSet = set()
        prerun_testcase_list = request.get_json().get('runTestCaseArray')
        print prerun_testcase_list
        run_testcase_list = db.session.query(TestCase.platform, TestCase.projectId). \
            filter(TestCase.testCaseId.in_(prerun_testcase_list)).all()
        for items in run_testcase_list:
            platformSet.add(items[0])
        print platformSet.pop()

        run_project_testcase_list = db.session.query(TestCase.projectId, TestCase.testCaseId). \
            filter(TestCase.testCaseId.in_(prerun_testcase_list)).all()
        print run_project_testcase_list
        for items in run_project_testcase_list:
            print items
            projectSet.add(items[0])
        print projectSet
        for key in projectSet:
            run_dict_child[key] = ''
        print run_dict_child

        return jsonify({"success": True})
