import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
from dotenv import load_dotenv
load_dotenv()


# CONFIG 
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'original_fantasy_game'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


# ALL ROUTES
@app.route('/')
@app.route('/main_page')
def main_page():
    return render_template('main.html')

@app.route('/new_game')
def new_game():
    return render_template('new_game.html')


# CLASS ROUTES
@app.route('/get_classes')
def get_classes():
    return render_template('classes_list.html',
                            classes=mongo.db.classes.find(),
                            presetClasses=mongo.db.preset_classes.find())

@app.route('/create_class')
def create_class():
    return render_template('create_class.html',
                            newClassImages=mongo.db.class_images.find())

@app.route('/insert_class', methods=['POST'])
def insert_class():
    classes =  mongo.db.classes
    classes.insert_one(request.form.to_dict())
    return redirect(url_for('get_classes'))

@app.route('/edit_class/<class_id>')
def edit_class(class_id):
    
    return render_template('edit_class.html', 
                            aClass=mongo.db.classes.find_one({'_id': ObjectId(class_id)}))

@app.route('/update_class/<class_id>', methods=["POST"])
def update_class(class_id):
    classes = mongo.db.classes
    classes.update( {'_id': ObjectId(class_id)},
    {
        'class_name':request.form.get('class_name'),
        'class_information':request.form.get('class_information'),
        'class_stat_mod': request.form.get('class_stat_mod'),
        'class_image': request.form.get('class_image')
    })
    return redirect(url_for('get_classes'))

@app.route('/delete_class/<class_id>')
def delete_class(class_id):
    mongo.db.classes.remove({'_id': ObjectId(class_id)})
    return redirect(url_for('get_classes'))


# RACE ROUTES
@app.route('/get_races')
def get_races():
    return render_template('races_list.html', 
                            races=mongo.db.races.find(),
                            presetRaces=mongo.db.preset_races.find())

@app.route('/create_race')
def create_race():
    return render_template('create_race.html',
                            newRaceImages=mongo.db.race_images.find())

@app.route('/insert_race', methods=['POST'])
def insert_race():
    races =  mongo.db.races
    races.insert_one(request.form.to_dict())
    return redirect(url_for('get_races'))

@app.route('/edit_race/<race_id>')
def edit_race(race_id):
    return render_template('edit_race.html', 
                            race=mongo.db.races.find_one({'_id': ObjectId(race_id)}))

@app.route('/update_race/<race_id>', methods=["POST"])
def update_race(race_id):
    races = mongo.db.races
    races.update( {'_id': ObjectId(race_id)},
    {
        'race_name':request.form.get('race_name'),
        'race_information':request.form.get('race_information'),
        'race_stat_mod': request.form.get('race_stat_mod'),
        'race_image': request.form.get('race_image')
    })
    return redirect(url_for('get_races'))

@app.route('/delete_race/<race_id>')
def delete_race(race_id):
    mongo.db.races.remove({'_id': ObjectId(race_id)})
    return redirect(url_for('get_races'))


# CHARACTER ROUTES
@app.route('/get_characters')
def get_characters():
    return render_template('characters_list.html', 
                            characters=mongo.db.characters.find())

@app.route('/create_character')
def create_character():
    return render_template('create_character.html',
                            classes=mongo.db.classes.find(),
                            races=mongo.db.races.find(),
                            characters=mongo.db.characters.find(),
                            newCharacterImages=mongo.db.profile_images.find())

@app.route('/insert_character', methods=['POST'])
def insert_character():
    characters =  mongo.db.characters
    characters.insert_one(request.form.to_dict())
    return redirect(url_for('get_characters'))

@app.route('/edit_character/<character_id>')
def edit_character(character_id):
    return render_template('edit_character.html',
                            classes=mongo.db.classes.find(),
                            races=mongo.db.races.find(),
                            character=mongo.db.characters.find_one({'_id': ObjectId(character_id)}),
                            newCharacterImages=mongo.db.profile_images.find())
                            
@app.route('/update_character/<character_id>', methods=["POST"])
def update_character(character_id):
    characters = mongo.db.characters
    characters.update( {'_id': ObjectId(character_id)},
    {
        'character_name':request.form.get('character_name'),
        'character_information':request.form.get('character_information'),
        'gender':request.form.get('gender'),
        'class_choice': request.form.get('class_choice'),
        'race_choice': request.form.get('race_choice'),
        'profile_image': request.form.get('profile_image')
    })
    return redirect(url_for('get_characters'))

@app.route('/delete_character/<character_id>')
def delete_character(character_id):
    mongo.db.characters.remove({'_id': ObjectId(character_id)})
    return redirect(url_for('get_characters'))


# Game Routes
@app.route('/start_game')
def start_game():
    return render_template('start_game.html')

@app.route('/location_1')
def location_1():
    return render_template('location_1.html')

@app.route('/game_locations')
def game_locations():
    return render_template('game_locations.html',
                            locationImages=mongo.db.location_images)


# APP RUN
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

