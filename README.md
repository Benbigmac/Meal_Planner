#How to Develop/RUN
from this directory level use this command
flask --app mealwiz run --debugger

within the utilities folder I've set up some defaults for food taken from the USDA food database. I am not responsible for errors in these food items Information
nor am I responsible for issues that arise from using said data

#TODO List

## styling changes needed
- fix up food library styling
- remove red lines on landing page
- clean up ratios modal
- fix food list for meal pushing save meal button out of view
- affix save meal to bottom of page on PC version
## landing page changes needed
- ability to open existing meal
- ability to add new food to food library
- modify ratios and add new ones
- display insulin for meals
## updates needed for new Meal page
- change units of measurement used and convert serving size on food items
- when page loads populate food library tab based on what's active/selected
- autoselect ratio based on closest time
-


#Common Serving sizes
Grams (g)
Milligrams (mg)
Ounces (oz)
Pounds (lbs)
Cups (cup)
Tablespoons (tbsp)
Teaspoons (tsp)
Fluid Ounces (fl oz)
Milliliters (ml)
Liters (L)
Item (I)
Serving (e.g., 1 serving of pasta)
Pinch (used in cooking for small amounts of seasonings)
Dry Cups (e.g., 1 cup of rice, 1 cup of soup)


# Key Nutrient Fields Explanation

    Macronutrients:
        carbs, protein, fat, and fiber provide insights into the food's energy and dietary impact.
        saturated_fat and trans_fat are included for tracking unhealthy fat types.

    Micronutrients:
        Vital vitamins (A, C, D, K) and minerals (e.g., calcium, iron, zinc) help assess nutritional quality.

    Cholesterol and Sodium:
        Important for monitoring heart and cardiovascular health.

    Glycemic Index and Load:
        Useful for individuals managing diabetes or blood sugar levels.

    Omega Fatty Acids:
        omega_3 and omega_6 are critical for brain and heart health.
