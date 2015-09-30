#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Flask Amphetamine.app

    Create on 15/9/29 20:44 By OmegaMiao

    runserver.py.py
"""


from amphetamine_app import amphetamine_app


if __name__ == '__main__':
    amphetamine_app.run(debug=True, port=5000)
