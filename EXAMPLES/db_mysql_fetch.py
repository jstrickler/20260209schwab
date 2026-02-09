from contextlib import closing
import pymysql

myconn =  pymysql.connect(
        host="localhost",
        db="presidents",
        user="scripts",
        passwd="scripts",
)
mycursor = myconn.cursor()

# select specified columns from all presidents
row_count = mycursor.execute("""
SELECT termnum, firstname, lastname, party
FROM presidents
""")  # execute a SQL statement

print(f"{row_count} rows in result set\n")

row = mycursor.fetchone()
print(f"{row = }")
print('-' * 60)

for row in mycursor.fetchmany(5):
    print(row)
print('-' * 60)

for row in mycursor.fetchall():
    print(row)
print()

mycursor.close()
myconn.close()