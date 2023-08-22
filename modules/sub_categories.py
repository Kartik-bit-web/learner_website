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
    'Basics': ['Basics', 'Number, Text, List, Basic Calulations', 13],
    'Terms Explaination': ['Built-In-Types', 'Numaric, Boolean, Mapping, Set', 13],
    'Control': ['Control-flow and Functions', 'If, For, While, Def', 13],
    'DataStucture' : ['Data Stucture', 'Stack, Queues, Tuple, Sets', 13],
    'Modules': ['Modules', 'Importing, Local, Packages', 13],
    'I&O': ['Input and Output', 'Reading Files, Formatting String, json', 13],
    'ErrorHandle': ['Error and Exception', 'user-define-excetion, Syntax error', 13],
    'Classes': ['Classes', 'Name, Object, methods', 13],
    'Library-1': ['Library-1', 'date and Time, Files, OS', 13],
    'Library-2': ['Library-2', 'Work with binary, Multi threading, logging', 13],
    'Virtual': ['Virtual Enviroment', 'Create Virtual Env', 13],
    'Glossary': ['Glossary', 'Defines the important words ', 13],

    'basic': ['basic', 'Aysic/await, Promise, Events ', 14],
    'crypto': ['crypto', 'cyptography data', 14],
    'Event': ['Event', 'Events in nodejs', 14],
    'HTTP/HTTPS': ['HTTP/HTTPS', 'http and server', 14],
    'Net': ['Net', 'Using of Net ', 14],
    'Path': ['Path', 'Dir, file path, os.path ', 14],
    'FileSystem': ['FileSystem', 'File create, modifying, delete, append data', 14],
    'Stream': ['Stream', 'Files streaming and handling', 14],
    'OS': ['OS', 'Using OS for knowing more about machine', 14],
    'Express': ['Express', 'API, Routing, connect with database', 14],

    'MySQL': ['MySQL Server', 'Install, Server Admin, Security, Backup and Recovery', 15],
    'Basic': ['Basic', 'Basics of SQL', 15],
    'DataTypes': ['Data Types', 'Types of data in SQl', 15],
    'Function': ['Funtions and Oprators', 'In build funtios', 15],
    'constrains': ['Contstrains', 'primary key, foreign key', 15],
    'control': ['Control Sataments', 'Case, between, logical', 15],
    'Join': ['Join', 'Self Join, Left Join, Full Join', 15],
    'statments': ['SQL Statments', 'DDL, DML, DCL, TCL', 15],

    'GitBasic': ['Git Basic', 'Init, add . , commit, remote', 16],
    'Branching': ['Branching', 'Switch, merge branch, branch create', 16],
    'gitServer': ['Git On Server', 'Init', 16],
    'Distribute': ['Distribute', 'push to Share Repository', 16],
    'gtihub': ['Gtihub', 'Github', 16],
    'customizing_git': ['Customizing Git', 'configuration, hooks', 16],

    'NginxBasic' : ['Nignx Basics ', 'installation, server start, configurations file', 17],
    'NginxAdmin' : ['Nignx Amdin guide ', 'Files, create server, security', 17],
    'controlling' : ['Nignx Control ', 'Load Balancer, permission, SSL', 17],
    'connection' : ['Connecting Processing Method ', 'connections, HTTP request', 17],
    'hashes' : ['Hashes ', 'using hash on nginx', 17],
    'Debuglog' : ['Debugging Log', 'Log files, System Log', 17],
    'configuration' : ['configuration file ', ' files, /etc/file', 17],
    'servername': ['Server Name', 'naming of servers', 17],
    'TCP/UDP' : ['TCP/UDP session', 'session', 17],
    'HTTPS' : ['HTTPS Configuration', 'HTTPS certificate', 17],


    'Linux' : ['Installation Linux', 'Install, Boot drive', 18],
    'linuxServer' : ['Linux server', 'Server installation', 18],
    'nginx' : ['Install Nginx', 'nginx', 18],
    'mysqlserver' : ['MySQL Server', 'Install and setup admin', 18],
    'git' : ['Git', 'install Git', 18]
}

#for i in x:
#    data = insert_sub_category(x[i][0], x[i][1], x[i][2])
#    data.insert_it()
#print('build')
cursor.close()