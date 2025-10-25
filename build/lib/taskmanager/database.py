import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT DEFAULT 'Add Description',
            status TEXT DEFAULT 'todo',
            createdAT TEXT DEFAULT CURRENT_TIMESTAMP,
            updatedAt  TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task_name):
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO tasks (title) VALUES (?, ?)
                   ''',(task_name))
    conn.commit()
    conn.close()




#runfirst
create_table()