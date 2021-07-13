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

@admin.route('/edit_group/<content>', methods=['GET', 'POST'])
def edit_group(content):
    obj = 0
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()

    group = db.session.query(Group).filter_by(id=content).first()
    
    if request.method == 'POST':
        group.name = request.form['groupName']
        group.project_title = request.form['projectTitle']
        group.program = request.form['program']
        db.session.commit()

        return redirect(url_for('admin.group'))

    if db.session.query(Group).first(): 
        return render_template('edit_group.html', groups=Group.query.all(), current_id=obj.id+1, to_edit=group)
    else:
        return render_template('edit_group.html', groups=None, current_id=1, to_edit=None)

@admin.route('/delete_group/<content>', methods=['GET', 'POST'])
def delete_group(content):
    obj = 0
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()

    if request.method == 'POST':
        if request.form['submit'] == 'yes':
            db.session.query(Group).filter_by(id=content).delete()
            db.session.commit()
            return redirect(url_for('admin.group'))

        else:
            return redirect(url_for('admin.group'))

    if db.session.query(Group).first(): 
        return render_template('delete_group.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('delete_group.html', groups=None, current_id=1, to_edit=None)

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
        password = f"{school.lower()[4:]}{obj.id+1}"

        new_panel = Panelist(last_name=lastName,
                             password=password,
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

@admin.route('/edit_panel/<content>', methods=['GET', 'POST'])
def edit_panel(content):
    obj = 0
    if db.session.query(Group).first():
        obj = db.session.query(Panelist).order_by(Panelist.id.desc()).first()

    panel = db.session.query(Panelist).filter_by(id=content).first()
    
    if request.method == 'POST':

        panel.last_name = request.form['lastName']
        panel.first_name = request.form['firstName']
        panel.middle_in = request.form['middleIn']
        panel.school = request.form['school']


        db.session.commit()
        return redirect(url_for('admin.panelist'))

    if db.session.query(Panelist).first(): 
        return render_template('edit_panel.html', panels=Panelist.query.all(), current_id=obj.id+1, to_edit=panel)
    else:
        return render_template('edit_panel.html', panels=None, current_id=1)


@admin.route('/delete_panel/<content>', methods=['GET', 'POST'])
def delete_panel(content):
    obj = 0
    if db.session.query(Panelist).first():
        obj = db.session.query(Panelist).order_by(Panelist.id.desc()).first()

    if request.method == 'POST':
        if request.form['submit'] == 'yes':
            db.session.query(Panelist).filter_by(id=content).delete()
            db.session.commit()
            return redirect(url_for('admin.panelist'))
        else:
            return redirect(url_for('admin.panelist'))

    if db.session.query(Panelist).first(): 
        return render_template('delete_panel.html', panels=Panelist.query.all())
    else:
        return render_template('delete_panel.html', panels=None, current_id=1)

@admin.route('/student/')
def student():
    if db.session.query(Student).first(): 
        return render_template('student.html', students=Student.query.all())
    else:
        return render_template('student.html', students=None)

@admin.route('/edit_student/<content>', methods=['GET', 'POST'])
def edit_student(content):
    student = db.session.query(Student).filter_by(stud_no=content).first()
    
    if request.method == 'POST':
        student.last_name = request.form['lastName']
        student.first_name = request.form['firstName']
        student.middle_in = request.form['middleIn']
        student.school = request.form['school']
        student.group_id = request.form['groupID']


        db.session.commit()
        return redirect(url_for('admin.student'))

    if db.session.query(Student).first(): 
        return render_template('edit_student.html', students=Student.query.all(), to_edit=student)
    else:
        return render_template('edit_student.html', students=None)

@admin.route('/delete_student/<content>', methods=['GET', 'POST'])
def delete_student(content):
    if request.method == 'POST':
        if request.form['submit'] == 'yes':
            db.session.query(Student).filter_by(stud_no=content).delete()
            db.session.commit()
            return redirect(url_for('admin.student'))
        else:
            return redirect(url_for('admin.student'))

    if db.session.query(Student).first(): 
        return render_template('delete_student.html', students=Student.query.all())
    else:
        return render_template('delete_student.html', students=None, current_id=1)


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

        new_defense = Defense(group_id=group.id, start_date=start_date, end_date=end_date, head_panel_id=panel1.id)
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

@admin.route('/edit_sched/<content>', methods=['GET', 'POST'])
def edit_sched(content):
    defense = db.session.query(Defense).filter_by(id=content).first()

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

        defense.group_id      = group.id
        defense.start_date    = start_date
        defense.end_date      = end_date
        defense.head_panel_id = panel1.id
        defense.panels = []
        defense.panels.append(panel1)
        defense.panels.append(panel2)
        defense.panels.append(panel3)
        print(defense.panels)

        db.session.commit()
       
        return redirect(url_for('admin.schedule'))
    
    if db.session.query(Defense).first(): 
        return render_template('edit_sched.html', defenses=Defense.query.all(), groups=Group.query.all(), panels=Panelist.query.all(), to_edit=defense)
    else:
        return render_template('edit_sched.html', defenses=None, groups=Group.query.all(), panels=Panelist.query.all())

@admin.route('/delete_sched/<content>', methods=['GET', 'POST'])
def delete_sched(content):
    if request.method == 'POST':
        if request.form['submit'] == 'yes':
            db.session.query(Defense).filter_by(id=content).delete()
            db.session.commit()
            return redirect(url_for('admin.schedule'))
        else:
            return redirect(url_for('admin.schedule'))

    if db.session.query(Defense).first(): 
        return render_template('delete_sched.html', defenses=Defense.query.all(), groups=Group.query.all(), panels=Panelist.query.all())
    else:
        return render_template('delete_sched.html', defenses=None, groups=Group.query.all(), panels=Panelist.query.all())