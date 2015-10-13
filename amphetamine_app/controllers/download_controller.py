#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/13 21:21 By OmegaMiao

    download_controller.py
"""


from flask import jsonify, request
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.mian_model import Amphetamine as Amp


@amphetamine_app.route('/export_testsuite_xls', methods=['GET'])
def export_testsuite_xls():
    if request.method == 'GET':
        parent = request.args.get('parent')
        child = request.args.get('child')
        try:
            testsuite_list = db.session.query(
                Amp.element_desc, Amp.parent_desc, Amp.child_desc, Amp.step, Amp.element_value).\
                filter(and_(Amp.parent == parent, Amp.child == child)).order_by(Amp.step).all()
            testsuite_dict = {}
            for index, item in enumerate(testsuite_list):
                testsuite_dict[index] = item.element_desc
            return jsonify({"testSuites": testsuite_dict})
        except Exception, e:
            return jsonify({"errorMessage": e.message})
