from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/user/info", methods=["GET"])
def user_info():
    # 通过GET形式发过来的数据
    # print(request.args)
    # 可以使数据更加可视化
    user = request.args.get("姓名")
    password = request.args.get("密码")
    hobby = request.args.getlist("爱好")
    skill = request.args.get("擅长")
    city = request.args.get("所在城市")
    more = request.args.get("个人简历")
    print(user, password, hobby, skill, city, more)

    return "seccess rolling"
    # return render_template("user_info.html")


# 通过POST形式发过来的数据
""" @app.route("/user/info", methods=["POST"])
def user_info_post():
    print(request.form)
    return "seccess rolling"
    # 此方式提交不会再网页头显示提交的数据
      """


# 登录页面
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        return "seccess rolling"


if __name__ == "__main__":
    app.run(debug=True)
