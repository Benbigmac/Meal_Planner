import sqlite3
import os
from typing import List, Tuple, Optional




class mealWizDB:
    DB_NAME=''

    def __init__(self, db_name='/mealWiz.db'):
         print("db helper initialized")
         basedir = os.path.abspath(os.path.dirname(__file__))
         print(basedir)
         self.DB_NAME = basedir+db_name
         print(self.DB_NAME)

    def connect_db(self):
        """Connect to the SQLite database."""
        return sqlite3.connect(self.DB_NAME)

    def create_food(self, type: int, foodname: str, carbs: float, protein: float, fat: float, servingsize: float, unittype: str, foodtype: int):
        """Insert a new food item into the food table."""
        query = '''
        INSERT INTO food (type, foodname, carbs, protein, fat, servingsize, unittype, foodtype)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (type, foodname, carbs, protein, fat, servingsize, unittype, foodtype))
            conn.commit()

    def create_foodtype(self, typename: str):
        """Insert a new food type into the foodtypes table."""
        query = '''
        INSERT INTO foodtypes (typename)
        VALUES (?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (typename,))
            conn.commit()

    def create_meal(self, code: int, mealtime: str, totalcarbs: float, totalfat: float, totalprotein: float, ratios: int):
        """Insert a new meal into the Meals table."""
        query = '''
        INSERT INTO Meals (code, mealtime, totalcarbs, totalfat, totalprotein, ratios)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (code, mealtime, totalcarbs, totalfat, totalprotein, ratios))
            conn.commit()

    def add_food_to_meal(meal_code: int, food_id: int):
        """Link a food item to a meal in the MealFoodItems table."""
        query = '''
        INSERT INTO MealFoodItems (meal_code, food_id)
        VALUES (?, ?)
        '''
        with self.connect_db() as conn:
            conn.execute(query, (meal_code, food_id))
            conn.commit()

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

    def get_food_by_name(foodname: str) -> Optional[Tuple]:
        """Retrieve a food item by name."""
        query = '''
        SELECT * FROM food WHERE foodname = ?
        '''
        with self.connect_db() as conn:
            result = conn.execute(query, (foodname,)).fetchone()
        return result

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
