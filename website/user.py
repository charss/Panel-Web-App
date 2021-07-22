from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
from flask_login import login_required, current_user
from .models import Group, Student, Panelist, Defense, Scores
from . import db
from .populate import *


user = Blueprint('user', __name__, static_folder='static', template_folder='templates/user')


@user.route("/user_home/")
@login_required
def user_home():
    return render_template("home_u.html", user=current_user)

@user.route("/user_groups/")
@login_required
def user_groups():
    return render_template('groups_u.html', user=current_user, groups=Group.query.all())

@user.route("/user_panelists/")
@login_required
def user_panelists():
    return render_template('panelists_u.html', user=current_user, panels=Panelist.query.all())

@user.route("/user_students/")
@login_required
def user_students():
    return render_template('students_u.html', user=current_user, students=Student.query.all())

@user.route("/grading/<tab>/<content>", methods=['GET', 'POST'])
@login_required
def grading(tab, content):
    defense = db.session.query(Defense).filter_by(id=content).first()
    for score in db.session.query(Scores).all():
        if score.defense_id == defense.id and score.panel_id == current_user.id:
            to_edit = db.session.query(Scores).filter_by(id=score.id).first() 
            break
    else:
        to_edit = Scores(
            defense_id=defense.id,
            panel_id=current_user.id
        )
        db.session.add(to_edit)
        db.session.commit()

    if request.method == 'POST':
        if tab == 'indiv':
            indiv_score = []
            for x in range(1, len(defense.group.members) + 1):
                indiv_score.append(request.form[f'student{x}'])
            temp = ','.join(indiv_score)
            to_edit.indiv_scores = temp
            db.session.commit()
        elif tab == 'group':
            to_edit.group_score = request.form['overall']
            db.session.commit()
        elif tab == 'comment':
            to_edit.comment = request.form['comments_inp']
            db.session.commit()
            
        return redirect(url_for('user.user_home'))

    if tab == 'indiv':
        return render_template('grading/indiv_sheet.html', defense=defense)
    elif tab == 'group':
        category_list = {}
        for rubric in defense.group_sheet.rubric:
            category_list.setdefault(rubric.category, [])
            category_list[rubric.category].append(rubric)
        print(category_list)
        return render_template('grading/group_sheet.html', defense=defense, categories=category_list)
    elif tab == 'comment':
        return render_template('grading/comment_sheet.html', defense=defense, comment=to_edit.comment)




