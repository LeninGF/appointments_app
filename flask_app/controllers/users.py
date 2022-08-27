from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":bcrypt.generate_password_hash(request.form['password'])
    }
    session["user_id"] = User.save(data)
    print(session)
    return redirect('/appointments')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    print(user.id)
    session['user_id'] = user.id
    return redirect('/appointments')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
