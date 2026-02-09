import ibm_db_dbi as db2
from db_alternate_cursors import dict_cursor

conn = db2.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=scripts;")

cursor = conn.cursor()

# select first name, last name from all presidents
if cursor.execute('''
    select lastname, firstname, party
    from presidents
'''):

    dc = dict_cursor(cursor)  # create dict cursor
    for row in dc:
        print(row['FIRSTNAME'], row['LASTNAME'], row['PARTY'])  # use column names

cursor.close()
conn.close()
