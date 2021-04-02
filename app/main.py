# Flask Library
from flask import Flask, render_template, request, session, redirect

# Flask Form Library
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

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

@app.route("/panel")
def panel():
    if "status" in session:
        return render_template("panel.html")
    else:
        return redirect("http://blackiq-neotrinost.fandogh.cloud")

# Render Login
@app.route("/login")
def login():
    if "status" in session:
        return redirect("http://blackiq-neotrinost.fandogh.cloud/panel")
    else:
        return render_template('login.html', login_form = LoginForm())

# Check Login
@app.route("/submit/", methods = ['POST'])
def submit():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == "Amirhossein" and password == "2003":
            session['status'] = True
            return redirect("http://blackiq-neotrinost.fandogh.cloud/panel")
        else:
            return render_template("error.html", context = ['User Error', 'Sorry, Username or Password is incorrect'])

# Logout
@app.route("/logout")
def logout():
    if "status" in session:
        session.pop('status', None)
        return redirect("http://blackiq-neotrinost.fandogh.cloud/login")
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