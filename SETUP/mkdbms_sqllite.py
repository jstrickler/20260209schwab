#!/usr/bin/python3
from typing import Any
import sqlite3

myconn = sqlite3.connect("presidents.db")

cursor = myconn.cursor()

cursor.execute("drop table if exists presidents")

create_table_sql = """
create table presidents (
    termnum integer primary key,
    lastname varchar(32),
    firstname varchar(64),
    termstart date,
    termend date,
    birthplace varchar(128),
    birthstate varchar(32),
    birthdate date,
    deathdate date,
    party varchar(32)
)
"""

insert_row_sql = """
insert into presidents (
    termnum, lastname, firstname, birthdate, deathdate,
    birthplace, birthstate, termstart, termend, party
)
values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

cursor.execute(create_table_sql)

with open ('../DATA/presidents.txt') as presidents_in:
    for line in presidents_in:
        fields: list[Any] = line.rstrip().split(':')
        for index in 4, 8: # deathdate, termend
            if fields[index] in ('', 'NONE'):
                fields[index] = None
            fields[0] = int(fields[0])
        cursor.execute(insert_row_sql, fields)

myconn.commit()
cursor.close()
myconn.close()
