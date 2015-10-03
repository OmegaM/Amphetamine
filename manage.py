#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/9/29 20:49 By OmegaMiao

    manage.py
"""


from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from amphetamine_app import amphetamine_app, db, mail
from amphetamine_app.models.mian_model import Amphetamine


manager = Manager(amphetamine_app)
migrate = Migrate(amphetamine_app, db)


def make_shell_context():
    return dict(amphetamine_app=amphetamine_app, db=db, Amphetamine=Amphetamine, mail=mail)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host='127.0.0.1', port=5000, use_debugger=True))
manager.add_command('db', MigrateCommand)  # add migrate command line

if __name__ == '__main__':
    manager.run()
