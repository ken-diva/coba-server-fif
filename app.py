from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Coba server!"


@app.route("/route_baru")
def route_baru():
    return "Coba route baru!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)
