CREATE TABLE `food` (
  `id` INTEGER PRIMARY KEY,
  `type` INTEGER,
  `foodname` TEXT,
  `carbs` REAL,
  `protein` REAL,
  `fat` REAL,
  `servingsize` REAL,
  `unittype` TEXT,
  `foodtype` INTEGER,
  FOREIGN KEY (`foodtype`) REFERENCES `foodtypes` (`id`)
);

CREATE TABLE `foodtypes` (
  `id` INTEGER PRIMARY KEY,
  `typename` TEXT
);

CREATE TABLE `Meals` (
  `code` INTEGER PRIMARY KEY,
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
