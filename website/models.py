from sqlalchemy.sql.expression import nullslast
from . import db
# from flask_login import UserMixin
from sqlalchemy.sql import func


panels = db.Table('panels',
         db.Column('panel_id', db.Integer, db.ForeignKey('panelist.id')),
         db.Column('movie_id', db.Integer, db.ForeignKey('defense.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    project_title = db.Column(db.String(150), nullable=False)
    program = db.Column(db.String(150), nullable=False)
    members = db.relationship('Student', backref='group')

class Student(db.Model):
    stud_no = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_in = db.Column(db.String(10))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))


class Panelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_in = db.Column(db.String(10))
    school = db.Column(db.String(150))
    

class Defense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    panelists = db.relationship(
        'Panelist',
        secondary=panels,
        backref=db.backref('panels')
    )