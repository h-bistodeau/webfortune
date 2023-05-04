from flask import (
        Flask, abort, jsonify, redirect, request, render_template, session, url_for
)

app = Flask(__name__)

import os
import subprocess

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    process = subprocess.run(['fortune'], stdout=subprocess.PIPE, universal_newlines=True)
    return 'Fortune: ' + process.stdout

@app.route('/cowsay/<message>/')
def cowsay(message):
    process = subprocess.run(['cowsay', message], stdout=subprocess.PIPE, universal_newlines=True)
    return '<pre>' + process.stdout + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    fprocess = subprocess.run(['fortune'], stdout=subprocess.PIPE, universal_newlines=True)
    cprocess = subprocess.run(['cowsay', fprocess.stdout], stdout=subprocess.PIPE, universal_newlines=True)
    return '<pre>' + str(cprocess.stdout) + '</pre>'
