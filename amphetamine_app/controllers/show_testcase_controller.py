#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/2 11:56 By OmegaMiao

    show_testcase_controller.py
"""

from flask import jsonify, request, render_template, redirect, flash, url_for, abort
from .. import amphetamine_app, logger, db
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep

PER_PAGE = 25


@amphetamine_app.route('/show_all_testcase', methods=['GET'])
def show_all_testcase():
    page = request.args.get('page', 1, type=int)
    try:
        pagination = TestCase.query.order_by(TestCase.id, TestCase.testCaseId). \
            paginate(page, PER_PAGE, error_out=False)
        testcases = pagination.items
        # raise Exception("this is message, has been set an error message for my macbookpro")
        return render_template('testcase/show_testcase.html', testcases=testcases, pagination=pagination)
    except Exception, e:
        logger.error("pagination query failed : " + e.message)
        # 错误消息通过'error'传递给前端模板的category_filter=['error']
        flash("Error message : " + e.message, 'error')
        abort(500)


@amphetamine_app.route('/show_testcase_by_category/<string:category>')
def show_testcase_by_category(category):
    page = request.args.get('page', 1, type=int)
    pagination = TestCase.query.filter(TestCase.platform == category). \
        order_by(TestCase.id, TestCase.testCaseId).paginate(page, PER_PAGE, error_out=False)
    testcases = pagination.items
    # raise Exception("this is message, has been set an error message for my macbookpro")
    category_flag = category
    return render_template('testcase/show_testcase.html',
                           testcases=testcases,
                           pagination=pagination,
                           category_flag=category_flag)
