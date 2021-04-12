# Flask Library
from flask import Flask, render_template, request, session, redirect

# Flask Form Library
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


# MySQL
import mysql.connector

# MySQL -> Make Connection
# cnx = mysql.connector.connect( # On Working
#     host = "localhost", # On Working
#     user = "blackiq", # On Working
#     password = "blackiq", # On Working
#     database = "blackiq" # On Working
# ) # On Working

# MySQL -> Cursor
# cursor = cnx.cursor() # On Working

# MySQL -> Select Data Of User
# cursor.execute("SELECT * FROM user") # On Working

# MySQL -> Loop in cursot
# for (username, password) in cursor: # On Working
#     dbusername, dbpassword = username, password # On Working

dbusername, dbpassword = "username", "password"

# Flask Form -> Login
class LoginForm(FlaskForm):
    username = TextField(validators = [DataRequired()])
    password = PasswordField(validators = [DataRequired()])

# App Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"

# Route Index
@app.route("/")
def index():
    return render_template("index.html")

# MySQL -> Select Data For Jobs
# cursor.execute("SELECT * FROM jobs ORDER BY id DESC") # On Working

# MySQL -> Fetch All
# rows = cursor.fetchall()  # On Working

# Rendert Welcome
@app.route("/welcome")
def panel():
    if "status" in session:
        return render_template("welcome.html", context = rows)
    else:
        return redirect("/")

# Render Login
@app.route("/login")
def login():
    if "status" in session:
        return redirect("/welcome")
    else:
        return render_template('login.html', login_form = LoginForm())

# Check Login
@app.route("/submit/", methods = ['POST'])
def submit():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == dbusername and password == dbpassword:
            session['status'] = True
            return redirect("/welcome")
        else:
            return render_template("error.html", context = ['User Error', 'Sorry, Username or Password is incorrect'])

# Logout
@app.route("/logout")
def logout():
    if "status" in session:
        session.pop('status', None)
        return redirect("/login")
    else:
        return render_template("error.html", context = ['Your are logedin ?', 'Sorry, You are not logedin to logout right now'])

# 404 Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", context = ['404', '404 Page not found', 'Sorry, This page is not found'])

# 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error.html", context = ['405', '405 Method Not Allowed', 'The method is not allowed for the requested URL'])

# 400 Bad Request
@app.errorhandler(400)
def forbiden(error):
    return render_template("error.html", context = ['400', '400 Bad Request', 'Sorry, an error has occured, There is a bad requeste'])

# 500 Internal Server Error
@app.errorhandler(500)
def server(error):
    return render_template("error.html", context = ['500', '500 Internal Server Error', 'The server encountered an internal error and was unable to complete your request . Either the server is overloaded or there is an error in the application'])

# 502 Gateway Error
@app.errorhandler(502)
def other_server(error):
    return render_template("error.html", context = ['502', '502 Gateway Error', 'Sorry, Bad gateway'])

# Srcive Error
@app.errorhandler(503)
def crash_server(error):
    return render_template("error.html", context = ['503', '503 Service Error', 'Sorry, service is Unavailable'])

# Running App
if __name__ == "__main__":
    app.run()