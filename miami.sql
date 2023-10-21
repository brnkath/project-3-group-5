DROP TABLE zip_income;
DROP TABLE restaurant;

CREATE TABLE zip_income (
	Zipcode VARCHAR NOT NULL,
	Median_income VARCHAR NOT NULL
);

CREATE TABLE restaurants (
	Name VARCHAR,
	Address VARCHAR,
	Category VARCHAR
);

SELECT * FROM restaurants;
SELECT * FROM zip_income;