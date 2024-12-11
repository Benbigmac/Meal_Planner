import sqlite3
import os
from typing import List, Tuple, Optional
import json




class mealWizDB:
    DB_NAME=''

    def __init__(self, db_name='/../mealWiz.db'):
         print("db helper initialized")
         basedir = os.path.abspath(os.path.dirname(__file__))
         print(basedir)
         self.DB_NAME = basedir+db_name
         print(self.DB_NAME)

    def connect_db(self):
        """Connect to the SQLite database."""
        conn = sqlite3.connect(self.DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn


    def add_food_item(self, foodname, carbs, protein, fat, fiber, saturated_fat, trans_fat, cholesterol,
                      sodium, potassium, calcium, iron, vitamin_a, vitamin_c, vitamin_d, vitamin_k,
                      magnesium, zinc, glycemic_index, glycemic_load, omega_3, omega_6, servingsize,
                      servingsizeunit, foodtype):
        """
        Adds a food item to the food table in the SQLite database.

        Parameters:
            db_path (str): Path to the SQLite database file.
            foodname (str): Name of the food item.
            carbs (float): Amount of carbohydrates in grams.
            protein (float): Amount of protein in grams.
            fat (float): Amount of fat in grams.
            fiber (float): Amount of fiber in grams.
            saturated_fat (float): Amount of saturated fat in grams.
            trans_fat (float): Amount of trans fat in grams.
            cholesterol (float): Amount of cholesterol in milligrams.
            sodium (float): Amount of sodium in milligrams.
            potassium (float): Amount of potassium in milligrams.
            calcium (float): Amount of calcium in milligrams.
            iron (float): Amount of iron in milligrams.
            vitamin_a (float): Amount of vitamin A in micrograms.
            vitamin_c (float): Amount of vitamin C in milligrams.
            vitamin_d (float): Amount of vitamin D in micrograms.
            vitamin_k (float): Amount of vitamin K in micrograms.
            magnesium (float): Amount of magnesium in milligrams.
            zinc (float): Amount of zinc in milligrams.
            glycemic_index (float): Glycemic index value.
            glycemic_load (float): Glycemic load value.
            omega_3 (float): Amount of omega-3 fatty acids in grams.
            omega_6 (float): Amount of omega-6 fatty acids in grams.
            servingsize (float): Serving size amount.
            servingsizeunit (str): Unit of serving size (e.g., grams, cups).
            foodtype (int): ID of the food type (foreign key).

        Returns:
            bool: True if insertion is successful, False otherwise.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()

            query = """
            INSERT INTO food (
                foodname, carbs, protein, fat, fiber, saturated_fat, trans_fat, cholesterol, sodium, potassium,
                calcium, iron, vitamin_a, vitamin_c, vitamin_d, vitamin_k, magnesium, zinc, glycemic_index,
                glycemic_load, omega_3, omega_6, servingsize, servingsizeunit, foodtype
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(query, (
                foodname, carbs, protein, fat, fiber, saturated_fat, trans_fat, cholesterol, sodium, potassium,
                calcium, iron, vitamin_a, vitamin_c, vitamin_d, vitamin_k, magnesium, zinc, glycemic_index,
                glycemic_load, omega_3, omega_6, servingsize, servingsizeunit, foodtype
            ))
            conn.commit()

    def get_foodtype_id(self, typename):
        """
        Get the ID of a food type based on its name.

        Args:
            typename (str): The name of the food type.

        Returns:
            int or None: The ID of the food type, or None if not found.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            # Query to fetch the food type ID
            query = "SELECT id FROM foodtypes WHERE typename = ?"
            cursor.execute(query, (typename,))
            result = cursor.fetchone()
            # Return the ID if found, otherwise None
            return result[0] if result else None


    def get_all_food_categories(self):
        """
        Retrieve all food categories from the database.
        Returns:
            list of tuples: A list of all food categories (id, typename).
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, typename FROM foodtypes")
            categories = [row[1] for row in cursor.fetchall()]
            return categories



    def create_foodtype(self, typename: str):
        """Insert a new food type into the foodtypes table."""
        query = '''
        INSERT INTO foodtypes (typename)
        VALUES (?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (typename,))
            conn.commit()

    def create_meal(self, mealtime: str, totalcarbs: float, totalfat: float, totalprotein: float, ratios: int) -> int:
        """
        Insert a new meal into the Meals table and return the generated meal_code.
        """
        query = '''
        INSERT INTO Meals (mealtime, totalcarbs, totalfat, totalprotein, ratios)
        VALUES (?, ?, ?, ?, ?)
        '''
        with self.connect_db() as conn:
            cursor = conn.execute(query, (mealtime, totalcarbs, totalfat, totalprotein, ratios))
            conn.commit()
            return cursor.lastrowid  # Get the generated ID


    def add_food_to_meal(self, meal_code: int, food_id: int, amount: float, unit: str):
        """
        Link a food item to a meal with its amount and unit.
        """
        query = '''
        INSERT INTO MealFoodItems (meal_code, food_id, amount, unit)
        VALUES (?, ?, ?, ?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (meal_code, food_id, amount, unit))
            conn.commit()

    def get_total_meals(self):
        query = "SELECT COUNT(*) AS total FROM Meals;"
        with self.connect_db() as conn:
            result = conn.execute(query).fetchone()
        return result[0]


    def get_paginated_meals(self, per_page: int, offset: int):
        """
        Retrieves paginated meal data, including food names and calculated total calories.
        """
        query = '''
        SELECT
            Meals.code AS meal_code,
            DATE(Meals.mealtime) AS meal_date,
            TIME(Meals.mealtime) AS meal_time,
            GROUP_CONCAT(Food.foodname, ', ') AS food_names,
            Meals.totalcarbs AS total_carbs,
            Meals.totalfat AS total_fat,
            Meals.totalprotein AS total_protein,
            (Meals.totalcarbs * 4 + Meals.totalprotein * 4 + Meals.totalfat * 9) AS total_calories
        FROM Meals
        LEFT JOIN MealFoodItems ON Meals.code = MealFoodItems.meal_code
        LEFT JOIN Food ON MealFoodItems.food_id = Food.id
        GROUP BY Meals.code
        ORDER BY Meals.mealtime DESC
        LIMIT ? OFFSET ?;
        '''
        with self.connect_db() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(query, (per_page, offset))
            results = cursor.fetchall()

        return [
            {
                "meal_code": row["meal_code"],
                "meal_date": row["meal_date"],
                "meal_time": row["meal_time"],
                "food_names": row["food_names"],
                "total_carbs": row["total_carbs"],
                "total_fat": row["total_fat"],
                "total_protein": row["total_protein"]
            }
            for row in results
        ]

    def create_restaurant(code: int, name: str):
        """Insert a new restaurant into the restaurants table."""
        query = '''
        INSERT INTO restaurants (code, name)
        VALUES (?, ?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (code, name))
            conn.commit()

    def add_food_to_restaurant(restaurant_code: int, food_id: int):
        """Link a food item to a restaurant in the RestaurantFoodItems table."""
        query = '''
        INSERT INTO RestaurantFoodItems (restaurant_code, food_id)
        VALUES (?, ?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (restaurant_code, food_id))
            conn.commit()

    def get_food_by_name(self, food_name: str) -> Optional[Tuple]:
        with self.connect_db() as conn:
            try:
        # Connect to the database
                cursor = conn.cursor()
                query = "SELECT * FROM food WHERE LOWER(foodname) = LOWER(?)"

                # Execute the query with the provided food name
                cursor.execute(query, (food_name,))
                results = cursor.fetchall()
                print(results)
                return results

            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return []

    def get_meals_with_food(food_id: int) -> List[Tuple]:
        """Retrieve all meals that include a specific food item."""
        query = '''
        SELECT Meals.* FROM Meals
        JOIN MealFoodItems ON Meals.code = MealFoodItems.meal_code
        WHERE MealFoodItems.food_id = ?
        '''
        with self.connect_db() as conn:
            results = conn.execute(query, (food_id,)).fetchall()
        return results

    def update_food_carbs(food_id: int, new_carbs: float):
        """Update the carbs content of a food item."""
        query = '''
        UPDATE food SET carbs = ? WHERE id = ?
        '''
        with self.connect_db() as conn:
            conn.execute(query, (new_carbs, food_id))
            conn.commit()

    def delete_meal(meal_code: int):
        """Delete a meal from the Meals table."""
        query = '''
        DELETE FROM Meals WHERE code = ?
        '''
        with self.connect_db() as conn:
            conn.execute(query, (meal_code,))
            conn.commit()

    def list_foods_in_meal(meal_code: int) -> List[Tuple]:
        """List all food items in a specific meal."""
        query = '''
        SELECT food.* FROM food
        JOIN MealFoodItems ON food.id = MealFoodItems.food_id
        WHERE MealFoodItems.meal_code = ?
        '''
        with self.connect_db() as conn:
            results = conn.execute(query, (meal_code,)).fetchall()
        return results


    def get_all_ratios(self):
        """
        Retrieve all ratios from the ratios table.

        Returns:
            list: A list of tuples where each tuple represents a row from the ratios table.
        """
        query = '''
        SELECT * FROM ratios
        '''
        with self.connect_db() as conn:
            result = conn.execute(query).fetchall()
        return result

    def create_ratio(self, time: str, name: str, carbratio: float, proteinratio: float, fatratio: float):
        """
        Insert a new ratio into the ratios table.
        Args:
            time (str): The time in 'HH:MM' format.
            name (str): A descriptive name for the ratio.
            carbratio (float): The carbohydrate ratio.
            proteinratio (float): The protein ratio.
            fatratio (float): The fat ratio.
        """
        query = '''
        INSERT INTO ratios (time, name, carbratio, proteinratio, fatratio)
        VALUES (?, ?, ?, ?, ?)
        '''
        print(query)
        with self.connect_db() as conn:
            conn.execute(query, (time, name, carbratio, proteinratio, fatratio))
            conn.commit()

    def get_ratio_by_time(self, time: str) -> Optional[Tuple]:
        """
        Retrieve a ratio by exact time.

        Args:
            time (str): The exact time in 'HH:MM' format.

        Returns:
            Optional[Tuple]: The row from the ratios table if found, otherwise None.
        """
        query = '''
        SELECT * FROM ratios WHERE time = ?
        '''
        with self.connect_db() as conn:
            result = conn.execute(query, (time,)).fetchone()
        return result

    def get_food_name_list_by_type(self, foodtype_id):
        """
        Retrieve all food items linked to a specific food type and return as list.

        Args:
            foodtype_id (int): The ID of the food type.

        Returns:
            str: A List of strings containing the food items linked to the food type.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, foodname
                FROM food
                WHERE foodtype = ?
            """, (foodtype_id,))
            food_items = cursor.fetchall()
            list=[]
            for item in food_items:
                list.append(item[1])
            return list



    def get_food_by_type_json(self, foodtype_id):
        """
        Retrieve all food items linked to a specific food type and return as JSON.

        Args:
            foodtype_id (int): The ID of the food type.

        Returns:
            str: A JSON string containing the food items linked to the food type.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, foodname, carbs, protein, fat, servingsize, servingsizeunit
                FROM food
                WHERE foodtype = ?
            """, (foodtype_id,))
            food_items = cursor.fetchall()

            # Convert to a list of dictionaries for JSON output
            food_list = [
                {
                    "id": row[0],
                    "foodname": row[1],
                    "carbs": row[2],
                    "protein": row[3],
                    "fat": row[4],
                    "servingsize": row[5],
                    "servingsizeunit": row[6]
                }
                for row in food_items
            ]

            return json.dumps(food_list, indent=2)  # Convert to JSON string with pretty formatting


    def get_ratio_by_nearest_time(self, input_time: str) -> Optional[Tuple]:
        """
        Retrieve the ratio closest to the specified time (input in 'HH:MM' format).

        Args:
            input_time (str): The time in 'HH:MM' format to find the closest ratio for.

        Returns:
            Optional[Tuple]: The row from the ratios table that has the closest time to input_time.
        """
        query = '''
        SELECT * FROM ratios
        ORDER BY ABS(strftime('%H', time) * 60 + strftime('%M', time) -
                     (strftime('%H', ?) * 60 + strftime('%M', ?))) ASC
        LIMIT 1
        '''
        with self.connect_db() as conn:
            result = conn.execute(query, (input_time, input_time)).fetchone()
        return result

    def update_ratio(self, time: str, new_carbratio: Optional[float] = None, new_proteinratio: Optional[float] = None, new_fatratio: Optional[float] = None):
        """
        Update the carb, protein, or fat ratio for a specific time in the ratios table.

        Args:
            time (str): The time in 'HH:MM' format to update.
            new_carbratio (Optional[float]): New carbohydrate ratio (if updating).
            new_proteinratio (Optional[float]): New protein ratio (if updating).
            new_fatratio (Optional[float]): New fat ratio (if updating).
        """
        query = 'UPDATE ratios SET '
        updates = []
        params = []

        if new_carbratio is not None:
            updates.append("carbratio = ?")
            params.append(new_carbratio)
        if new_proteinratio is not None:
            updates.append("proteinratio = ?")
            params.append(new_proteinratio)
        if new_fatratio is not None:
            updates.append("fatratio = ?")
            params.append(new_fatratio)

        if updates:
            query += ', '.join(updates) + ' WHERE time = ?'
            params.append(time)
            with self.connect_db() as conn:
                conn.execute(query, params)
                conn.commit()

    def delete_ratio(self, time: str):
        """
        Delete a ratio from the ratios table based on time.

        Args:
            time (str): The exact time in 'HH:MM' format to delete.
        """
        query = '''
        DELETE FROM ratios WHERE time = ?
        '''
        with self.connect_db() as conn:
            conn.execute(query, (time,))
            conn.commit()
