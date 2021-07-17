from flask import Blueprint, render_template, url_for, request, jsonify, session
from sqlalchemy.sql.operators import json_getitem_op
from werkzeug.utils import redirect
from .models import Group, Student, Panelist, Defense, Rubric, Gradesheet, Template
from flask_login import login_required, current_user
from . import db
from .populate import *
from datetime import datetime, date, time, timedelta

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates/admin')

@admin.route("/home/", defaults={'data' : 'None'})
@admin.route("/home/<data>")
@login_required
def admin_home(data):
    if not db.session.query(Group).first():
        populate_group()

    if not db.session.query(Student).first():
        populate_students()

    if not db.session.query(Panelist).first():
        populate_panelist()

    if not db.session.query(Defense).first():
        populate_defense()

    if not db.session.query(Rubric).first():
        populate_rubric()

    return render_template("home.html", rub_type=data)
    
@admin.route('/groups/', methods=['GET', 'POST'])
@login_required
def group():
    obj = 0
    if db.session.query(Group).first():
        obj = db.session.query(Group).order_by(Group.id.desc()).first()
    
    if request.method == 'POST':
        if request.form.get('search'):
            pass
    
    if db.session.query(Group).first(): 
        return render_template('groups.html', groups=Group.query.all(), current_id=obj.id+1)
    else:
        return render_template('groups.html', groups=None, current_id=1)

@admin.route('/new_group/', methods=['GET', 'POST'])
@login_required
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
@login_required
def edit_group(content):
    group = db.session.query(Group).filter_by(id=content).first()
    
    if request.method == 'POST':
        group.name = request.form['groupName']
        group.project_title = request.form['projectTitle']
        group.program = request.form['program']
        db.session.commit()

        return redirect(url_for('admin.group'))

    return render_template('edit_group.html', groups=Group.query.all(),to_edit=group)

@admin.route('/delete_group/<content>', methods=['GET', 'POST'])
@login_required
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

@admin.route('/panelist/', methods=['GET', 'POST'])
@login_required
def panelist():
    obj = 0
    if db.session.query(Panelist).first():
        obj = db.session.query(Panelist).order_by(Panelist.id.desc()).first()
    
    if db.session.query(Panelist).first(): 
        return render_template('panelist.html', panels=Panelist.query.all(), current_id=obj.id+1)
    else:
        return render_template('panelist.html', panels=None, current_id=1)

@admin.route('/new_panel/', methods=['GET', 'POST'])
@login_required
def new_panel():
    obj = 0
    if db.session.query(Panelist).first():
        obj = db.session.query(Panelist).order_by(Panelist.id.desc()).first()
    
    if request.method == 'POST':
        lastName = request.form['lastName']
        firstName = request.form['firstName']
        middleIn = request.form['middleIn']
        school = request.form['school']
        username = f"{lastName.lower()}_{school.lower()[4]}"
        password = f"{school.lower()[4:]}{obj.id+1}"

        new_panel = Panelist(last_name=lastName,
                             username=username,
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
@login_required
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
        panel.username = f"{panel.last_name.lower()}_{panel.school.lower()[4]}"
        panel.password = f"{panel.school.lower()[4:]}{panel.id}"

        db.session.commit()
        return redirect(url_for('admin.panelist'))

    if db.session.query(Panelist).first(): 
        return render_template('edit_panel.html', panels=Panelist.query.all(), current_id=obj.id+1, to_edit=panel)
    else:
        return render_template('edit_panel.html', panels=None, current_id=1)


@admin.route('/delete_panel/<content>', methods=['GET', 'POST'])
@login_required
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
@login_required
def student():
    if db.session.query(Student).first(): 
        return render_template('student.html', students=Student.query.all())
    else:
        return render_template('student.html', students=None)

@admin.route('/edit_student/<content>', methods=['GET', 'POST'])
@login_required
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
@login_required
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
@login_required
def schedule():
    obj = 0
    if db.session.query(Defense).first():
        obj = db.session.query(Defense).order_by(Defense.id.desc()).first()
    
    
    
    if db.session.query(Defense).first(): 
        return render_template('schedule.html', defenses=Defense.query.all(), current_id=obj.id+1)
    else:
        return render_template('schedule.html', defenses=None, current_id=1)

@admin.route('/new_sched/', methods=['GET', 'POST'])
@login_required
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
@login_required
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

        db.session.commit()
       
        return redirect(url_for('admin.schedule'))
    
    if db.session.query(Defense).first(): 
        return render_template('edit_sched.html', defenses=Defense.query.all(), groups=Group.query.all(), panels=Panelist.query.all(), to_edit=defense)
    else:
        return render_template('edit_sched.html', defenses=None, groups=Group.query.all(), panels=Panelist.query.all())

@admin.route('/delete_sched/<content>', methods=['GET', 'POST'])
@login_required
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

@admin.route('/rubrics/')
@login_required
def rubrics():
    obj = 0
    if db.session.query(Rubric).first():
        obj = db.session.query(Rubric).order_by(Rubric.id.desc()).first()
    
    if db.session.query(Rubric).first(): 
        return render_template('rubrics.html', rubrics=Rubric.query.all(), current_id=obj.id+1)
    else:
        return render_template('rubrics.html', rubrics=None, current_id=1)

@admin.route('/new_rubric/', methods=['GET', 'POST'])
@login_required
def new_rubric():
    obj = 0

    if db.session.query(Rubric).first():
        obj = db.session.query(Rubric).order_by(Rubric.id.desc()).first()
    
    if request.method == 'POST':
        desc = request.form['desc']
        rate5 = request.form['rate5']
        rate4 = request.form['rate4']
        rate3 = request.form['rate3']
        rate2 = request.form['rate2']
        rate1 = request.form['rate1']
        weight = int(request.form['weight'])
        rub_type = request.form['rubType']
        
        if rub_type == 'Group':
            pbl_lvl = request.form['pblLvl']
            category = request.form['category']
        else:
            pbl_lvl = category = None

        print(rub_type, pbl_lvl, category)
        temp = Rubric(
            desc=desc,
            rate5=rate5,
            rate4=rate4,
            rate3=rate3,
            rate2=rate2,
            rate1=rate1,
            weight=weight,
            rubric_type=rub_type,
            pbl_lvl=pbl_lvl,
            category=category
        )

        db.session.add(temp)
        db.session.commit()

       
        # return redirect(url_for('admin.rubrics'))
   
    if db.session.query(Rubric).first(): 
        return render_template('new_rubric.html', rubrics=Rubric.query.all(), current_id=obj.id+1)
    else:
        return render_template('new_rubric.html', rubrics=None, current_id=1)


@admin.route('/edit_rubric/<content>', methods=['GET', 'POST'])
@login_required
def edit_rubric(content):
    rubric = db.session.query(Rubric).filter_by(id=content).first()
    
    if request.method == 'POST':
        desc = request.form['desc']
        rate5 = request.form['rate5']
        rate4 = request.form['rate4']
        rate3 = request.form['rate3']
        rate2 = request.form['rate2']
        rate1 = request.form['rate1']
        weight = int(request.form['weight'])
        rubric_type = request.form['rubType']
        pbl_lvl = request.form['pblLvl']

        db.session.commit()
        return redirect(url_for('admin.rubrics'))
    
    return render_template('edit_rubric.html', rubrics=Rubric.query.all(), to_edit=rubric)

@admin.route('/delete_rubric/<content>', methods=['GET', 'POST'])
@login_required
def delete_rubric(content):
    if request.method == 'POST':
        if request.form['submit'] == 'yes':
            db.session.query(Rubric).filter_by(id=content).delete()
            db.session.commit()
            return redirect(url_for('admin.rubrics'))
        else:
            return redirect(url_for('admin.rubrics'))

    if db.session.query(Defense).first(): 
        return render_template('delete_rubric.html', rubrics=Rubric.query.all())
    else:
        return render_template('delete_rubric.html', rubrics=None)

@admin.route('/gradesheets/')
@login_required
def gradesheets():
    obj = 0
    try:
        session.pop('trial')
        print("MAY SESSION")
    except:
        print("WALANG SESSION")

    if db.session.query(Template).first():
        obj = db.session.query(Template).order_by(Template.id.desc()).first()
    
    if db.session.query(Template).first(): 
        return render_template('gradesheet.html', templates=Template.query.all(), current_id=obj.id+1)
    else:
        return render_template('gradesheet.html', templates=None, current_id=1)


@admin.route('/new_sheet/', defaults={'data' : 'None'}, methods=['GET', 'POST'])
@admin.route('/new_sheet/<data>', methods=['GET', 'POST'])
@login_required
def new_sheet(data):
    obj = 0
    back_arr = []
    back_rub = None
    try:
        if session['trial']:
            back_arr = session['trial']['rubrics']
            back_rub = session['trial']['rubric_type']
            print('BACKED')
    except:
        print("BRAND NEW")

    if db.session.query(Template).first():
        obj = db.session.query(Template).order_by(Template.id.desc()).first()

    if request.method == 'POST':
        multiselect = request.form['invis'].split(',')
        if '-1982' in multiselect:
            multiselect.pop(0)
        print(multiselect)
        rubric_type = request.form['rubType']

        contents = {
            'rubric_type': rubric_type,
            'rubrics': multiselect
        }

        session['trial'] = contents
        
        return redirect(url_for('admin.confirm_sheet', contents=contents, rubrics=Rubric.query.all()))

    if db.session.query(Template).first():
        return render_template('new_sheet.html', rubrics=Rubric.query.all(), templates=Template.query.all(), back_arr=back_arr, back_rub=back_rub, current_id=obj.id+1, rub_type=data)
    else:
        return render_template('new_sheet.html', templates=None, rubrics=Rubric.query.all(), back_arr=back_arr, back_rub=back_rub, current_id=1, rub_type=data)


@admin.route('/view_sheet/<content>', methods=['GET', 'POST'])
@login_required
def view_sheet(content):

    template = db.session.query(Template).filter_by(id=content).first()
    rubrics = []

    for rubric in template.rubric:
        rubrics.append(rubric.id)

    return render_template('gradesheet/view_sheet.html', template=template, rubrics=template.rubric)

@admin.route('/edit_sheet/<content>', methods=['GET', 'POST'])
@login_required
def edit_sheet(content):
    template = db.session.query(Template).filter_by(id=content).first()

    try:
        if session['trial']:
            print('BACKED')
    except:
        print("BRAND NEW")


    if request.method == "POST":
        multiselect = request.form['invis'].split(',')
        if '-1982' in multiselect:
            multiselect.pop(0)
        
        contents = {
            'rubric_id': template.id,
            'rubric_type': template.sheet_type,
            'rubrics': multiselect
        }

        session['trial'] = contents
        
        return redirect(url_for('admin.c_edit_sheet'))

    return render_template('edit_sheet.html', to_edit=template, templates=Template.query.all(), rubrics=Rubric.query.all())

@admin.route('/c_edit_sheet/', methods=['GET', 'POST'])
@login_required
def c_edit_sheet():

    template = db.session.query(Template).filter_by(id=session['trial']['rubric_id']).first()

    new_rubrics = []
    for x in session['trial']['rubrics']:
        new_rubrics.append(db.session.query(Rubric).filter_by(id=x).first())

    if request.method == 'POST':
        if request.form.get('button_inp'):
            return redirect(url_for('admin.edit_sheet', content=template.id))
        else:
            template.rubric = []

            for rubric in new_rubrics:
                template.rubric.append(rubric)

            db.session.commit()
            session.pop('trial')
            return redirect(url_for('admin.gradesheets'))

    return render_template('gradesheet/individual2.html', rubrics=new_rubrics)

@admin.route('/confirm_sheet/', methods=['GET', 'POST'])
@login_required
def confirm_sheet():
    obj = 0
    if db.session.query(Template).first():
        obj = db.session.query(Template).order_by(Template.id.desc()).first()

    rubric_list = []
    for rubric in session['trial']['rubrics']:
        rubric_list.append(db.session.query(Rubric).filter_by(id=rubric).first())

    if request.method == 'POST':
        if request.form.get('button_inp'):
            return redirect(url_for('admin.new_sheet'))
        else:
            print('SUBMITTING')
            print(session['trial']['rubric_type'])
            new_template = Template(sheet_type=session['trial']['rubric_type'])
            db.session.add(new_template)


            for rubric in rubric_list:
                new_template.rubric.append(rubric)

            db.session.commit()
            session.pop('trial')
            return redirect(url_for('admin.gradesheets'))


    if db.session.query(Template).first():
        return render_template('gradesheet/individual.html', rubrics=rubric_list, current_id=obj.id+1)
    else:
        return render_template('gradesheet/individual.html', rubrics=rubric_list, current_id=1)



@admin.route('/parse_data/', methods=['GET', 'POST'])
def parse_data():
    if request.method == "POST":
        data = request.get_json()
        print(data['key'])
        # return redirect(url_for('admin.admin_home', data=data['key']))
        return jsonify(data)
        render_template('home.html', data=data['key'])
