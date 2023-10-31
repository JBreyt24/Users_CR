
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.


class User:
    db = "users" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        # self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Users Models

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)


    # Read Users Models

    @classmethod
    def get_all(cls):
        query = """SELECT * 
        FROM users;
        """
        list_returned_from_db = connectToMySQL(cls.db).query_db(query)
        output = []
        for each_dictionary in list_returned_from_db:
            output.append(cls(each_dictionary))
        print(output)
        return output
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users 
        WHERE id = %(id)s
        """
        list_returned_from_db = connectToMySQL(cls.myDB).query_db(query, data)
        print(list_returned_from_db)
        return User(list_returned_from_db[0])

    # Update Users Models



    # Delete Users Models