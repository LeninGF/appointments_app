from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime


class Appointment:
    db = 'appointmentsdb'
    def __init__(self, data):
        self.id = data["id"]
        self.task = data["task"]
        self.date = data["date"]
        self.status = data["status"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    @classmethod
    def save(cls,data):
        query = "INSERT INTO appointments (task, date, status, user_id) VALUES(%(task)s,%(date)s,%(status)s,%(user_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    # @classmethod
    # def get_recipie_and_user(cls):
    #     # equivalent to get_all in bootcamp code
    #     query = "select name, under_30, users.first_name, recipies.id as receta_id, users.id as user_id from recipies left join users on recipies.user_id = users.id;"
    #     return connectToMySQL(cls.db).query_db(query)
    
    # @classmethod
    # def get_recipie_with_user_by_recipie_id(cls, data):
    #     query = "select * from recipies left join users on recipies.user_id = users.id where recipies.id=%(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query)
    #     return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM appointments;"
        results = connectToMySQL(cls.db).query_db(query)
        appointments = []
        for row in results:
            appointments.append( cls(row))
        return appointments
    
    
    @classmethod
    def get_all_where_user_is(cls, data):
        query = "SELECT * FROM appointments where user_id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        appointments = []
        for row in results:
            appointments.append( cls(row))
        return appointments
    
    @classmethod
    def get_pending_where_user_is(cls, data):
        query = "SELECT * FROM appointments where date(date) >= date(now()) and user_id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        appointments = []
        for row in results:
            appointments.append( cls(row))
        return appointments
    
    @classmethod
    def get_all_past_where_user_is(cls,data):
        query = "select * from appointments where date(date) < date(now()) and user_id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        appointments = []
        for row in results:
            appointments.append( cls(row))
        return appointments
    
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM appointments WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])    
    
    
    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM appointments WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
        
    
    @classmethod
    def update(cls, data):
        query = "UPDATE appointments SET task=%(task)s, date=%(date)s, status=%(status)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
        
    @staticmethod
    def validate_register(appointment):
        is_valid = True
        # query = "SELECT * FROM appointments WHERE task = %(task)s;"
        # results = connectToMySQL(Appointment.db).query_db(query,appointment)
        # if len(results) >= 1:
            # flash("Appointment already in database", 'appointment')
            # is_valid=False
        this_date = datetime.strptime(appointment['date'], '%Y-%m-%d')
        this_date = this_date.date()
        today = datetime.now().date()
        print(this_date, type(this_date))
        if len(appointment['task']) < 3:
            flash("Task Name must be at least 3 characters",'appointment')
            is_valid= False
        if len(appointment['date']) == "":
            flash("Please enter a date", 'appointment')
            is_valid=False
        if this_date<today:
            flash("Please insert a new future appointment", 'appointment')
            is_valid=False
        return is_valid
