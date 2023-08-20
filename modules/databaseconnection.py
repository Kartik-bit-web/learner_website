#Sign up tables will execute from here using OOP Python
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = '@karTIK32',
    database = 'web_leaner',
    auth_plugin='mysql_native_password'
)

db = mydb.cursor()

data_push = {}

#main product tables:----
data_push['sql_categories'] = (''' CREATE TABLE IF NOT EXISTS `categories` (
        id INTEGER NOT NULL AUTO_INCREMENT,
        uuid CHAR(40) NOT NULL,
        category_name VARCHAR(30) NOT NULL,
        category_title VARCHAR(100) NOT NULL,
        file_name VARCHAR(30) NOT NULL,
        date_creation DATE NOT NULL,
        PRIMARY KEY(id)
 )''')

data_push['sql_sub_category'] = (''' CREATE TABLE IF NOT EXISTS `sub_categories` (
        id INTEGER NOT NULL AUTO_INCREMENT,
        uuid CHAR(40) NOT NULL,
        sub_category_name VARCHAR(30) NOT NULL,
        sub_category_title VARCHAR(100) NOT NULL,
        categories_id INTEGER,
        date_creation DATE NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (categories_id) REFERENCES categories (id)
)''')
                                 
data_push['sql_product']= (''' CREATE TABLE IF NOT EXISTS `products` (
        id INTEGER NOT NULL AUTO_INCREMENT,
        uuid CHAR(40) NOT NULL,
        product_name VARCHAR(30) NOT NULL,
        product_title VARCHAR(100) NOT NULL,
        code_text TEXT(20000) NOT NULL,
        defination TEXT(20000) NOT NULL,
        sub_categories_id INTEGER,
        date_creation DATE NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (sub_categories_id) REFERENCES sub_categories (id)
        
)''')

#Login and Register:-----
data_push['Registeration'] = (''' CREATE TABLE IF NOT EXISTS `register_users` (
        id INTEGER NOT NULL AUTO_INCREMENT,
        uuid CHAR(40) NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(30) NOT NULL UNIQUE,
        password CHAR(64) NOT NULL,
        date_creation DATE NOT NULL,
        PRIMARY KEY(id)
) ''')

for i in data_push:
    execute_it = data_push[i]
    db.execute(execute_it)
    print('All table are created')

db.close()

print('Database Closed Succesfully')
