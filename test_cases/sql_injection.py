import sqlite3

def get_user_data(user_id):
    # Vulnerable to SQL Injection
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()