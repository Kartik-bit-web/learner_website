from databaseconnection import mydb
import uuid
import datetime

cursor = mydb.cursor()

class insert_category:
    def __init__(self, category_name, category_title, file_name):
        self.category_name = category_name
        self.category_title  =category_title
        self.file_name = file_name
    
    def insert_it(self):
        sql = ''' 
            INSERT INTO categories (uuid, category_name, category_title, file_name, date_creation) VALUES (%s, %s, %s, %s, %s)
        '''
        val = (uuid.uuid4().hex, self.category_name, self.category_title, self.file_name, datetime.datetime.now())
        cursor.execute(sql, val)
        mydb.commit()

x = {
    'Python': ['Python', 'Basics and Advance', 'img01'],
    'NodeJS': ['NodeJS', 'Basics and Advance With Pactice', 'img02'],
    'SQL': ['SQL', 'Basics and Advance With Pactice', 'img03'],
    'Git': ['Git', 'Version Control', 'img04'],
    'Nginx': ['Nginx', 'Web Server', 'img05'],
    'Linux': ['Linux', 'Servers and Networking Practics', 'img06']
}

#for i in x:
#    data = insert_category(x[i][0], x[i][1], x[i][2])
#    data.insert_it()
#print('build')
cursor.close()
