import sqlite3

# list of one-element tuples -- each tuple provides parameters for
# a SQL statement. 
TERMS_TO_UPDATE = [(1,), (5,), (19,), (22,), (36,)]

PARTY_UPDATE = '''
update presidents 
set party = "SURPRISE!"
where termnum = ?
'''  # ? is SQLite3 placeholder for SQL statement parameter; different DBMSs use different placeholders

PARTY_QUERY = """
select termnum, firstname, lastname, party
from presidents
where termnum = ?
"""

with sqlite3.connect("../DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()
    # second argument to executemany() is iterable of parameters
    # each parameter is an iterable of values to fill in the placeholdelrs
    s3cursor.executemany(PARTY_UPDATE, TERMS_TO_UPDATE) 

    for param in TERMS_TO_UPDATE:
        term = param[0]
        s3cursor.execute(PARTY_QUERY, (term,))
        print(s3cursor.fetchone())