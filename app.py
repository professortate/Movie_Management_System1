from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    # Use absolute path to ensure database is found in production
    db_path = os.path.join(os.path.dirname(__file__), 'movie1.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    movies = conn.execute('''
        SELECT m.Movie_ID, m.Movie_Name, m.Release_Date, d.Director_Name, 
               GROUP_CONCAT(c.Cast_Name, ', ') AS Casts, md.Budget, md.Duration, md.Rating
        FROM Movies m
        LEFT JOIN MovieDetails md ON m.Movie_ID = md.Movie_ID
        LEFT JOIN Directors d ON md.Director_ID = d.id
        LEFT JOIN MovieCasts mc ON m.Movie_ID = mc.Movie_ID
        LEFT JOIN Casts c ON mc.Cast_ID = c.id
        GROUP BY m.Movie_ID
    ''').fetchall()
    conn.close()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    # For production deployment - use environment variable for port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
