#testing how to get tables
import sqlite3
def create_table(instr):
    
    db=sqlite3.connect('C:\code\chat app v1\engine\login_engine_with_database\darft.db')
    c=db.cursor()
    c.execute(instr)
    db.commit()
    db.close()
    
def extract_tables(instr):
    db=sqlite3.connect('C:\code\chat app v1\engine\login_engine_with_database\darft.db')
    c=db.cursor()
    c.row_factory=sqlite3.Row
    c.execute(instr)
    result=[dict(row) for row in c.fetchall()]
    db.commit()
    db.close()
    print(result)
'''
instr1='CREATE TABLE want( too TEXT, eat TEXT) '
instr2='CREATE TABLE wants( eating TEXT) '

create_table(instr1)
create_table(instr2)
'''

table_extract_instr = """SELECT name FROM sqlite_master
    WHERE type='table';"""
table_extract_instr='SELECT * FROM wants'
extract_tables(table_extract_instr)
