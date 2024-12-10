CREATE TABLE food (
    id INTEGER PRIMARY KEY,
    foodname TEXT NOT NULL,
    servingsize DOUBLE NOT NULL,
   servingsizeunit TEXT NOT NULL,
    carbs REAL,
    protein REAL,
    fat REAL,
    fiber REAL,
    saturated_fat REAL,
    trans_fat REAL,
    cholesterol REAL,
    sodium REAL,
    potassium REAL,
    calcium REAL,
    iron REAL,
    vitamin_a REAL,
    vitamin_c REAL,
    vitamin_d REAL,
    vitamin_k REAL,
    magnesium REAL,
    zinc REAL,
    glycemic_index REAL,
    glycemic_load REAL,
    omega_3 REAL,
    omega_6 REAL,
    foodtype INTEGER,
    FOREIGN KEY (foodtype) REFERENCES foodtypes (id)
);



CREATE TABLE `foodtypes` (
  `id` INTEGER PRIMARY KEY,
  `typename` TEXT
);

CREATE TABLE `Meals` (
  `code` INTEGER PRIMARY KEY AUTOINCREMENT,
  `mealtime` TIMESTAMP,
  `totalcarbs` REAL,
  `totalfat` REAL,
  `totalprotein` REAL,
  `ratios` TEXT,  -- Changed to TEXT format for time
  FOREIGN KEY (`ratios`) REFERENCES `ratios` (`time`)
);

CREATE TABLE `restaurants` (
  `code` INTEGER PRIMARY KEY,
  `name` TEXT
);

CREATE TABLE `ratios` (
  `time` TEXT PRIMARY KEY,  -- Stored as TEXT in 'HH:MM' format
  `name` TEXT,
  `carbratio` REAL,
  `proteinratio` REAL,
  `fatratio` REAL
);

-- Junction table for Meals and Food items
CREATE TABLE `MealFoodItems` (
  `meal_code` INTEGER,
  `food_id` INTEGER,
  FOREIGN KEY (`meal_code`) REFERENCES `Meals` (`code`),
  FOREIGN KEY (`food_id`) REFERENCES `food` (`id`)
);

-- Junction table for Restaurants and Food items
CREATE TABLE `RestaurantFoodItems` (
  `restaurant_code` INTEGER,
  `food_id` INTEGER,
  FOREIGN KEY (`restaurant_code`) REFERENCES `restaurants` (`code`),
  FOREIGN KEY (`food_id`) REFERENCES `food` (`id`)
);
