import sqlite3
from db_alternate_cursors import dataclass_cursor

with sqlite3.connect("../DATA/presidents.db") as conn:
    cursor = conn.cursor()

    # select first name, last name from all presidents
    num_recs = cursor.execute('''
        select firstname, lastname, party
        from presidents
    ''')
    for row in dataclass_cursor(cursor):
        full_name = f'{row.firstname} {row.lastname}'
        print(f'{full_name:35s} {row.party}')

