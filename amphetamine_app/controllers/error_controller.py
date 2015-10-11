#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/11 13:56 By OmegaMiao

    error_controller.py
"""

from flask import render_template, flash
from .. import amphetamine_app


@amphetamine_app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')


@amphetamine_app.errorhandler(500)
def not_found(error):
    flash(error)
    return render_template('errors/500.html')
