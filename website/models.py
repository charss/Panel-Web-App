from sqlalchemy.sql.expression import nullslast
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


defense_panel = db.Table('defense_panel',
         db.Column('panel_id', db.Integer, db.ForeignKey('panelist.id')),
         db.Column('defense_id', db.Integer, db.ForeignKey('defense.id'))
)

scores = db.Table('scores',
         db.Column('panel_id', db.Integer, db.ForeignKey('gradesheet.id')),
         db.Column('defense_id', db.Integer, db.ForeignKey('rubric.id')),
         db.Column('score', db.Integer)
)

# class User(db.Model):
#     id         = db.Column(db.Integer, primary_key=True)
#     email      = db.Column(db.String(150), unique=True)
#     password   = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))

class Group(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(150), nullable=False)
    project_title = db.Column(db.String(150), nullable=False)
    program       = db.Column(db.String(150), nullable=False)
    gradesheets   = db.relationship('Gradesheet', backref='group', uselist=True)
    members       = db.relationship('Student', backref='group', uselist=True)
    defenses      = db.relationship('Defense', backref='group', uselist=True)
    

class Student(db.Model):
    stud_no    = db.Column(db.Integer, primary_key=True)
    last_name  = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_in  = db.Column(db.String(10))
    group_id   = db.Column(db.Integer, db.ForeignKey('group.id'))
    


class Panelist(db.Model, UserMixin):
    id         = db.Column(db.Integer, primary_key=True)
    username   = db.Column(db.String(150), nullable=False)
    password   = db.Column(db.String(150), nullable=False)
    last_name  = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_in  = db.Column(db.String(10))
    school     = db.Column(db.String(150))
    header     = db.relationship('Defense', backref='head')
    paneling   = db.relationship(
        'Defense',
        secondary=defense_panel,
        backref=db.backref('panels')
    )

    def get_id(self):
        return self.username

class Master(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return self.username
    

class Defense(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    group_id      = db.Column(db.Integer, db.ForeignKey('group.id'))
    head_panel_id = db.Column(db.Integer, db.ForeignKey('panelist.id'))
    start_date    = db.Column(db.DateTime)
    end_date      = db.Column(db.DateTime)
    paneling      = db.relationship(
        'Panelist',
        secondary=defense_panel,
        backref=db.backref('defenses')
    )
    
class Gradesheet(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    sheet_type = db.Column(db.String(50), nullable=False)
    total      = db.Column(db.Integer, nullable=False)
    group_id   = db.Column(db.Integer, db.ForeignKey('group.id'))
    paneling   = db.relationship(
        'Rubric',
        secondary=scores,
        backref=db.backref('rubric')
    )


class Rubric(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    desc         = db.Column(db.String(150), nullable=False)
    rate1        = db.Column(db.String(150), nullable=False)
    rate2        = db.Column(db.String(150), nullable=False)
    rate3        = db.Column(db.String(150), nullable=False)
    rate4        = db.Column(db.String(150), nullable=False)
    rate5        = db.Column(db.String(150), nullable=False)
    weight       = db.Column(db.Integer, nullable=False)
    rubric_type  = db.Column(db.String(150), nullable=False)
    pbl_lvl      = db.Column(db.String(150), nullable=False)

    