from flask import Flask, redirect, request, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from os import path
if path.exists("env.py"):
    import env



app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template(
            'index.html',
            recipes=mongo.db.recipes.find(),
            products=mongo.db.products.find()
        )


@app.route('/get_all_recipes')
def get_all_recipes():
    return render_template(
        'all-recipes.html',
        recipes=mongo.db.recipes.find()
    )


@app.route('/whole_recipe/<recipe_id>')
def whole_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'whole-recipe.html',
        recipe=the_recipe,
        products=mongo.db.products.aggregate([{'$sample': {'size': 3}}])
    )


@app.route('/add_recipe')
def add_recipe():
    """
        Used to render add recipe form
    """
    return render_template('add-recipe.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """
       Insert new recipe into database
    """
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_all_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """
        Used to render edit recipe form
    """
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'edit-recipe.html',
        recipe=the_recipe
    )


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """
        Updates the edited recipe in the database
    """
    mongo.db.recipes.replace_one(
        {'_id': ObjectId(recipe_id)},
        {
            'recipe_title': request.form.get('recipe_title'),
            'serving_size': request.form.get('serving_size'),
            'ingredients': request.form.get('ingredients'),
            'procedure': request.form.get('procedure'),
            'image_url': request.form.get('image_url')
        }
    )
    return redirect(url_for('whole_recipe', recipe_id=recipe_id))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_all_recipes'))


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
