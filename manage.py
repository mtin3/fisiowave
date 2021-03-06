import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
# from app.main.model import profile, patient, appointment, clinic, invoice, blacklist


app = create_app(os.getenv('FISOWAVE') or 'dev')

# app = create_app(os.getenv('FISIOWAVE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
