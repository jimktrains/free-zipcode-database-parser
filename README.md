This parses and imports the csv file into a database (postgres at the moment) table defined by

    CREATE TABLE zips (
         id INT,
         zipcode CHARACTER(5),
         type VARCHAR(50),
         city VARCHAR(100),
         state CHARACTER(2),
         location_type VARCHAR(20),
         loctext VARCHAR(255),
         location VARCHAR(255),
         decom VARCHAR(20),
         notes VARCHAR(255));

    CREATE INDEX zipcodes_index ON zips(zipcode);
    ALTER TABLE zips ADD PRIMARY KEY (id);

