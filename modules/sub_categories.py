from databaseconnection import mydb
import uuid
import datetime

cursor = mydb.cursor()

class insert_sub_category:
    def __init__(self, sub_category_name, sub_category_title, categories_id):
        self.sub_category_name = sub_category_name
        self.sub_category_title  =sub_category_title
        self.categories_id = categories_id
    
    def insert_it(self):
        sql = ''' 
            INSERT INTO sub_categories (uuid, sub_category_name, sub_category_title, categories_id, date_creation) VALUES (%s, %s, %s, %s, %s)
        '''
        val = (uuid.uuid4().hex, self.sub_category_name, self.sub_category_title, self.categories_id, datetime.datetime.now())
        cursor.execute(sql, val)
        mydb.commit()

x = {
    'Basics': ['Basics', 'Number, Text, List, Basic Calulations', 1],
    'Terms Explaination': ['Built-In-Types', 'Numaric, Boolean, Mapping, Set', 1],
    'Control': ['Control-flow and Functions', 'If, For, While, Def', 1],
    'DataStucture' : ['Data Stucture', 'Stack, Queues, Tuple, Sets', 1],
    'Modules': ['Modules', 'Importing, Local, Packages', 1],
    'I&O': ['Input and Output', 'Reading Files, Formatting String, json', 1],
    'ErrorHandle': ['Error and Exception', 'user-define-excetion, Syntax error', 1],
    'Classes': ['Classes', 'Name, Object, methods', 1],
    'Library-1': ['Library-1', 'date and Time, Files, OS', 1],
    'Library-2': ['Library-2', 'Work with binary, Multi threading, logging', 1],
    'Virtual': ['Virtual Enviroment', 'Create Virtual Env', 1],
    'Glossary': ['Glossary', 'Defines the important words ', 1],

    'basic': ['basic', 'Aysic/await, Promise, Events ', 2],
    'crypto': ['crypto', 'cyptography data', 2],
    'Event': ['Event', 'Events in nodejs', 2],
    'HTTP/HTTPS': ['HTTP/HTTPS', 'http and server', 2],
    'Net': ['Net', 'Using of Net ', 2],
    'Path': ['Path', 'Dir, file path, os.path ', 2],
    'FileSystem': ['FileSystem', 'File create, modifying, delete, append data', 2],
    'Stream': ['Stream', 'Files streaming and handling', 2],
    'OS': ['OS', 'Using OS for knowing more about machine', 2],
    'Express': ['Express', 'API, Routing, connect with database', 2],

    'MySQL': ['MySQL Server', 'Install, Server Admin, Security, Backup and Recovery', 3],
    'Basic': ['Basic', 'Basics of SQL', 3],
    'DataTypes': ['Data Types', 'Types of data in SQl', 3],
    'Function': ['Funtions and Oprators', 'In build funtios', 3],
    'constrains': ['Contstrains', 'primary key, foreign key', 3],
    'control': ['Control Sataments', 'Case, between, logical', 3],
    'Join': ['Join', 'Self Join, Left Join, Full Join', 3],
    'statments': ['SQL Statments', 'DDL, DML, DCL, TCL', 3],

    'GitBasic': ['Git Basic', 'Init, add . , commit, remote', 4],
    'Branching': ['Branching', 'Switch, merge branch, branch create', 4],
    'gitServer': ['Git On Server', 'Init', 4],
    'Distribute': ['Distribute', 'push to Share Repository', 4],
    'gtihub': ['Gtihub', 'Github', 4],
    'customizing_git': ['Customizing Git', 'configuration, hooks', 4],

    'NginxBasic' : ['Nignx Basics ', 'installation, server start, configurations file', 5],
    'NginxAdmin' : ['Nignx Amdin guide ', 'Files, create server, security', 5],
    'controlling' : ['Nignx Control ', 'Load Balancer, permission, SSL', 5],
    'connection' : ['Connecting Processing Method ', 'connections, HTTP request', 5],
    'hashes' : ['Hashes ', 'using hash on nginx', 5],
    'Debuglog' : ['Debugging Log', 'Log files, System Log', 5],
    'configuration' : ['configuration file ', ' files, /etc/file', 5],
    'servername': ['Server Name', 'naming of servers', 5],
    'TCP/UDP' : ['TCP/UDP session', 'session', 5],
    'HTTPS' : ['HTTPS Configuration', 'HTTPS certificate', 5],


    'Linux' : ['Installation Linux', 'Install, Boot drive', 6],
    'linuxServer' : ['Linux server', 'Server installation', 6],
    'nginx' : ['Install Nginx', 'nginx', 6],
    'mysqlserver' : ['MySQL Server', 'Install and setup admin', 6],
    'git' : ['Git', 'install Git', 6]
}

#for i in x:
#    data = insert_sub_category(x[i][0], x[i][1], x[i][2])
#    data.insert_it()
#print('build')
cursor.close()