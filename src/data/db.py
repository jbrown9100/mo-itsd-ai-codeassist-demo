import sqlite3

DB_PATH = 'demo.db'


def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT, agency TEXT)')
    cur.execute('DELETE FROM people')
    cur.executemany('INSERT INTO people (name, agency) VALUES (?, ?)', [
        ('Ava Johnson', 'ITSD'),
        ('Noah Smith', 'OA'),
        ('Mia Garcia', 'DSS'),
        ('Liam Brown', 'DOR'),
    ])
    con.commit()
    con.close()


def insecure_search_people(name_fragment: str):
    """Intentionally insecure for demo: vulnerable to SQL injection."""
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = f"SELECT name, agency FROM people WHERE name LIKE '%{name_fragment}%'"  # VULNERABLE
    cur.execute(sql)
    rows = cur.fetchall()
    con.close()
    return [{'name': r[0], 'agency': r[1]} for r in rows]
