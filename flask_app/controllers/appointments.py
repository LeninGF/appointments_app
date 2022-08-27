from urllib import request
from flask_app import app
from flask import render_template, redirect, flash, session, request
from flask_app.models.appointment import Appointment
from flask_app.models.user import User

@app.route('/appointments')
def myappointments():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {"id":session['user_id']}
    user = User.get_by_id(data)
    # all_appointments = Appointment.get_all()
    # all_appointments = Appointment.get_all_where_user_is(data)
    all_appointments = Appointment.get_pending_where_user_is(data)
    all_past_appointments = Appointment.get_all_past_where_user_is(data)
    return render_template("appointments.html", user=user, all_appointments=all_appointments, all_past=all_past_appointments)

@app.route("/appointments/add")
def appointments_form():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {"id":session['user_id']}
    return render_template("create_appointment.html", user=User.get_by_id(data))

@app.route("/create-appointment", methods = ["POST"])
def create_appointment():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Appointment.validate_register(request.form):
        return redirect('/appointments/add')
    data = {
        "task":request.form["task"],
        "date":request.form["date"],
        "status":request.form["status"],
        "user_id": session["user_id"]
    }
    print(request.form)
    print("Fechas", data['date'])
    Appointment.save(data)
    return redirect('/appointments')

@app.route('/appointments/delete/<int:id>')
def delete_appointment(id):
    Appointment.delete_by_id({"id":id})
    return redirect('/appointments')

@app.route('/appointments/edit/<int:id>')
def render_update_form(id):
    if 'user_id' not in session:
        return redirect('/logout')
    all_about_appointment = Appointment.get_by_id({"id":id})
    session['appointment_id'] = id
    return render_template("edit_appointment.html", this=all_about_appointment, user = User.get_by_id({"id":session['user_id']}))


@app.route('/edit-appointment', methods=['POST'])
def update_appointment():
    if 'user_id' not in session:
        return redirect('/logout')
    appointment_id = session['appointment_id']
    if not Appointment.validate_register(request.form):
        return redirect(f'/appointments/edit/{appointment_id}')
    data = {
        "id": appointment_id,
        "task":request.form["task"],
        "date":request.form["date"],
        "status":request.form["status"],
        "user_id": session["user_id"]
    }
    Appointment.update(data)
    return redirect('/appointments')
