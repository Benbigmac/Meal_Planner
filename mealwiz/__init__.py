import os, json
from flask import Flask, render_template,request, jsonify
from .dbhandler import mealWizDB
from .forms import addFood
from flask_bootstrap import Bootstrap
from flask_cors import CORS

from flask_wtf import FlaskForm, CSRFProtect


def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    # Bootstrap-Flask requires this line
    bootstrap = Bootstrap(app)
    CORS(app)
    # Flask-WTF requires this line
    csrf = CSRFProtect(app)
    app.config.from_mapping(
            SECRET_KEY='DEV',
            TEMPLATES_AUTO_RELOAD = True,
            DATABASE=os.path.join(app.instance_path,'mealwiz.sqlite'),
            )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    @app.route('/')
    def entrance():
        mwDB=mealWizDB()
        ratios=mwDB.get_all_ratios()
        return render_template("meallist.html",ratios=ratios, meals={})


    @app.route('/newFood')
    def newFood():
        form = addFood()
        return render_template('addfood.html', form=form)

    @app.route('/newMeal')
    def newmeal():
        mwDB=mealWizDB()
        ratios=mwDB.get_all_ratios()
        foodCategories=__getCategories()
        print(foodCategories.sort())
        print(foodCategories)
        return render_template("newmeal.html",foodCategories=foodCategories,ratios=ratios,__getFoodCategoryList=__getFoodCategoryList)

    @app.route('/Updateratios')
    def ratios():
        mwDB=mealWizDB()
        ratios=mwDB.get_all_ratios()
        print(ratios)
        return render_template("ratioLibrary.html",ratios=ratios)

    @app.route('/getcategorylist', methods=['POST'])
    def createMeal():
        try:
            data = request.get_json()

            mealtime = data.get('mealtime', datetime.now().isoformat())

            mwDB=mealWizDB()
            meal_code=mwDB.create_meal(mealtime)
            for food_id in food_ids:
                db.add_food_to_meal(meal_code, food_id)
        except Exception as e:
        return jsonify({"error": str(e)}), 500

    @app.route('/test')
    def rest():


        return render_template("test.html")

    @app.route('/create_new_ratio')
    def create_newratio():
        return render_template("create_new_ratio.html")

    @app.route('/addRatio')
    def create_add_ratio():
        mwDB=mealWizDB()
        #mwDB.create_ratio('12:00', 'Lunch', 0.116, 0.045, 0.08)
        return mwDB.get_all_ratios()

    @app.route('/initList')
    def create_add_list():
        mwDB=mealWizDB()
        return sorted(mwDB.get_all_food_categories())

    #this function will be pinged by jquery to get the list of food items and their relevant data
    @csrf.exempt
    @app.route('/getcategorylist', methods=['POST'])
    def getcategorylistfunction():
        print(request.data)
        try:
            data = request.get_json()
            category = data.get('key')
            foodlist=__getFoodCategoryList(category)

            return sorted(foodlist)
        except Exception as e:
            print("Error:", e)
            return jsonify({"status": "error", "message": str(e)}), 500


    @csrf.exempt
    @app.route('/getFoodInfo', methods=['POST'])
    def getFoodInfo():
        try:
            data = request.get_json()
            category = data.get('key')
            print(category)
            food=__getFood(category)
            return food
        except Exception as e:
            print("Error:", e)
            return jsonify({"status": "error", "message": str(e)}), 500

    #function to access database and return list of food items in category
    def __getFoodCategoryList(category):
        mwDB=mealWizDB()
        print(category)
        id=mwDB.get_foodtype_id(category)
        return mwDB.get_food_name_list_by_type(id)

    #helper function to go and access database to give what category food is in
    def __getCategories():
        mwDB=mealWizDB()
        return sorted(mwDB.get_all_food_categories())

    def __getFood(name):
        mwDB=mealWizDB()
        print(name)
        return mwDB.get_food_by_name(name)

    #access database and gets list of meal data (for front page)
    def __getMeals():
        return

    #helper function to help you calculate how many calories each meal or food item has
    def __calculate_Calories(carb,protein,fat):
        totalCal= (carb*4)+(protein*4)+(fat*9)
        return totalCal

    return app
