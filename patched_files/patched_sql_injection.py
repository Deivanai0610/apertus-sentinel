import sqlite3

def get_user_data(user_id):
    # Secure implementation using parameterized query
    query = "SELECT * FROM users WHERE id = ?"
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query, (user_id,))
    return cursor.fetchone()