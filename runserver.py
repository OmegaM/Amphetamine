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
    # for x in range(10):
    #     print (x, 'child'+str(x))
    # # fs = [(lambda n: i + n) for i in range(10)]
    # p = [(lambda x: (x, 'child'+str(x))) for x in range(10)]
    # print p
    # f = [(x, 'child'+str(x)) for x in range(10)]
    # print f
