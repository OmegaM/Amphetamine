#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/11/1 17:36 By OmegaMiao

    show_teststep_controller.py
"""

from flask import jsonify, request, render_template, redirect, flash, url_for, abort
from .. import amphetamine_app, logger, db
from sqlalchemy.sql import and_
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep

PER_PAGE = 5


@amphetamine_app.route('/show_all_teststep', methods=['GET'])
def show_all_teststep():
    page = request.args.get('page', 1, type=int)
    try:
        pagination = TestStep.query.order_by(TestStep.id, TestStep.testcaseId). \
            paginate(page, PER_PAGE, error_out=False)
        teststeps = pagination.items
        # raise Exception("this is message, has been set an error message for my macbookpro")
        return render_template('teststep/show_teststep.html', teststeps=teststeps, pagination=pagination)
    except Exception, e:
        logger.error("pagination query failed : " + e.message)
        # 错误消息通过'error'传递给前端模板的category_filter=['error']
        flash("Error message : " + e.message, 'error')
        abort(500)


@amphetamine_app.route('/show_teststep_by_category/<string:category>')
def show_teststep_by_category(category):
    page = request.args.get('page', 1, type=int)
    print "====================sql===================="
    pagination = TestStep.query.filter(and_(TestCase.platform == category,
                                            TestStep.testcaseId == TestCase.testCaseId)). \
        order_by(TestStep.id, TestStep.testcaseId).paginate(page, PER_PAGE, error_out=False)
    teststeps = pagination.items
    # raise Exception("this is message, has been set an error message for my macbookpro")
    category_flag = category
    return render_template('teststep/show_teststep.html',
                           teststeps=teststeps,
                           pagination=pagination,
                           category_flag=category_flag)
