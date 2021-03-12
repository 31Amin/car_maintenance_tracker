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


@app.route("/add_record", methods=["GET", "POST"])
def add_record():

    cars = mongo.db.cars.find()
    garages = mongo.db.garage.find()
    return render_template("add_record.html", cars=cars, garages=garages)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
