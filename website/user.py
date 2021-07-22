from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
from flask_login import login_required, current_user
from .models import Group, Student, Panelist, Defense
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

@user.route("/grading/<tab>/<content>")
@login_required
def indiv_sheet(tab, content):
    defense = db.session.query(Defense).filter_by(id=content).first()
    if tab == 'indiv':
        return render_template('grading/indiv_sheet.html', defense=defense)
    elif tab == 'group':
        return render_template('grading/group_sheet.html', defense=defense)
    elif tab == 'comment':
        return render_template('grading/comment_sheet.html', defense=defense)




