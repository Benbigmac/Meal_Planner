from dbhandler import mealWizDB

# This script is here to help populate the database with relevant data if for some reason it is ever destroyed#or if I just need to create a new instance somewhere else I'lll have a default
#or if I just need to create a new instance somewhere else I'lll have a default
mwDB=mealWizDB()
mwDB.create_ratio('8:00', 'Breakfast', 0.116, 0.045, 0.08)
mwDB.create_ratio('12:00', 'Lunch', 0.116, 0.045, 0.08)
mwDB.create_foodtype( "Baking Goods")
mwDB.create_foodtype( "Bread")
mwDB.create_foodtype( "Cheese")
mwDB.create_foodtype( "Chips")
mwDB.create_foodtype( "Dairy")
mwDB.create_foodtype( "Drinks")
mwDB.create_foodtype( "Fruit")
mwDB.create_foodtype( "Fish")
mwDB.create_foodtype( "Meat")
mwDB.create_foodtype( "Pretzels")
mwDB.create_foodtype( "Spice")
mwDB.create_foodtype( "Vegetable")

#food data pulled from USDA nutrition website labels on food may say otherwise
mwDB.add_food_item(
    foodname="Ground Cinnamon",
    carbs=6.29,
    protein=0.3,
    fat=0.0,
    fiber=4.14,
    saturated_fat=0.0,
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=0.78,
    potassium=33.6,
    calcium=78.0,
    iron=0.6,
    vitamin_a=1.17,
    vitamin_c=0.3,
    vitamin_d=0.0,
    vitamin_k=2.4,
    magnesium=4.7,
    zinc=0.14,
    glycemic_index=0.0,
    glycemic_load=0.0,
    omega_3=0,
    omega_6=0,
    servingsize=7.8,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Spice')
) #ground Cinnamon #abberation: 7.6G ==1TBSP for serving size
mwDB.add_food_item(
    foodname="Salt",
    carbs=0.0,
    protein=0.0,
    fat=0.0,
    fiber=0.0,
    saturated_fat=0.0,
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=500.0,
    potassium=0.0,
    calcium=0.0,
    iron=0.0,
    vitamin_a=0.0,
    vitamin_c=0.0,
    vitamin_d=0.0,
    vitamin_k=0.0,
    magnesium=0.0,
    zinc=0.0,
    glycemic_index=0.0,
    glycemic_load=0.0,
    omega_3=0,
    omega_6=0,
    servingsize=1.2,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Spice')
) #salt
mwDB.add_food_item(
    foodname="Cumin Seed",
    carbs=2.65,
    protein=1.0,
    fat=1.0,
    fiber=0.63,
    saturated_fat=0.0,
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=10.1,
    potassium=107.0,
    calcium=55.9,
    iron=3.98,
    vitamin_a=3.48,
    vitamin_c=0.46,
    vitamin_d=0.0,
    vitamin_k=0.32,
    magnesium=22.0,
    zinc=0.28,
    glycemic_index=0.0,
    glycemic_load=0.0,
    omega_3=0,
    omega_6=0,
    servingsize=6.0,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Spice') )#cumin Seed

#White Pepper, Thyme, Parsley, Basil, Orgegano
mwDB.add_food_item(
    foodname="Apple",
    carbs=20.7,  # g
    protein=0.45,  # g
    fat=0.3,  # g
    fiber=3.6,  # g
    saturated_fat=0.045,  # g
    trans_fat=0.0,  # g
    cholesterol=0.0,  # mg
    sodium=1.5,  # mg
    potassium=160.5,  # mg
    calcium=9.0,  # mg
    iron=0.15,  # mg
    vitamin_a=2.4,  # µg
    vitamin_c=6.9,  # mg
    vitamin_d=0.0,  # µg
    vitamin_k=3.3,  # µg
    magnesium=7.5,  # mg
    zinc=0.06,  # mg
    glycemic_index=38.0,
    glycemic_load=9.0,
    omega_3=0.0,  # g
    omega_6=0.015,  # g
    servingsize=150.0,  # g
    servingsizeunit="grams",
    foodtype=mwDB.get_foodtype_id('Fruit')
)
mwDB.add_food_item(
    foodname="Carrots",
    carbs=10.3,
    protein=0.94,
    fat=0.35,
    fiber=2.8,
    saturated_fat=0.037,
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=87.0,
    potassium=320.0,
    calcium=30.0,
    iron=0.15,
    vitamin_a=835.0,
    vitamin_c=5.9,
    vitamin_d=0.0,
    vitamin_k=13.2,
    magnesium=12.0,
    zinc=0.0,
    glycemic_index=35.0,
    glycemic_load=3.4,
    omega_3=0,
    omega_6=0,
    servingsize=100.0,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Vegetable')
)
mwDB.add_food_item(
    foodname="raw Ground Beef 90% lean ",
    carbs=0.00,
    protein=18.2,
    fat=12.8,
    fiber=0.0,
    saturated_fat=5.05,
    trans_fat=0.0,
    cholesterol=66.0,
    sodium=62.0,
    potassium=2.0,
    calcium=7.0,
    iron=2.13,
    vitamin_a=0.0,
    vitamin_c=0.0,
    vitamin_d=0.0,
    vitamin_k=0.0,
    magnesium=16.5,
    zinc=4.19,
    glycemic_index=65.0,
    glycemic_load=65.0,
    omega_3=0.0,
    omega_6=0.0,
    servingsize=100.0,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Meat')
)
mwDB.add_food_item(
    foodname="Graulated Sugar",
    carbs=100.00,
    protein=0.0,
    fat=0.0,
    fiber=0.0,
    saturated_fat=0.0,
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=1.0,
    potassium=2.0,
    calcium=1.0,
    iron=0.01,
    vitamin_a=0.0,
    vitamin_c=0.0,
    vitamin_d=0.0,
    vitamin_k=0.0,
    magnesium=0.0,
    zinc=0.0,
    glycemic_index=65.0,
    glycemic_load=65.0,
    omega_3=0.0,
    omega_6=0.0,
    servingsize=100.0,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Baking Goods')
)
mwDB.add_food_item(
    foodname="Whole Milk",
    carbs=4.8,
    protein=3.4,
    fat=3.25,
    fiber=0.0,
    saturated_fat=1.865,
    trans_fat=0.0,
    cholesterol=14.0,
    sodium=44.0,
    potassium=132.0,
    calcium=125.0,
    iron=0.03,
    vitamin_a=46.0,
    vitamin_c=0.0,
    vitamin_d=0.05,
    vitamin_k=0.0,
    magnesium=12.0,
    zinc=0.38,
    glycemic_index=41.0,
    glycemic_load=2.0,
    omega_3=0.032,
    omega_6=0.092,
    servingsize=100.0,
    servingsizeunit="ml",
    foodtype=mwDB.get_foodtype_id('Dairy')
)
mwDB.add_food_item(
    foodname="Celery",
    carbs=2.97,
    protein=0.69,
    fat=0,
    fiber=1.6,
    saturated_fat=0,
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=80.0,
    potassium=260.0,
    calcium=40.0,
    iron=0.2,
    vitamin_a=22.0,
    vitamin_c=3.1,
    vitamin_d=0.0,
    vitamin_k=29.3,
    magnesium=11.0,
    zinc=0.13,
    glycemic_index=15.0,
    glycemic_load=0.4,
    omega_3=0.003,
    omega_6=0.002,
    servingsize=100.0,
    servingsizeunit="g",
    foodtype=mwDB.get_foodtype_id('Vegetable')
)
