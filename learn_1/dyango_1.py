from flask import Flask, render_template

app = Flask(__name__)


@app.route("/show/info")
def index():
    # return "中国蓝天"
    return render_template("mainweb.html")


@app.route("/get/web_1")
def web_1():
    return render_template("ancillary_web_1.html")


@app.route("/get/web_2")
def user_list():
    return render_template("user_list.html")


@app.route("/get/web_3")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
