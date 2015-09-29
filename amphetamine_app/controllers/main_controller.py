#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 20:54 By OmegaMiao

    main_controller.py
"""



from amphetamine_app import amphetamine_app, logger, db
from amphetamine_app.forms.main_form import EditTestCaseForm
from flask import jsonify, request, render_template, redirect, flash, url_for


@amphetamine_app.route('/')
@amphetamine_app.route('/index')
def index():
    form = EditTestCaseForm()
    return render_template('index.html', form=form)


@amphetamine_app.route('/add_case')
def add_case():
    pass
