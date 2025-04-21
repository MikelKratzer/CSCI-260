-- remove extremes table
drop table if exists extremes;
drop table if exists normhousing;

-- Make the normhousing table
create table normhousing (like housing);

-- Create extremes table
create table extremes (
    minlongitude float,maxlongitude float,
    minlatitude float,maxlatitude float,
    minhousing_median_age float, maxhousing_median_age float,
    mintotal_rooms float,maxtotal_rooms float,
    mintotal_bedrooms float,maxtotal_bedrooms float,
    minpopulation float, maxpopulation float,
    minhouseholds float, maxhouseholds float,
    minmedian_income float, maxmedian_income float,
    minmedian_house_value float, maxmedian_house_value float
  );

-- Calculate and insert the extremes  
insert into extremes select 
  min(longitude) as minlongitude, max(longitude) as maxlongitude, 
  min(latitude) as minlatitude , max(latitude) as maxlatitude ,
  min(housing_median_age) as minhousing_median_age , max(housing_median_age) as maxhousing_median_age ,
  min(total_rooms) as mintotal_rooms , max(total_rooms) as maxtotal_rooms ,
  min(total_bedrooms) as mintotal_bedrooms , max(total_bedrooms) as maxtotal_bedrooms ,
  min(population) as minpopulation , max(population) as maxpopulation ,
  min(households) as minhouseholds , max(households) as maxhouseholds ,
  min(median_income) as minmedian_income , max(median_income) as maxmedian_income ,
  min(median_house_value) as minmedian_house_value , max(median_house_value) as maxmedian_house_value
  from housing;

-- function beUseful(field,minfield,maxfield)
create or replace function n(value float, min float, max float) returns float
  LANGUAGE SQL
  IMMUTABLE
  return (value - min) / (max - min);

-- Add the normalized values to the normhousing table
insert into normhousing select 
  n(longitude,minlongitude,maxlongitude) as longitude, 
  n(latitude,minlatitude ,maxlatitude ) as  latitude, 
  n(housing_median_age,minhousing_median_age ,maxhousing_median_age ) as  housing_median_age, 
  n(total_rooms,mintotal_rooms ,maxtotal_rooms ) as  total_rooms, 
  n(total_bedrooms,mintotal_bedrooms ,maxtotal_bedrooms ) as  total_bedrooms, 
  n(population,minpopulation ,maxpopulation ) as  population, 
  n(households,minhouseholds ,maxhouseholds ) as  households, 
  n(median_income,minmedian_income ,maxmedian_income ) as  median_income, 
  n(median_house_value,minmedian_house_value ,maxmedian_house_value ) as  median_house_value
  from housing, extremes;

-- to run, type into PSQL: "\i normHousing.sql"