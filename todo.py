# Commands to run - 
#     1. python -m venv venv
#     2. /venv/Scripts/activate
#     3. pip install -r /requirements.txt
#     4. python todo.py
#     5. hit on browser http://127.0.0.1:5000/health
import datetime
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return  'Web app with Python Flask'

app.run(host='0.0.0.0' , port=5000)


