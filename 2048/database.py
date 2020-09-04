import sqlite3

bd = sqlite3.connect("2048.sqllite")

cur = bd.cursor()

cur.execute('''
            create table if not exists RECORDS(
            name text, 
            score integer)
''')


def insert_result(name, score):
    cur.execute("""
          insert into RECORDS values (?, ?)
    """, (name, score))
    bd.commit()


def get_best():
    cur.execute('''
                SELECT name gamer, max(score) score from RECORDS
                GROUP by name
                ORDER BY score DESC
                limit 3
    ''')

    return cur.fetchall()

