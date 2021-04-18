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
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = mongo.db.directory.find_one(
            {"username": request.form.get("username").lower()})
        if user:
            if check_password_hash(
                user["password"], request.form.get
                    ("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "userprofile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/tracker")
def tracker():
    if session:
        if session["user"] == "admin":
            user_cars = list(mongo.db.cars.find())
            logs = list(mongo.db.maintenance.find().sort("service_date", -1))
            return render_template(
                "tracker.html", logs=logs, user_cars=user_cars)

        else:
            user_cars = list(mongo.db.cars.find(
                {"user": session["user"]}))
            logs = list(mongo.db.maintenance.find().sort("service_date", -1))
            return render_template(
                "tracker.html", logs=logs, user_cars=user_cars)

    flash("Login to site required")
    return redirect(url_for("login"))


@app.route("/detailed_record<record_id>")
def detailed_record(record_id):
    record = mongo.db.maintenance.find_one({"_id": ObjectId(record_id)})
    return render_template("detailed_record.html", record=record)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
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


# add a new maintenance record to the DB.
@app.route("/add_record", methods=["GET", "POST"])
def add_record():
    if request.method == "POST":
        car_details = mongo.db.cars.find_one(
            {"reg_no": request.form.get("reg_no")})
        make = car_details["make"]
        model = car_details["model"]

        garage_details = mongo.db.garage.find_one(
            {"garage_name": request.form.get("garage_name")})
        contact = garage_details["garage_contact"]
        phone = garage_details["garage_phone"]

        paid = "yes" if request.form.get("service_paid") else "no"

        details = {
            "reg_no": request.form.get("reg_no"),
            "username": session["user"],
            "service_date": request.form.get("service_date"),
            "service_cost": request.form.get("service_cost"),
            "service_desc": request.form.get("service_desc"),
            "service_paid": paid,
            "odometer_reading": request.form.get("odometer_reading"),
            "car_make": make,
            "car_model": model,
            "garage_name": request.form.get("garage_name"),
            "garage_contact": contact,
            "garage_phone": phone,
            "service_items": request.form.getlist("service_items")
        }

        mongo.db.maintenance.insert_one(details)
        flash("Maintenance recorded added")
        return redirect(url_for("tracker"))

    cars = mongo.db.cars.find({"user": session["user"]})
    garages = mongo.db.garage.find(
        {"garage_status": "active"}).sort("garage_name", 1)
    return render_template("add_record.html", cars=cars, garages=garages)


# edit a maintenance record.
@app.route("/edit_record<record_id>", methods=["GET", "POST"])
def edit_record(record_id):
    if request.method == "POST":
        print("test")
        car_details = mongo.db.cars.find_one(
            {"reg_no": request.form.get("reg_no")})
        make = car_details["make"]
        model = car_details["model"]

        garage_details = mongo.db.garage.find_one(
            {"garage_name": request.form.get("garage_name")})
        contact = garage_details["garage_contact"]
        phone = garage_details["garage_phone"]

        paid = "yes" if request.form.get("service_paid") else "no"

        edit_details = {
            "reg_no": request.form.get("reg_no"),
            "username": session["user"],
            "service_date": request.form.get("service_date"),
            "service_cost": request.form.get("service_cost"),
            "service_desc": request.form.get("service_desc"),
            "service_paid": paid,
            "odometer_reading": request.form.get("odometer_reading"),
            "car_make": make,
            "car_model": model,
            "garage_name": request.form.get("garage_name"),
            "garage_contact": contact,
            "garage_phone": phone,
            "service_items": request.form.getlist("service_items")

        }
        mongo.db.maintenance.update({"_id": ObjectId(record_id)}, edit_details)
        flash("Record Updated")
        return redirect(url_for("tracker"))

    cars = mongo.db.cars.find({"user": session["user"]})
    garages = mongo.db.garage.find(
        {"garage_status": "active"}).sort("garage_name", 1)

    record = mongo.db.maintenance.find_one({"_id": ObjectId(record_id)})

    return render_template(
        "edit_record.html", cars=cars, garages=garages, record=record)


# Page for user to add a new car.
@app.route("/addcar/<username>", methods=["GET", "POST"])
def addcar(username):
    active_user = mongo.db.directory.find_one(
        {"username": session["user"]})
    username = active_user["username"]
    email = active_user["email"]

    if request.method == "POST":
        already_registered = mongo.db.cars.find_one(
            {"reg_no": request.form.get("reg_no")})

        if already_registered:
            flash("A car with this reg #, already registered")
            return render_template(
                "addcar.html", username=username, email=email)

        car_details = {
            "reg_no": request.form.get("reg_no"),
            "user": username,
            "email": email,
            "make": request.form.get("make"),
            "model": request.form.get("model")
        }
        mongo.db.cars.insert_one(car_details)
        flash("Your car has been added to the database")

    return render_template("addcar.html", username=username, email=email)


# Functions for add gagrage page - add garage, activate / deactivate
@app.route("/add_garage", methods=["GET", "POST"])
def add_garage():
    if request.method == "POST":
        garage_exists = mongo.db.garage.find_one(
            {"garage_name": request.form.get("garage_name")})

        if garage_exists:
            flash("A garage with this name already exists in the DB")
            return redirect(url_for("add_garage"))

        garage_details = {
            "garage_name": request.form.get("garage_name"),
            "garage_contact": request.form.get("garage_contact"),
            "garage_phone": request.form.get("garage_phone"),
            "garage_status": "active"
            }
        mongo.db.garage.insert_one(garage_details)
        flash("Garage details added to the DB")
        return redirect(url_for("add_garage"))

    lst_garages = mongo.db.garage.find().sort("garage_name", 1)
    return render_template("add_garage.html", lst_garages=lst_garages)


# Deactivate Garage
@app.route("/deactivate_garage/<garage_id>")
def deactivate_garage(garage_id):
    mongo.db.garage.update(
        {"_id": ObjectId(garage_id)}, {"$set": {"garage_status": "inactive"}})
    flash("Selected garage set to inactive")
    return redirect(url_for("add_garage"))


# Activate Garage
@app.route("/activate_garage/<garage_id>")
def activate_garage(garage_id):
    mongo.db.garage.update(
        {"_id": ObjectId(garage_id)}, {"$set": {"garage_status": "active"}})
    flash("Selected garage set to active")
    return redirect(url_for("add_garage"))

# end add garage

# Log out & remove user session


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
