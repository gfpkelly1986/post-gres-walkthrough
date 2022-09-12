# Linking up psycopg2 to connect to our postgreSQL database to python
import psycopg2

# connect to "chinookone" database
connection = psycopg2.connect(database="chinookone")

# build a cursor object of the database
# [similar to a list or array, you can then iterate over the cursor object]
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 3 - select only Queen from the Artist table
# !!The %s is a python string placeholder!!
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId"  #51 from the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where 
# the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple results)
results = cursor.fetchall()

# fetch the result (single results if you want them)
# results = cursor.fetchone()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)
