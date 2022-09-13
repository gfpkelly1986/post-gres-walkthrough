# This is a walktorough using SQL alchemy to query a Postgres database using Python code.
# Its  a step up from using psycopg2 where punctuation is so strict.

# 
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Use create_engine to point to our chinookone database as db
db = create_engine("postgresql:///chinookone")

# The metadata class will contain a collection of table objects
meta = MetaData(db)

# Before querying the database, tables need to be constructed
# so python knows which schema you are working with.
# Each table is known as a data model.

# Run these commands to get the table headers needed
# set_pg
# psql -d chinookone
# SELECT * FROM "Artist" WHERE false;
# Create a variable for the "Artist table", This is a data model
# Defining a Column = (columnname, data presented, further fields)
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create a variable for the "Album" Table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("album_table.ArtistId"))
)

# Create a variable for the "Track" Table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),
)

# Make the connection to the database
# save your connection to a variable called connection0

with db.connect() as connection:

    # Query 1 - select all records from the "Artist" Table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # Notice the use of the python list even though its only one column
    # we are grabbing, and .c also.
    # select_query = artist_table.select().with_only_columns
    # ([artist_table.c.Name])

    # Query - 3 select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query - 4 select only by ArtistId #51 on the 'Album' table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query - 5 select only the albums with 'ArtistId' #51 on the 'Album' table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)