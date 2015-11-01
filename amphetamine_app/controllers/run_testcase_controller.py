#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/11/1 14:53 By OmegaMiao

    run_testcase_controller.py
"""

import datetime
import json
from flask import jsonify, request, make_response
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep


@amphetamine_app.route('/run_testcase', methods=['POST'])
def run_testcase():
    if request.method == 'POST':
        platformSet = set()
        projectSet = set()
        prerun_testcase_list = request.get_json().get('runTestCaseArray')
        print prerun_testcase_list
        run_testcase_list = db.session.query(TestCase.platform, TestCase.projectId). \
            filter(TestCase.testCaseId.in_(prerun_testcase_list)).all()
        for items in run_testcase_list:
            platformSet.add(items[0])
            projectSet.add(items[1])
        # print platformSet.pop()
        # print projectSet.pop()

        mydict = {"platform": platformSet.pop(),
                  "projectId": projectSet.pop(),
                  "testSet": "",
                  "systemTime": datetime.datetime.now().strftime('%Y-%m-%d'),
                  "testcase": prerun_testcase_list}
        print mydict
        print json.dumps(mydict, indent=2)

        return jsonify({"success": True})
