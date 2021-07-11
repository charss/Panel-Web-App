from flask import Blueprint, render_template, request
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
    obj = db.session.query(Group).order_by(Group.id.desc()).first()
    if request.method == 'POST':
        groupName = request.form.get('groupName')
        projectTitle = request.form.get('projectTitle')
        program = request.form.get('program')


        new_group = Group(name=groupName, project_title=projectTitle, program=program)
        db.session.add(new_group)
        db.session.commit()
        
    return render_template('groups.html', current_id=obj.id+1)

@admin.route('/panelist/')
def panelist():
    return render_template('panelist.html')

@admin.route('/schedule/')
def schedule():
    return render_template('schedule.html')


# @admin.route('/create_new_group/')
# def schedule():
#     return render_template('schedule.html')