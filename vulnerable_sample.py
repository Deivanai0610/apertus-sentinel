import sqlite3

def login_user(username, password):
    # DANGER: Insecure SQL query vulnerable to SQL Injection!
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    return user

# Hardcoded credentials
admin_api_key = "YOUR_CSCS_API_KEY"