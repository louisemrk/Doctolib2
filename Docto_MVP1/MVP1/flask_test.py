from flask import Flask
app = Flask(__name__)
from MVP1.actualisation import *

@app.route('/')
def hello_world():
    html = code_html("candidat_internet.html");

    return html
