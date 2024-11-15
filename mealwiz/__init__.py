import os, json
from flask import Flask, render_template
from .dbhandler import mealWizDB



def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='DEV',
            TEMPLATES_AUTO_RELOAD = True,
            DATABASE=os.path.join(app.instance_path,'mealwiz.sqlite'),
            )
    #from . import db
    #db.init_app(app)
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

    @app.route('/newMeal')
    def newmeal():
        mwDB=mealWizDB()
        ratios=mwDB.get_all_ratios()
        foodCategories=__getCategories()
        return render_template("newmeal.html",foodCategories=foodCategories,ratios=ratios)

    @app.route('/Updateratios')
    def ratios():
        mwDB=mealWizDB()
        ratios=mwDB.get_all_ratios()
        print(ratios)
        return render_template("ratioLibrary.html",ratios=ratios)

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



    #this function will be pinged by jquery to get the list of food items and their relevant data
    @app.route('/getcategorylist', methods=['GET'])
    def getcategorylist(category):
        foodlist=__getFoodCategoryList(category)
        return foodlist

    #helper function to go and access database to give what category food is in
    def __getCategories():
        categorylist=["fruit","Mcdonalds","Arbys","meat","vegetables","baking ingredients"]
        return categorylist

    #function to access database and return list of food items in category
    def __getFoodCategoryList(category):
        foodlist=['apple','banana','pear']
        return foodlist

    #access database and gets list of meal data (for front page)
    def __getMeals():
        return

    #helper function to help you calculate how many calories each meal or food item has
    def __calculate_Calories(carb,protein,fat):
        totalCal= (carb*4)+(protein*4)+(fat*9)
        return 0

    return app
