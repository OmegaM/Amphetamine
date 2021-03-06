#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 20:54 By OmegaMiao

    main_controller.py
"""

from flask import jsonify, request, render_template, redirect, flash, url_for

from .. import amphetamine_app, logger, db
from ..forms.main_form import EditTestCaseForm
from ..models.mian_model import Amphetamine
from ..utils import amphetamineUtils


@amphetamine_app.route('/edit_testcase')
def edit_testcase():
    form = EditTestCaseForm()
    try:
        amphetamine_list = db.session.query(Amphetamine).order_by(Amphetamine.parent, Amphetamine.id).all()
        return render_template('edit_testcase.html', form=form, amphetamine_list=amphetamine_list)
    except Exception, e:
        logger.error("query all testcase list failed : " + e.message)
        return render_template('edit_testcase.html', form=form)


@amphetamine_app.route('/add_testcase', methods=['GET', 'POST'])
def add_testcase():
    form = EditTestCaseForm(request.form)
    amphetamine_list = db.session.query(Amphetamine).order_by(Amphetamine.parent, Amphetamine.id).all()
    if request.method == 'POST':
        if form.validate_on_submit():
            # amphetamine = Amphetamine(element_desc=form.element_desc.data,
            #                           element_key=form.element_key.data,
            #                           element_value=form.element_value.data,
            #                           by_element_type=form.by_element_type.data,
            #                           action=form.action.data,
            #                           step=form.step.data,
            #                           child=form.child.data,
            #                           child_desc=form.child_desc.data,
            #                           parent=form.parent.data,
            #                           parent_desc=form.parent_desc.data,
            #                           row=form.row.data
            #
            amphetamine = Amphetamine()
            form.populate_obj(amphetamine)  # 使用form的数据直接写入amphetamine对象
            try:
                db.session.add(amphetamine)
                db.session.commit()
                flash(u'用例添加成功', 'success')
                return redirect(url_for('edit_testcase')), 201
            except Exception, e:
                logger.error("add testcase failed : " + e.message)
                db.session.rollback();
                flash(u'用例添加失败', 'error')
                return redirect(url_for('edit_testcase'))
        else:
            flash(u'输入的表单含有错误项')
            return render_template('edit_testcase.html', form=form, amphetamine_list=amphetamine_list)
    return redirect(url_for('edit_testcase'))


@amphetamine_app.route('/update_case_enable/<int:id>', methods=['GET'])
def update_case_enable(id):
    if request.method == 'GET':
        try:
            case = db.session.query(Amphetamine).get(id)
            case.is_enable = not case.is_enable
            db.session.commit()
            flash(u'用例状态修改成功', 'success')
            return redirect(url_for('edit_testcase'))
        except Exception, e:
            logger.error("update testcase status failed : " + e.message)
            db.session.rollback()
            flash(u'用例状态修改失败', 'error')
            return redirect(url_for('edit_testcase'))
    return redirect(url_for('edit_testcase'))


@amphetamine_app.route('/update_testcase', methods=['POST'])
def update_testcase():
    if request.method == 'POST':
        # print request.form.items()
        testCaseDict = amphetamineUtils.jsListToPythonDict(request.form.items())
        try:
            testcase = db.session.query(Amphetamine).get(testCaseDict.get('id'))
            if testcase.element_desc != testCaseDict.get('element_desc'):
                testcase.element_desc = testCaseDict.get('element_desc')
            if testcase.element_key != testCaseDict.get('element_key'):
                testcase.element_key = testCaseDict.get('element_key')
            if testcase.element_value != testCaseDict.get('element_value'):
                testcase.element_value = testCaseDict.get('element_value')
            if testcase.step != testCaseDict.get('step'):
                testcase.step = testCaseDict.get('step')
            if testcase.child != testCaseDict.get('child'):
                testcase.child = testCaseDict.get('child')
            if testcase.child_desc != testCaseDict.get('child_desc'):
                testcase.child_desc = testCaseDict.get('child_desc')
            if testcase.parent != testCaseDict.get('parent'):
                testcase.parent = testCaseDict.get('parent')
            if testcase.parent_desc != testCaseDict.get('parent_desc'):
                testcase.parent_desc = testCaseDict.get('parent_desc')
            if testcase.row != testCaseDict.get('row'):
                testcase.row = testCaseDict.get('row')
            # db.session.add(amphetamineUtils.updateChangeField(testcase, testCaseDict))
            # testcase = amphetamineUtils.updateChangeField(testcase, testCaseDict)
            db.session.commit()
            return jsonify(status='success', messages=u'用例更新成功')
        except Exception, e:
            logger.error("modify testcase failed : " + e.message)
            db.session.rollback()
            return jsonify(status='fail', messages=u'用例更新失败')
    return redirect(url_for('edit_testcase'))


@amphetamine_app.route('/delete_case/<int:id>', methods=['GET'])
def delete_testcase(id):
    if request.method == 'GET':
        try:
            case = db.session.query(Amphetamine).get(id)
            db.session.delete(case)
            db.session.commit()
            flash(u'删除用例成功', 'success')
            return redirect(url_for('edit_testcase'))
        except Exception, e:
            logger.debug("delete testcase failed : " + e.message)
            db.session.rollback()
            lash(u'删除用例失败', 'error')
            return redirect(url_for('edit_testcase'))
    return redirect(url_for('edit_testcase'))
