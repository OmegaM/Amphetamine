#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Created with Pycharm IDEA

@Create on 2015/10/28 0028 13:23

@Amphetamine edit_teststep_controller.py

@author : OmegaMiao"""

import datetime
from flask import jsonify, request, render_template, redirect, flash, url_for
from amphetamine_app.utils import amphetamineUtils
from ..forms.teststep_form import EditTestStepForm
from .. import amphetamine_app, logger, db
from ..models.testcase_model import TestCase
from ..models.teststep_model import TestStep


@amphetamine_app.route('/edit_teststep', methods=['GET'])
def edit_teststep():
    form = EditTestStepForm()
    try:
        teststepList = db.session.query(TestStep).order_by(TestStep.id).all()
        return render_template('teststep/edit_teststep.html', form=form, teststepList=teststepList)
    except Exception, e:
        logger.error("query all teststep list failed : " + e.message)
        return render_template('teststep/edit_teststep.html', form=form)


@amphetamine_app.route('/add_teststep', methods=['GET', 'POST'])
def add_teststep():
    form = EditTestStepForm(request.form)
    teststepList = db.session.query(TestStep).order_by(TestStep.id).all()
    if request.method == 'POST':
        if form.validate_on_submit():

            teststep = TestStep()

            form.populate_obj(teststep)
            teststep.testcaseId = form.testCaseId.data.testCaseId  # very importent
            try:
                db.session.add(teststep)
                db.session.commit()
                flash(u'步骤添加成功', 'success')
                return redirect(url_for('edit_teststep'))
            except Exception, e:
                logger.error("add teststep failed : " + e.message)
                db.session.rollback()
                flash(u'步骤添加失败', 'error')
                return redirect(url_for('edit_teststep'))
        else:
            flash(u'输入的表单含有错误项')
            return render_template('teststep/edit_teststep.html', form=form, teststepList=teststepList)
    return redirect(url_for('edit_teststep'))


@amphetamine_app.route('/delete_teststep/<int:id>', methods=['GET'])
def delete_teststep(id):
    if request.method == 'GET':
        try:
            teststep = db.session.query(TestStep).get(id)
            db.session.delete(teststep)
            db.session.commit()
            flash(u'删除步骤成功', 'success')
            return redirect(url_for('edit_teststep'))
        except Exception, e:
            logger.debug("delete teststep failed : " + e.message)
            db.session.rollback()
            flash(u'删除步骤失败', 'error')
            return redirect(url_for('edit_teststep'))
    return redirect(url_for('edit_teststep'))


@amphetamine_app.route('/update_teststep', methods=['POST'])
def update_teststep():
    if request.method == 'POST':
        # print request.form.items()
        testStepDict = amphetamineUtils.jsListToPythonDict(request.form.items())
        try:
            teststep = db.session.query(TestStep).get(testStepDict.get('id'))
            teststep.step = testStepDict.get('step')
            teststep.stepDescription = testStepDict.get('stepDescription')
            teststep.pageName = testStepDict.get('pageName')
            teststep.pageObjectName = testStepDict.get('pageObjectName')
            teststep.byType = testStepDict.get('byType')
            teststep.byExpression = testStepDict.get('byExpression')
            teststep.actionKeyword = testStepDict.get('actionKeyword')
            teststep.testData = testStepDict.get('testData')
            teststep.testExpectValue = testStepDict.get('testExpectValue')
            teststep.officalData = testStepDict.get('officalData')
            teststep.officalExpectValue = testStepDict.get('officalExpectValue')
            teststep.updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.commit()
            return jsonify(status='success', messages=u'步骤更新成功')
        except Exception, e:
            logger.error("modify teststep failed : " + e.message)
            db.session.rollback()
            return jsonify(status='fail', messages=u'步骤更新失败')
    return redirect(url_for('edit_teststep'))
