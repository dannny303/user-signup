from flask import Flask, render_template, request, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

@app.route("/")
def index():
    return render_template('index.html', title = "SignUp")



app.run()