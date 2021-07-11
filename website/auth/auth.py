from flask import Blueprint, redirect, url_for, render_template, request, session, flash

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates')



@auth.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['username']
        password = request.form['pass']

        if user == 'admin' and password == 'admin':
            return redirect(url_for('admin.home'))
    else:
        return render_template('login.html')



# @login.route("", methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         session.permanent = True
#         user = request.form['nm']
#         session['user'] = user

#         # Check if exist in database
#         found_user = users.query.filter_by(name=user).first()
#         # Delete an object
#         # found_user = users.query.filter_by(name=user).first()

#         # If there are many objects
#         # for user in found_user:
#         #     user.delete()
#         if found_user:
#             session['email'] = found_user.email
#         else:
#             usr = users(user, '')
#             db.session.add(usr)
#             db.session.commit()

#         flash(f'Login Successful!', "info")
#         return redirect(url_for("user"))
#     else:
#         if 'user' in session:
#             flash(f'Already Logged In!', "info")
#             return redirect(url_for("user"))

#         return render_template("login.html")