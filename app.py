import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")


@app.route("/tracker")
def tracker():
    logs = list(mongo.db.maintenance.find())
    return render_template("tracker.html", logs=logs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("Im running")
        user_taken = mongo.db.directory.find_one(
            {"username": request.form.get("username").lower()})

        if user_taken:
            flash("Selected username is already assigned")
            return redirect(url_for("register"))

        register = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        print(register)
        mongo.db.directory.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("userprofile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.directory.find_one(
            {"username": request.form.get("username").lower()})
        name =  existing_user["name"]

        if existing_user:
            if check_password_hash(
            existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("userprofile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/userprofile/<username>", methods=["GET", "POST"])
def userprofile(username):
    active_user = mongo.db.directory.find_one(
        {"username": session["user"]})
    username = active_user["username"]
    name = active_user["name"]
    email = active_user["email"]

    if session["user"]:
        return render_template(
            "userprofile.html", username=username, name=name, email=email)

    return redirect(url_for("login"))


@app.route("/add_record", methods=["GET", "POST"])
def add_record():
    cars = mongo.db.cars.find()
    garages = mongo.db.garage.find()
    return render_template("add_record.html", cars=cars, garages=garages)


@app.route("/addcar/<username>", methods=["GET", "POST"])
def addcar(username):
    active_user = mongo.db.directory.find_one(
        {"username": session["user"]})
    username = active_user["username"]
    email = active_user["email"]

    if request.method == "POST":
        already_registered = mongo.db.cars.find_one(
            {"reg_no":request.form.get("reg_no")})

        if already_registered:
            flash("A car with this registration number is already registered in the database.")
            return render_template("addcar.html", username=username, email=email)

        car_details = {
            "reg_no":request.form.get("reg_no"),
            "user":request.form.get("username"),
            "email":request.form.get("email"),
            "make":request.form.get("make"),
            "model":request.form.get("model")
        }
        mongo.db.cars.insert_one(car_details)
        flash("Your car has been added to the database")

    return render_template("addcar.html", username=username, email=email)

# Functions for add gagrage page - add garage, activate / deactivate
@app.route("/add_garage", methods=["GET", "POST"])
def add_garage():
    if request.method == "POST":
        garage_details ={
            "garage_name":request.form.get("garage_name"),
            "garage_contact":request.form.get("garage_contact"),
            "garage_phone":request.form.get("garage_phone"),
            "garage_status":"active"
            }
        mongo.db.garage.insert_one(garage_details)
        flash("Garage details added to the DB")
        return redirect(url_for("add_garage"))

    lst_garages = mongo.db.garage.find().sort("garage_name", 1)
    return render_template("add_garage.html", lst_garages=lst_garages)


@app.route("/deactivate_garage/<garage_name>", methods=["POST"])
def deactivate_garage(garage_name):
    lst_garages = mongo.db.garage.find().sort("garage_name", 1)
    print ("running")
    return render_template("add_garage.html", lst_garages=lst_garages)

# end add garage 

@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
