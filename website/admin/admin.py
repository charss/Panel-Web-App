from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')


@admin.route("/home")
@admin.route("/")
def home():
    # return "<h1>HOME</h1>"
    return render_template("home.html")

@admin.route('/groups/')
def group():
    return render_template('groups.html')

@admin.route('/panelist/')
def panelist():
    return render_template('panelist.html')

@admin.route('/schedule/')
def schedule():
    return render_template('schedule.html')