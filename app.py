from flask import Flask, render_template, Request, url_for

class R(Request):
    # Whitelist your SRCF and/or custom domains to access the site via proxy.
    trusted_hosts = {"jb2328.user.srcf.net", "cyantist.xyz"}

app = Flask(__name__)
app.request_class = R

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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()