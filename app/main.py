# Flask Library
from flask import Flask, render_template

# App Configuration
app = Flask(__name__)


# Route Index
@app.route("/")
def index():
    return "Welcome!"
