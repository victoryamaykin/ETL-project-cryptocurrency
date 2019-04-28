-- Create Database--
CREATE DATABASE cryptocurrency_db;

-- Issue USE statement to activate the Database to use--
USE cryptocurrency_db;

-- Create Table --
create table data (
Currency TEXT NOT NULL,
Date_open DATE NOT NULL,
Open_price DEcimal(12,2),
High INT NOT NULL,
Low INT NOT NULL,
Close_price Decimal(12,2),
Volume Decimal(12,2),
Market_Cap INT NOT NULL
);

-- Create Table --
create table ranks (
Close_Ratio int,
Ranknow int,
Currency Text not null,
Spread int,
System int
);  

-- Use the following to retrieve data from database --
Select d.Currency, d.Date_open, d.Open_price , d.high, d.low, d.close_price,
r.spread, r.system, r.close_ratio, r.ranknow, d.volume, d.market_cap
From data AS d inner Join ranks AS r on r.currency = d.currency
Where r.spread > 0
order by ranknow DESC;



