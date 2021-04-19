from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def show_welcome():
    return "Welcome!"

@app.route('/welcome/home')
def show_welcome_home():
    return "Welcome Home!"

@app.route('/welcome/back')
def show_welcome_back():
    return "Welcome Back!"