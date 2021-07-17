# Flask Library
from flask import Flask, render_template

# App Configuration
app = Flask(__name__)

# Route Index
@app.route("/")
def index():
    return render_template("index.html")

# Running App
if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
