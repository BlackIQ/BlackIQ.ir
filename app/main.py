# Flask Library
from flask import Flask, render_template

# App Configuration
app = Flask(__name__)


# Route Index
@app.route("/")
def index():
    return render_template("index.html")


# 404 Error
@app.errorhandler(404)
def page_not_found(error):
    return "<p>Sorry 404 Page not found. Amirhossein Mohammadi</p>"


# 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    return "<p>Sorry 405 The method is not allowed for the requested URL. Amirhossein Mohammadi</p>"


# 400 Bad Request
@app.errorhandler(400)
def forbiden(error):
    return render_template("Error/error.html",
                           context=['400', '400 Bad Request', 'Sorry, an error has occured, There is a bad requeste'])


# 500 Internal Server Error
@app.errorhandler(500)
def server(error):
    return render_template("Error/error.html", context=['500', '500 Internal Server Error',
                                                        'The server encountered an internal error and was unable to complete your request . Either the server is overloaded or there is an error in the application'])


# 502 Gateway Error
@app.errorhandler(502)
def other_server(error):
    return render_template("Error/error.html", context=['502', '502 Gateway Error', 'Sorry, Bad gateway'])


# Srcive Error
@app.errorhandler(503)
def crash_server(error):
    return render_template("Error/error.html", context=['503', '503 Service Error', 'Sorry, service is Unavailable'])


# Running App
if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
