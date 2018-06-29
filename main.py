from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', title = "SignUp")

@app.route("/", methods = ['POST'])
def validate_form():
    
    user = request.form["username"]
    password = request.form["password"]
    confirm = request.form["confirm"]
    email = request.form["email"]
    
    user_error = ""
    password_error = ""
    confirm_error = ""
    email_error = ""

    if user == "":
        user_error = "Field cannot be empty"
    elif len(user) > 3 or len(user) < 20:
        user_error = "Username must be between 3 and 20 characters"
    elif " " in user:
        user_error = "No spaces please"

    if password == "":
             password_error = "Field cannot be empty"
    elif len(password) > 3 or len(password) < 20:
        password_error = "Password must be between 3 and 20 characters"
    
    elif " " in password:
        password_error = "No spaces please"

    if confirm == "":
        confirm_error = "Field cannot be empty"

    elif confirm != password:
        confirm_error = "Passwords must match"
    
    elif len(email) > 3 or len(email) < 20:
        email_error = "Email must be between 3 and 20 characters"
    elif " " in email:
        email_error = "No spaces please"

    if not user_error and not password_error and not confirm_error and not email_error:
        return render_template('welcom.html')
    else:
        return render_template('index.html', 
        user_error = user_error, 
        password_error = password_error,
        confirm_error = confirm_error,
        email_error = email_error,
        user = user,
        password = password, 
        confirm = confirm, 
        email = email)

    
app.run()