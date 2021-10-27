#import required libs
import os
import re
import sys
import mysql.connector
from mysql.connector import Error
import ipdb
#ipdb.trace()

def create_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect( 
                host=host_name, 
                user=user_name, 
                passwd=user_password, 
                database=database 
                )        
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "dev", "123456", "devopstt")

cursor=connection.cursor()

def get_db_version(cursor):
    """Check DB version"""
    cursor.execute("select * from versionTable;")
    for row in cursor:
        return row[0]

def get_files():
    version_numbers = []
    dbscripts = os.listdir("dbscripts")
    for file in dbscripts:
        m=re.search(r'^(\d\d)',file):
        if m:
            version_numbers.append(int(m.group(0)))
    db_version = get_db_version(cursor)
    if max (version_numbers) == db_version:
        print("BD version is already up to date") 
        sys.exit(0)
    else:
        for version in sort(version_numbers):
            for file in dbscripts:
                if version in file:
                    with open(file) as f:
                        cursor.execute(f.read())






