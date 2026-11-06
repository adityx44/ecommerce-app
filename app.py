from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from services.auth import register
from services.auth import login

from services.product import get_products

app = Flask(__name__)

app.secret_key = "secret123"


@app.route("/")
def home():
    return redirect("/login")


@app.route("/register",
methods=["GET","POST"])
def register_user():

    if request.method=="POST":

        username=request.form["username"]
        password=request.form["password"]

        register(username,password)

        return redirect("/login")

    return render_template("register.html")


@app.route("/login",
methods=["GET","POST"])
def login_user():

    if request.method=="POST":

        username=request.form["username"]
        password=request.form["password"]

        user_id=login(
            username,
            password
        )

        if user_id:

            session["user_id"]=user_id

            return redirect("/products")

    return render_template("login.html")


@app.route("/products")
def products():

    items = get_products()

    return render_template(
        "products.html",
        products=items.to_dict(
            orient="records"
        )
    )


if __name__=="__main__":
    app.run(debug=True)