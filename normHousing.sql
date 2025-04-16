-- remove existing tables
drop table if exists extremes;
drop table if exists normhousing;

-- make the normhousing table
create table normhousing (like housing);

-- create extremes table
create table extremes (
    minlongitude float, maxlongitude float,
    minlatitude float, maxlatitude float,
    minhousing_median_age float, maxhousing_median_age float,
    mintotal_rooms float, maxtotal_rooms float,
    mintotal_bedrooms float, maxtotal_bedrooms float,
    minpopulation float, maxpopulation float,
    minhouseholds float, maxhouseholds float,
    minmedian_income float, maxmedian_income float,
    minmedian_house_value float, maxmedian_house_value float
    );

-- calculate and insert the extremes
insert into extremes select 
    min(longitude) as minlongitude, max(longitude) as maxlongitude 
    from housing;

-- add normalized values to normhousing table
insert into normhousing select 
    (longitude - minlongitude)/(maxlongitude-minlongitude) as longitude 
    from housing, extremes;

-- to run, type into PSQL: "\i normHousing.sql"