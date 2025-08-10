import sqlite3

DB_NAME = "database.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     original_url TEXT NOT NULL,
                     short_code TEXT UNIQUE NOT NULL,
                     visit_count INTEGER DEFAULT 0
                    )
''')