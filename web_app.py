from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, roll_number, bio FROM users LIMIT 1;")
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return f"""
        <h1>{user[0]}</h1>
        <h2>Roll Number: {user[1]}</h2>
        <p>{user[2]}</p>
        """
    else:
        return "<h3>No user data found in database</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
