import pandas as pd
import sqlite3 as db
import requests
import nasdaqdatalink as ndl

SQL = '''
        SELECT Album.Title, Artist.Name 
        FROM ALBUM 
        LEFT JOIN Artist
        ON Album.ArtistId = Artist.ArtistId
        '''

# Building connection to database
con = db.connect("Chinook_Sqlite.sqlite")

# Setting cursor
cursor = con.cursor()
cursor.execute(SQL)

artists = [[item[0],item[1]] for item in cursor]

# DataFrame
df = pd.read_sql(SQL, con)
print(df)
