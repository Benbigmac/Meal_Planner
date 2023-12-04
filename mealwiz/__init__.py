import os, json
from flask import Flask, render_template





def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='DEV',
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
        return render_template("base.html",ratioData=ratioData)

    @app.route('/Updateratios')
    def ratios():
        return render_template("ratioLibrary.html")

    def __getRatios():
        f = open('config/ratios.json')
        data = json.load(f)
        f.close()
        return data['list']

    def __getMeals():
        return

    return app
