import sqlite3
conn = sqlite3.connect('rides.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS ride_pool")
c.execute("DROP TABLE IF EXISTS ride")

c.execute('''CREATE TABLE ride(
    ride_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    created_by TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    source INTEGER NOT NULL,
    destination INTEGER NOT NULL)''')
c.execute('''CREATE TABLE ride_pool(
    username TEXT NOT NULL,
    ride_id INTEGER NOT NULL,
    FOREIGN KEY(ride_id) REFERENCES ride(ride_id) ON UPDATE CASCADE ON DELETE CASCADE)''')

conn.commit()
conn.close()