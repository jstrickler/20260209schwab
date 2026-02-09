import sqlite3

# conn = sqlite3.Connection(...)
with sqlite3.connect("../DATA/presidents.db") as conn:  # connect to the database

    s3_cursor = conn.cursor()  # get a cursor object

    # select specified columns from all presidents
    s3_cursor.execute('''
        select termnum, firstname, lastname, party
        from presidents
    ''')  # execute a SQL statement

    row = s3_cursor.fetchone()
    print(f"{row = }")
    print('-' * 60)

    for row in s3_cursor.fetchmany(5):
        print(row)
    print('-' * 60)


    for row in s3_cursor.fetchall():
        print(row)
    print()

