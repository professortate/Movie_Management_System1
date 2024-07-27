from flask import Flask, render_template
import sqlite3
import os
print("Current working directory:", os.getcwd())
print("Does 'templates' folder exist?", os.path.exists('templates'))
print("Contents of current directory:", os.listdir())
if os.path.exists('templates'):
    print("Contents of 'templates' folder:", os.listdir('templates'))
else:
    print("'templates' folder not found!")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('movie1.db')
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
    app.run(debug=True)