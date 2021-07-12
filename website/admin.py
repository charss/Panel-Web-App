from flask import Blueprint, render_template, url_for, request, jsonify
import json
from werkzeug.utils import redirect
from .models import Group, Student
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
    
    
    if db.session.query(Group).first(): 
        return render_template('groups.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('groups.html', groups=None, current_id=1)

@admin.route('/new_group/', methods=['GET', 'POST'])
def new_group():
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()


    if request.method == 'POST':
        data = request.json
        groupName = data['group_name']
        projectTitle = data['project_title']
        program = data['program']
        i = 0
        for prop in data['proponents']:
            if i == 0:
                studNo = prop
            elif i == 1:
                lastName = prop
            elif i == 2:
                firstName = prop
            elif i == 3:
                middleI = prop
                new_student = Student(stud_no=studNo, 
                                      last_name=lastName, 
                                      first_name=firstName,
                                      middle_in=middleI,
                                      group_id=obj.id+1)
                db.session.add(new_student)
                db.session.commit()
                i = -1
            i += 1


        new_group = Group(name=groupName, 
                          project_title=projectTitle, 
                          program=program)
        db.session.add(new_group)
        db.session.commit()
        return jsonify(data)

    if db.session.query(Group).first(): 
        return render_template('new_group.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('new_group.html', groups=None, current_id=1)

    

@admin.route('/panelist/')
def panelist():
    return render_template('panelist.html')

@admin.route('/schedule/')
def schedule():
    return render_template('schedule.html')

@admin.route('/student/')
def student():
    if db.session.query(Student).first(): 
        return render_template('student.html', students=Student.query.all())
    else:
        return render_template('student.html', students=None)
    return render_template('student.html')

# @admin.route('/create_new_group/')
# def schedule():
#     return render_template('schedule.html')