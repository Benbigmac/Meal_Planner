CREATE TABLE `food` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `type` int,
  `foodname` varchar(255),
  `carbs` double,
  `protein` double,
  `fat` double,
  `servingsize` double,
  `unittype` varchar(255),
  `foodtype` int,
  PRIMARY KEY (`id`, `foodname`)
);

CREATE TABLE `foodtypes` (
  `id` int,
  `typename` varchar(255),
  PRIMARY KEY (`id`)
);

CREATE TABLE `Meals` (
  `code` int,
  `mealtime` timestamp,
  `fooditems` LIST,
  `totalcarbs` double,
  `totalfat` double,
  `totalprotein` double,
  `ratios` int
);

CREATE TABLE `restaurants` (
  `code` int PRIMARY KEY,
  `name` varchar(255),
  `fooditems` LIST
);

CREATE TABLE `ratios` (
  `time` int PRIMARY KEY,
  `name` varchar(255),
  `carbratio` double,
  `proteinratio` double,
  `fatratio` double
);

ALTER TABLE `food` ADD FOREIGN KEY (`foodtype`) REFERENCES `foodtypes` (`id`);

ALTER TABLE `Meals` ADD FOREIGN KEY (`fooditems`) REFERENCES `food` (`id`);

ALTER TABLE `Meals` ADD FOREIGN KEY (`ratios`) REFERENCES `ratios` (`time`);

ALTER TABLE `restaurants` ADD FOREIGN KEY (`fooditems`) REFERENCES `food` (`id`);
