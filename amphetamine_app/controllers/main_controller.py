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


@amphetamine_app.route('/')
@amphetamine_app.route('/index')
def index():
    form = EditTestCaseForm()
    amphetamine_list = db.session.query(Amphetamine).order_by(Amphetamine.parent, Amphetamine.id).all()
    logger.debug('amphetamine_list is : ' + str(amphetamine_list[0]))

    return render_template('index.html', form=form, amphetamine_list=amphetamine_list)


@amphetamine_app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    form = EditTestCaseForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            amphetamine = Amphetamine(page_key=form.page_key.data,
                                      page_value=form.page_value.data,
                                      element=form.element.data,
                                      child=form.child.data,
                                      child_desc=form.child_desc.data,
                                      parent=form.parent.data,
                                      parent_desc=form.parent_desc.data,
                                      branch=form.branch.data,
                                      action=form.action.data
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