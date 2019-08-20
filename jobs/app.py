from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

app = Flask(__name__)

def open_connection():
    conection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.row
    return connection

def execute_sql(sql, value=(), commit=False, single=False):
    conection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        result = connection.commit()
    else:
        result = cursor.fetchone() if single else cursor.fetchall()

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
