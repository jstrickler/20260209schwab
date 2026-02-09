import psycopg

pg_conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
pg_cursor = pg_conn.cursor()

# select specified columns from all presidents
pg_cursor.execute('''
    select termnum, firstname, lastname, party
    from presidents
''')  # execute a SQL statement


row = pg_cursor.fetchone()
print(f"{row = }")
print('-' * 60)

for row in pg_cursor.fetchmany(5):
    print(row)
print('-' * 60)


for row in pg_cursor.fetchall():
    print(row)
print()

pg_cursor.close()
pg_conn.close()

