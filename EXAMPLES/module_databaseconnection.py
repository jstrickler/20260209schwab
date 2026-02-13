# only one connection and one cursor will be created

import sqlite3

databaseconnection = sqlite3.connect(':memory:')

db_cursor = databaseconnection.cursor()

