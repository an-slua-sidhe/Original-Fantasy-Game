import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'original_fantasy_game'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://polocoinn:Ansluasidhe2@myfirstcluster-c89ie.mongodb.net/original_fantasy_game?retryWrites=true&w=majority')

mongo = PyMongo(app)

@app.route('/')
@app.route('/main_page')
def main_page():
    return render_template('main.html')

@app.route('/new_game')
def new_game():
    return render_template('new_game.html')


@app.route('/get_classes')
def get_classes():
    return render_template('classes_list.html', classes=mongo.db.classes.find())

@app.route('/create_class')
def create_class():
    return render_template('create_class.html')

@app.route('/insert_class', methods=['POST'])
def insert_class():
    classes =  mongo.db.classes
    classes.insert_one(request.form.to_dict())
    return redirect(url_for('get_classes'))



@app.route('/get_races')
def get_races():
    return render_template('races_list.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            # Do not use 'debug=True' in actual applications, only when testing!
            debug=True)