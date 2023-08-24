from modules.databaseconnection import mydb
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
import uuid
import datetime

cursor = mydb.cursor()


class registration:
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def Insert_it(self):
        cursor = mydb.cursor()
        
        sql = ''' 
            INSERT INTO register_users (uuid, first_name, last_name, email, password, date_creation)
            VALUES(%s, %s, %s, %s, %s, %s)
        '''
        val = (uuid.uuid4().hex, 
               self.firstname, self.lastname, self.email, 
               generate_password_hash(self.password, method='sha256'), 
               datetime.datetime.now())
        cursor.execute(sql, val)
        mydb.commit()

        return 'User Successfully Added'
