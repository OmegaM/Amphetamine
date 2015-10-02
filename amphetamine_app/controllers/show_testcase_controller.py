#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/2 11:56 By OmegaMiao

    show_testcase_controller.py
"""


from amphetamine_app import amphetamine_app, logger, db
from amphetamine_app.models.mian_model import Amphetamine
from flask import jsonify, request, render_template, redirect, flash, url_for
PER_PAGE = 5


@amphetamine_app.route('/show_testcases', methods=['GET'])
def show_testcases():
    page = request.args.get('page', 1, type=int)
    pagination = Amphetamine.query.order_by(Amphetamine.id, Amphetamine.parent).\
        paginate(page, PER_PAGE, error_out=False)
    testcases = pagination.items
    return render_template('show_testcases.html', testcases=testcases, pagination=pagination)