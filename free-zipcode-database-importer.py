"""
 id            | integer                |
 zipcode       | character(5)           |
 type          | character varying(50)  |
 city          | character varying(100) |
 state         | character(2)           |
 location_type | character varying(20)  |
 lat           | real                   |
 lon           | real                   |
 xaxis         | real                   |
 yaxis         | real                   |
 woldreg       | character varying(50)  |
 country       | character varying(50)  |
 loctext       | character varying(255) |
 location      | character varying(255) |
 decom         | character varying(20)  |
 tax_returns   | integer                |
 pop           | integer                |
 wages         | integer                |
 notes         | character varying(255) |



"RecordNumber","Zipcode","ZipCodeType",
"City","State","LocationType","Lat","Long","Xaxis","Yaxis","Zaxis",
"WorldRegion","Country","LocationText","Location",
"Decommisioned","TaxReturnsFiled","EstimatedPopulation","TotalWages","Notes"

"""
import psycopg2
import csv

conn = psycopg2.connect("dbname=ls user=jim")
cur = conn.cursor()
with open('free-zipcode-database.csv.bak', 'r') as csv_file:
   zips = csv.DictReader(csv_file)
   for z in zips:
      cur.execute("""
      INSERT INTO zips (
         id, zipcode, type, city, state, location_type,
         loctext, location, decom, notes)
         VALUES
         (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
      """,
      (
         z["RecordNumber"],
         z["Zipcode"],
         z["ZipCodeType"],
         z["City"],
         z["State"],
         z["LocationType"],
         z["LocationText"],
         z["Location"],
         z["Decommisioned"],
         z["Notes"])
      )
      if int(z["RecordNumber"]) % 1000 == 0:
         conn.commit()
         print("Stored %d records so far" % int(z["RecordNumber"]))
cur.close()
conn.close()
