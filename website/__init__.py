from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .commands import create_tables
from .extensions import db 

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app) 

    from .admin import admin
    # from .panelist import panelist
    from .auth import auth
    from .user import user

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(user, url_prefix='/')



    from .models import Panelist, Master

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(username):
        if username == 'admin':
            return Master.query.filter_by(username=username).first()
        return Panelist.query.filter_by(username=username).first()

    app.cli.add_command(create_tables)
    return app
