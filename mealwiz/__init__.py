import os, json
from flask import Flask, render_template




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
        ratioData=__getRatios()
        return render_template("meallist.html",ratioData=ratioData)

    @app.route('/newMeal')
    def newmeal():
        ratioData=__getRatios()
        foodCategories=__getCategories()
        return render_template("newmeal.html",foodCategories=foodCategories,ratioData=ratioData)

    @app.route('/Updateratios')
    def ratios():
        return render_template("ratioLibrary.html")

    def __getRatios():
        f = open('/home/benbigmac/Documents/mealwizard/mealwiz/config/ratios.json')
        data = json.load(f)
        f.close()
        return data['list']

    @app.route('/getcategorylist',methods=['GET'])
    def getcategorylist(category):
        foodlist=__getFoodCategoryList(category)
        return foodlist

    def __getCategories():
        categorylist=["fruit","Mcdonalds","Arbys","meat","vegetables","baking ingredients"]
        return categorylist

    def __getMeals():
        return

    def __getFoodCategoryList(category):
        foodlist=['apple','banana','pear']
        return foodlist

    return app
