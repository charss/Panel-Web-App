from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates/admin')


@admin.route("/home")
def home():
    # return "<h1>HOME</h1>"
    return render_template("home.html")


@admin.route('/groups/', methods=['GET', 'POST'])
def group():
    return render_template('groups.html')

@admin.route('/panelist/')
def panelist():
    return render_template('panelist.html')

@admin.route('/schedule/')
def schedule():
    return render_template('schedule.html')


# @admin.route('/create_new_group/')
# def schedule():
#     return render_template('schedule.html')