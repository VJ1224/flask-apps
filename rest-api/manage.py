import os
from flask_script import Manager # noqa
from flask_migrate import Migrate, MigrateCommand # noqa

from app import app # noqa
from models import db # noqa


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
