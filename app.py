from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["Get"])
def index_get():
    return render_template("index.html")


@app.route("/", methods=["Post"])
def index_post():
    message = request.form["message"]
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
