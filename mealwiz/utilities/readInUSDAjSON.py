import json
from dbhandler import mealWizDB



def process_usda_items_to_mwdb(usda_items_raw, foodtype):
    # Parse the JSON string if input is a string
    mwDB=mealWizDB()
    if isinstance(usda_items_raw, str):
        usda_items = json.loads(usda_items_raw)
    else:
        usda_items = usda_items_raw
    print("am I here?")
    print(usda_items['description'])
        # Extracting nutrient values using nested structures
    nutrients = {}
    for nutrient in usda_items['foodNutrients']:
        if nutrient.get('nutrient'):
            nutrients[nutrient['nutrient']['name']] = nutrient.get('amount', 0.0)
    # Extracting serving size information
    serving_size = None
    serving_size_unit = None
    if 'foodMeasures' in item and item['foodMeasures']:
        serving_size = item['foodMeasures'][0].get('gramWeight', 0)
        serving_size_unit = item['foodMeasures'][0].get('measureUnitName', 'g')
    if "Flour" in ''.join(usda_items['description'].split(',')):
        foodtype="Baking Goods"
    mwDB.add_food_item(
        foodname=''.join(usda_items['description'].split(',')),
        carbs=nutrients.get('Carbohydrate, by difference', 0.0),
        protein=nutrients.get('Protein', 0.0),
        fat=nutrients.get('Total lipid (fat)', 0.0),
        fiber=nutrients.get('Fiber, total dietary', 0.0),
        saturated_fat=nutrients.get('Fatty acids, total saturated', 0.0),
        trans_fat=nutrients.get('Fatty acids, total trans', 0.0),
        cholesterol=nutrients.get('Cholesterol', 0.0),
        sodium=nutrients.get('Sodium, Na', 0.0),
        potassium=nutrients.get('Potassium, K', 0.0),
        calcium=nutrients.get('Calcium, Ca', 0.0),
        iron=nutrients.get('Iron, Fe', 0.0),
        vitamin_a=nutrients.get('Vitamin A, RAE', 0.0),
        vitamin_c=nutrients.get('Vitamin C, total ascorbic acid', 0.0),
        vitamin_d=nutrients.get('Vitamin D (D2 + D3)', 0.0),
        vitamin_k=nutrients.get('Vitamin K (phylloquinone)', 0.0),
        magnesium=nutrients.get('Magnesium, Mg', 0.0),
        zinc=nutrients.get('Zinc, Zn', 0.0),
        glycemic_index=0.0,
        glycemic_load=0.0,
        omega_3=0.0,
        omega_6=0.0,
        servingsize= 100.0, #wasted time parsing serving size since all the usda info is based around 100g
        servingsizeunit= "g",
        foodtype=mwDB.get_foodtype_id(foodtype)
    )


# Specify the path to the JSON file
file_path = ["Spice.json","Vegetable.json", "Fruit.json", "Meat.json"]


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
try:
    # Open the file and load its contents
    for foodList in file_path:
        print(foodList)
        print(str(foodList).split('.')[0])
        with open(foodList, 'r') as file:
            data = json.load(file)
            for item in data:
                print(''.join(item['description']))
                process_usda_items_to_mwdb(item, str(foodList).split('.')[0])
                #name
                print(''.join(item['description']))
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from the file '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
