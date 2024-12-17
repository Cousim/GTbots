import mysql.connector
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import csv


db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234", 
  auth_plugin='mysql_native_password'
)
#print(db_connection)

# creating database_cursor to perform SQL operation to run queries
db_cursor = db_connection.cursor(buffered=True)

# executing cursor with execute method and pass SQL query
# db_cursor.execute("CREATE DATABASE gametheory")

# get list of all databases
# db_cursor.execute("SHOW DATABASES")

# print all databases
#for db in db_cursor:
#    print(db)

db_cursor.execute("USE gametheory")

'''
db_cursor.execute("""
CREATE TABLE BILATERAL_CLOSED_DETERMINISTIC (
    id INT NOT NULL, 
    most_coop_strat VARCHAR(255), 
    less_coop_strat VARCHAR(255), 
    less_defect_strat VARCHAR(255), 
    most_defect_strat VARCHAR(255), 
    coop_commit_prob FLOAT, 
    budget FLOAT, 
    assume_commit_prob FLOAT, 
    commit_type BOOLEAN, 
    opponent_coop_commit_type VARCHAR(255), 
    PRIMARY KEY (id)
)
""")
'''

db_cursor.execute("SHOW TABLES")
tables = db_cursor.fetchall()

for table in tables:
    print(table[0])  # Each table is returned as a tuple


insert_bilateral_closed_deterministic = (
    "INSERT INTO BILATERAL_CLOSED_DETERMINISTIC "
    "(id, most_coop_strat, less_coop_strat, less_defect_strat, most_defect_strat, coop_commit_prob, budget, assume_commit_prob, commit_type, opponent_coop_commit_type) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)



