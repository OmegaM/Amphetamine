#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/11 16:04 By OmegaMiao

    index_controller.py
"""

from flask import render_template
from .. import amphetamine_app


@amphetamine_app.route('/')
@amphetamine_app.route('/index')
def index():
    return render_template('index.html')


@amphetamine_app.route('/tree_demo')
def tree_demo():
    return render_template('tree_demo.html')
