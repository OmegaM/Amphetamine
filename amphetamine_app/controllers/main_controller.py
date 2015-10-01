#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 20:54 By OmegaMiao

    main_controller.py
"""

from amphetamine_app import amphetamine_app, logger, db
from amphetamine_app.forms.main_form import EditTestCaseForm
from amphetamine_app.models.mian_model import Amphetamine
from flask import jsonify, request, render_template, redirect, flash, url_for
from amphetamine_app.utils import amphetamineUtils


@amphetamine_app.route('/')
@amphetamine_app.route('/index')
def index():
    form = EditTestCaseForm()
    amphetamine_list = db.session.query(Amphetamine).order_by(Amphetamine.parent, Amphetamine.id).all()
    return render_template('index.html', form=form, amphetamine_list=amphetamine_list)


@amphetamine_app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    form = EditTestCaseForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            amphetamine = Amphetamine(element_desc=form.element_desc.data,
                                      element_key=form.element_key.data,
                                      element_value=form.element_value.data,
                                      by_element_type=form.by_element_type.data,
                                      action=form.action.data,
                                      step=form.step.data,
                                      child=form.child.data,
                                      child_desc=form.child_desc.data,
                                      parent=form.parent.data,
                                      parent_desc=form.parent_desc.data,
                                      row=form.row.data
                                      )
            db.session.add(amphetamine)
            db.session.commit()
            flash(u"添加成功")
            return redirect(url_for('index'))
        else:
            flash(u"添加失败")
            return render_template('index.html', form=form)
    else:
        return redirect(url_for('index'))


@amphetamine_app.route('/update_case_enable/<int:id>', methods=['GET'])
def update_case_enable(id):

    if request.method == 'GET':
        try:
            case = db.session.query(Amphetamine).get(id)
            case.is_enable = not case.is_enable
            db.session.commit()
            flash(u"修改成功")
            return redirect(url_for('index'))
        except Exception, e:
            logger.debug("update case failed : " + e.message)
            db.session.rollback()
    return redirect(url_for('index'))


@amphetamine_app.route('/update_test_case', methods=['POST'])
def update_test_case():
    if request.method == 'POST':
        testCaseDict = amphetamineUtils.jsListToPythonDict(request.form.items())
        try:
            testcase = db.session.query(Amphetamine).get(testCaseDict.get('id'))
            testcase.element_desc = testCaseDict.get('element_desc')
            testcase.element_key = testCaseDict.get('element_key')
            testcase.element_value = testCaseDict.get('element_value')
            testcase.step = testCaseDict.get('step')
            testcase.child = testCaseDict.get('child')
            testcase.child_desc = testCaseDict.get('child_desc')
            testcase.parent = testCaseDict.get('parent')
            testcase.parent_desc = testCaseDict.get('parent_desc')
            testcase.row = testCaseDict.get('row')
            db.session.commit()
            return jsonify(status='success', messages=u'用例更新成功')
        except Exception, e:
            logger.error("update testcase has error : " + e.message)
            db.session.rollback()
            return jsonify(status='fail', messages=u'用例更新失败')
    return redirect(url_for('index'))


@amphetamine_app.route('/delete_case/<int:id>', methods=['GET'])
def delete_case(id):

    if request.method == 'GET':
        try:
            case = db.session.query(Amphetamine).get(id)
            db.session.delete(case)
            db.session.commit()
            flash(u"删除成功")
            return redirect(url_for('index'))
        except Exception, e:
            logger.debug("delete case failed : " + e.message)
            db.session.rollback()
    return redirect(url_for('index'))
