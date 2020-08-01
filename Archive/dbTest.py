import sqlite3
from datetime import datetime

conn = sqlite3.connect('shop.db')
conn.execute("PRAGMA foreign_keys = 1")

c = conn.cursor()
c.executescript(open("../setup.sql").read())
conn.commit()

for x in range(30):
    c.execute("INSERT INTO types (name, image) VALUES (?, ?)", ("Test" + str(x+1), "http://google.com"))
    for y in range(5):
        c.execute("INSERT INTO batches (type, expiry, price) VALUES (?, ?, ?)", (x+1, datetime.now(), 45))
        for z in range(24):
            c.execute("INSERT INTO cans (batch) VALUES (?)", (y+1,))
conn.commit()

conn.close()

