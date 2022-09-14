# Set up imports: You import the needed data-types that are in your database

# We also need to import something called the
# declarative_base from the sqlalchemy declarative extension.
# Finally, we need to import the sessionmaker class from the ORM.
# The reason that we no longer need to import the Table class, is because with the ORM,
# we're not going to create tables, but instead, we'll be creating Python classes.
# These Python classes that we'll create will subclass the declarative_base, meaning that
# any class we're making will extend from the main class within the ORM.
# It's the same exact thing for the sessionmaker; instead of making a connection to the database
# directly
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to the postgres server on the localhost to get the chinook database
db = create_engine("postgresql:///chinookone")
base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Instead of connecting, we ask for a session
# Creste a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens up an actual session by calling the Session() subclass
session = Session()

# Create the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only the Artist Name of Queen from the "Artist" table
# ---- filter_by method of the session class used here ----
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.Name)

# Query 5 - select only albums with the "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query - 6 select only tracks filtered by the composer of Queen
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.Name)