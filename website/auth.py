from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Panelist, Master
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user, UserMixin


auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates/auth')



@auth.route('/login/', methods=['GET', 'POST'])
@auth.route('/', methods=['GET', 'POST'])
def login():
    if not db.session.query(Master).first():
        new_admin = Master(username='admin')
        db.session.add(new_admin)
        db.session.commit()
    else:
        master = db.session.query(Master).first()

    if current_user.is_authenticated:
        if current_user.username == 'admin':
            return redirect(url_for('admin.admin_home'))
        return redirect(url_for('user.user_home'))
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            login_user(master, remember=True)
            return redirect(url_for('admin.admin_home'))
        
        if user := Panelist.query.filter_by(username=username).first():
            if user.password == password:
                login_user(user, remember=True)
                return redirect(url_for('user.user_home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist', category='error')


    return render_template("index.html", user=current_user)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out.', category='success')
    return redirect(url_for('auth.login'))
