import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite') # path to connect to database
cur = conn.cursor() # open

df = pd.DataFrame(
    cur.execute("""SELECT * FROM offices;""").fetchall(),
    columns=[x[0] for x in cur.description]
)

print(df) #printing out result

conn.close() # close

