from databaseconnection import mydb

from modules.databaseconnection import mydb
import uuid
import datetime

cursor = mydb.cursor()


class registration:
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    @staticmethod
    def passwordEncrypt():
        pass
    
    def Insert_it(self):
        cursor = mydb.cursor()
        cursor.execute('SELECT email FROM register_users')
        x = cursor.fetchall()
        if self.email in x:
            return 'Email already Exist'
        else:
            sql = ''' 
                INSERT INTO register_users (uuid, first_name, last_name, email, password, date_creation)
                VALUES(%s, %s, %s, %s, %s, %s)
            '''
            val = (uuid.uuid4().hex, self.firstname, self.lastname, self.email, self.password, datetime.datetime.now())
    
            cursor.execute(sql, val)
            cursor.close()
            return 'User Successfully Added'
        