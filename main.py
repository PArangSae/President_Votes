from flask import Flask
import flask
app = Flask('app')
import os

@app.route('/')
def index():
    return flask.render_template('index.html', API_KEY = os.environ["API_KEY"])

app.run(host='0.0.0.0', port=8080)