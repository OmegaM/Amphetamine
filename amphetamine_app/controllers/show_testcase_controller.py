#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/2 11:56 By OmegaMiao

    show_testcase_controller.py
"""


from amphetamine_app import amphetamine_app, logger, db
from amphetamine_app.models.mian_model import Amphetamine
from flask import jsonify, request, render_template, redirect, flash, url_for, abort

PER_PAGE = 10


@amphetamine_app.route('/show_testcases', methods=['GET'])
def show_testcases():
    page = request.args.get('page', 1, type=int)
    try:
        pagination = Amphetamine.query.order_by(Amphetamine.id, Amphetamine.parent). \
            paginate(page, PER_PAGE, error_out=False)
        testcases = pagination.items
        # raise Exception("this is message, has been set an error message for my macbookpro")
        return render_template('show_testcases.html', testcases=testcases, pagination=pagination)
    except Exception, e:
        logger.error("pagination query failed : " + e.message)
        # 错误消息通过'error'传递给前端模板的category_filter=['error']
        flash("Error message : " + e.message, 'error');
        abort(500)
