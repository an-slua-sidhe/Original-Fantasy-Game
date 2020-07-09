import os
from flask import Flask, render_template, redirect, request, url_for, request
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId

app = Flask(__name__)
# app.config["MONGO_DBNAME"] = '??'
# app.config["MONGO_URI"] = os.getenv('MONGO_URI', '??')

# mongo = PyMongo(app)

@app.route('/')
def main_page():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            # Do not use 'debug=True' in actual applications, only when testing, like here! :)
            debug=True)