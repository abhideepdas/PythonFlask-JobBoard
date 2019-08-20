from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')

def Jobs():
    return render_template('index.html')
