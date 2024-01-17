from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Coba tes route pakai ini!"


@app.route("/tes")
def tes():
    return "Coba route baru!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)
