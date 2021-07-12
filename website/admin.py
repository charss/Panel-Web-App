from flask import Blueprint, render_template, url_for,request
from werkzeug.utils import redirect
from .models import Group
from . import db

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates/admin')


@admin.route("/home")
def home():
    # return "<h1>HOME</h1>"
    return render_template("home.html")


@admin.route('/groups/', methods=['GET', 'POST'])
def group():
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()
    if request.method == 'POST':
        groupName = request.form.get('groupName')
        projectTitle = request.form.get('projectTitle')
        program = request.form.get('program')


        new_group = Group(name=groupName, project_title=projectTitle, program=program)
        db.session.add(new_group)
        db.session.commit()

    if db.session.query(Group).first(): 
        return render_template('groups.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('groups.html', groups=None, current_id=1)

@admin.route('/new_group/', methods=['GET', 'POST'])
def new_group():
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()
    if db.session.query(Group).first(): 
        return render_template('groups.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('groups.html', groups=None, current_id=1)

@admin.route('/panelist/')
def panelist():
    return render_template('panelist.html')

@admin.route('/schedule/')
def schedule():
    return render_template('schedule.html')


# @admin.route('/create_new_group/')
# def schedule():
#     return render_template('schedule.html')