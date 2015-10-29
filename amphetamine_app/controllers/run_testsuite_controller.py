#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/16 21:24 By OmegaMiao

    run_testsuite_controller.py
"""


from flask import jsonify, request, make_response
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep as Amp


@amphetamine_app.route('/run_testsuite', methods=['POST'])
def run_testsuite():
    if request.method == 'POST':
        test_suite_mapping_dict = {}
        test_suite_dict = request.get_json().get('testSuite')
        print test_suite_dict['parentArrays']
        print test_suite_dict['childArrays']
        print zip(test_suite_dict['parentArrays'], test_suite_dict['childArrays'])
        test_suite_mapping_dict['mappingList'] = zip(test_suite_dict['parentArrays'], test_suite_dict['childArrays'])
        print test_suite_mapping_dict
        return jsonify({"message": "success"})
