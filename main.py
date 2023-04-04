import flask

app=flask.Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello</h1>"

@app.route("/loginpage")
def login():
    return flask.render_template("login.html")

if __name__=="__main__":
    app.run()
