from sqlalchemy.sql.expression import nullslast
from . import db
# from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # notes = db.relationship('Note')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    project_title = db.Column(db.String(150), nullable=False)
    program = db.Column(db.String(150), nullable=False)
    members = db.relationship('Student', backref='group')

class Student(db.Model):
    stud_no = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_in = db.Column(db.String(10))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))



# Foreign Key setup
# user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# notes = db.relationship('Note')