from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """

    <h1>Hello World</h1>
    <p>I'm Geuun</p>

    """

if __name__ == "__main__":
    app.run(debug = True)