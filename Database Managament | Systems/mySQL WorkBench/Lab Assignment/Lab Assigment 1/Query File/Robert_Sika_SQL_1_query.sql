CREATE SCHEMA `Demo_1`;

CREATE TABLE `Demo_1`.`new_table_1` (
  `property_id` INT NOT NULL,
  `address` VARCHAR(255) NULL,
  `bedrooms` INT NULL,
  `square_feet` INT NULL,
  `price` DECIMAL(10,2) NULL,
  PRIMARY KEY (`property_id`));


INSERT INTO new_table_1
VALUE(000001,"GH-849-234-1-ACCRA",4,2400,800000)