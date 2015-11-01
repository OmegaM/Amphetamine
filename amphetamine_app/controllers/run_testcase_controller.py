#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/11/1 14:53 By OmegaMiao

    run_testcase_controller.py
"""

import datetime
import json
import requests
from flask import jsonify, request, make_response
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep
from ..models.testcase_object import TestCaseClass
from amphetamine_app.utils.amphetamineUtils import pythonObjectToJSON


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


        run_testcase_json = pythonObjectToJSON(TestCaseClass(platform=platformSet.pop(),
                                                             projectId=projectSet.pop(),
                                                             systemTime=datetime.datetime.now().strftime('%Y-%m-%d'),
                                                             testcase_list=prerun_testcase_list))

        # run_testcase_dict = {"platform": platformSet.pop(),
        #           "projectId": projectSet.pop(),
        #           "testSet": "",
        #           "systemTime": datetime.datetime.now().strftime('%Y-%m-%d'),
        #           "testcase": prerun_testcase_list}
        # print run_testcase_dict
        print run_testcase_json
        headers = {'content-type': 'application/json;charset=UTF-8'}
        r = requests.post('http://127.0.0.1:5000/invoke', data=run_testcase_json, headers=headers)
        print r.text
        return jsonify({"success": True})


@amphetamine_app.route('/invoke', methods=['POST'])
def invoke():
    print request.get_json()
    return jsonify({"success": True})
