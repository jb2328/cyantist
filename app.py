from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    #return "Hello, Cyantist!"

@app.route("/test/")
@app.route("/test/<name>")
def test(name = None):
    return render_template(
        "test.html",
        name=name,
        date=datetime.now()
    )

if __name__ == '__main__':
    app.run()