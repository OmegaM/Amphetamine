#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Created with Pycharm IDEA

@Create on 2015/10/28 0028 13:23

@Amphetamine edit_testcase_controller.py

@author : OmegaMiao"""

import datetime
from flask import jsonify, request, render_template, redirect, flash, url_for
from amphetamine_app.utils import amphetamineUtils
from .. import amphetamine_app, logger, db
from ..forms.testcase_form import EditTestCaseForm
from ..models.testcase_model import TestCase


@amphetamine_app.route('/edit_testcase', methods=['GET'])
def edit_testcase():
    form = EditTestCaseForm()
    try:
        testcaseList = db.session.query(TestCase).order_by(TestCase.id).all()
        return render_template('testcase/edit_testcase.html', form=form, testcaseList=testcaseList)
    except Exception, e:
        logger.error("query all testcase list failed : " + e.message)
        return render_template('testcase/edit_testcase.html', form=form)


@amphetamine_app.route('/add_testcase', methods=['GET', 'POST'])
def add_testcase():
    form = EditTestCaseForm(request.form)
    testcaseList = db.session.query(TestCase).order_by(TestCase.id).all()
    if request.method == 'POST':
        if form.validate_on_submit():

            testcase = TestCase()
            form.populate_obj(testcase)  # 使用form的数据直接写入amphetamine对象
            try:
                db.session.add(testcase)
                db.session.commit()
                flash(u'用例添加成功', 'success')
                return redirect(url_for('edit_testcase'))
            except Exception, e:
                logger.error("add testcase failed : " + e.message)
                db.session.rollback()
                flash(u'用例添加失败', 'error')
                return redirect(url_for('edit_testcase'))
        else:
            flash(u'输入的表单含有错误项')
            return render_template('testcase/edit_testcase.html', form=form, testcaseList=testcaseList)
    return redirect(url_for('edit_testcase'))


@amphetamine_app.route('/delete_testcase/<int:id>', methods=['GET'])
def delete_testcase(id):
    if request.method == 'GET':
        try:
            testcase = db.session.query(TestCase).get(id)
            db.session.delete(testcase)
            db.session.commit()
            flash(u'删除用例成功', 'success')
            return redirect(url_for('edit_testcase'))
        except Exception, e:
            logger.debug("delete testcase failed : " + e.message)
            db.session.rollback()
            flash(u'删除用例失败', 'error')
            return redirect(url_for('edit_testcase'))
    return redirect(url_for('edit_testcase'))


@amphetamine_app.route('/update_testcase', methods=['POST'])
def update_testcase():
    if request.method == 'POST':
        # print request.form.items()
        testCaseDict = amphetamineUtils.jsListToPythonDict(request.form.items())
        try:
            testcase = db.session.query(TestCase).get(testCaseDict.get('id'))
            testcase.projectId = testCaseDict.get('projectId')
            testcase.projectName = testCaseDict.get('projectName')
            testcase.testCaseId = testCaseDict.get('testCaseId')
            testcase.caseDescription = testCaseDict.get('caseDescription')
            testcase.testSet = testCaseDict.get('testSet')
            testcase.updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.commit()
            return jsonify(status='success', messages=u'用例更新成功')
        except Exception, e:
            logger.error("modify testcase failed : " + e.message)
            db.session.rollback()
            return jsonify(status='fail', messages=u'用例更新失败')
    return redirect(url_for('edit_testcase'))
