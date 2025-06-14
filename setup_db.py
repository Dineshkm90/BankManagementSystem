import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        name TEXT,
        email TEXT,
        password TEXT,
        account_number TEXT UNIQUE,
        balance REAL DEFAULT 0
    )
''')

# Transactions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT,
        amount REAL,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

conn.commit()
conn.close()
print("✅ Database created successfully.")
