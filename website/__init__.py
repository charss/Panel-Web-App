from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 

    from .admin import admin
    # from .panelist import panelist
    from .auth import auth
    from .user import user

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(user, url_prefix='/')



    from .models import Panelist, Master

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(username):
        if username == 'admin':
            return Master.query.filter_by(username=username).first()
        return Panelist.query.filter_by(username=username).first()

    return app

    


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

