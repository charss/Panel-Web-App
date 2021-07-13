from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
from .models import Group, Student, Panelist, Defense
from . import db
from .populate import *
from datetime import datetime, date, time, timedelta

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates/admin')



@admin.route("/home")
def home():
    if not db.session.query(Group).first():
        populate_group()

    if not db.session.query(Student).first():
        populate_students()

    if not db.session.query(Panelist).first():
        populate_panelist()

    return render_template("home.html")


@admin.route('/groups/', methods=['GET', 'POST'])
def group():
    obj = 0
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()
    
    
    if db.session.query(Group).first(): 
        return render_template('groups.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('groups.html', groups=None, current_id=1)

@admin.route('/new_group/', methods=['GET', 'POST'])
def new_group():
    obj = 0
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()


    if request.method == 'POST':
        if type(obj) == int:
            temp = 0
        else:
            temp = obj.id
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
                                      group_id=temp)
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
    obj = 0
    if db.session.query(Panelist).first():
        obj = db.session.query(Panelist).order_by(Panelist.id.desc()).first()
    
    if db.session.query(Panelist).first(): 
        return render_template('panelist.html', panels=Panelist.query.all(), current_id=obj.id+1)
    else:
        return render_template('panelist.html', panels=None, current_id=1)

@admin.route('/new_panel/', methods=['GET', 'POST'])
def new_panel():
    obj = 0
    if db.session.query(Panelist).first():
        obj = db.session.query(Panelist).order_by(Panelist.id.desc()).first()
    
    if request.method == 'POST':
        lastName = request.form['lastName']
        firstName = request.form['firstName']
        middleIn = request.form['middleIn']
        school = request.form['school']

        new_panel = Panelist(last_name=lastName,
                             first_name=firstName,
                             middle_in=middleIn,
                             school=school)
        db.session.add(new_panel)
        db.session.commit()
        return redirect(url_for('admin.panelist'))

    if db.session.query(Panelist).first(): 
        return render_template('new_panel.html', panels=Panelist.query.all(), current_id=obj.id+1)
    else:
        return render_template('new_panel.html', panels=None, current_id=1)

@admin.route('/schedule/')
def schedule():
    obj = 0
    if db.session.query(Defense).first():
        obj = db.session.query(Defense).order_by(Defense.id.desc()).first()
    
    
    
    if db.session.query(Defense).first(): 
        return render_template('schedule.html', defenses=Defense.query.all(), current_id=obj.id+1)
    else:
        return render_template('schedule.html', defenses=None, current_id=1)

@admin.route('/new_sched/', methods=['GET', 'POST'])
def new_sched():
    obj = 0
    if db.session.query(Defense).first():
        obj = db.session.query(Defense).order_by(Defense.id.desc()).first()
    
    if request.method == 'POST':
        group = db.session.query(Group).filter_by(id=request.form['group'][5:]).first()
        panel1 = db.session.query(Panelist).filter_by(id=request.form['selectBox1']).first()
        panel2 = db.session.query(Panelist).filter_by(id=request.form['selectBox2']).first()
        panel3 = db.session.query(Panelist).filter_by(id=request.form['selectBox3']).first()
        
        date_temp  = date.fromisoformat(request.form['defense_date'])
        time_temp  = time.fromisoformat(request.form['start_time'])
        start_date = datetime.combine(date_temp, time_temp)

        duration = request.form['duration'][4:]
        end_date = start_date + timedelta(hours=int(duration))

        new_defense = Defense(group_id=group.id, start_date=start_date, end_date=end_date)
        db.session.add(new_defense)
        db.session.commit()

        new_defense.panels.append(panel1)
        new_defense.panels.append(panel2)
        new_defense.panels.append(panel3)

        db.session.commit()
       
        return redirect(url_for('admin.schedule'))
    
    if db.session.query(Defense).first(): 
        return render_template('new_sched.html', defenses=Defense.query.all(), current_id=obj.id+1, groups=Group.query.all(), panels=Panelist.query.all())
    else:
        return render_template('new_sched.html', defenses=None, current_id=1, groups=Group.query.all(), panels=Panelist.query.all())

@admin.route('/student/')
def student():
    if db.session.query(Student).first(): 
        return render_template('student.html', students=Student.query.all())
    else:
        return render_template('student.html', students=None)

# @admin.route('/create_new_group/')
# def schedule():
#     return render_template('schedule.html')