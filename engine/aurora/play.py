import sqlite3

con = sqlite3.connect("veyra.db")
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS characters(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT NOT NULL,
    disposition INTEGER DEFAULT 0)""")

cur.execute("INSERT INTO characters(name,region)VALUES(?,?)",
           ("Maren","lumenreach"))
con.commit()

print(cur.execute("SELECT * FROM characters").fetchall())

cur.execute("""CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY,
    timestamp INTEGER NOT NULL,
    type TEXT NOT NULL,
    data TEXT NOT NULL)""")

cur.execute("INSERT INTO events(timestamp,type,data)VALUES(?,?,?)",
            (1,"PLAYER_HELPED",'{"npc":"maren"}'))
cur.execute("INSERT INTO events(timestamp,type,data)VALUES(?,?,?)",
            (2,"player_not_helped",'{"npc":"saren"}'))
cur.execute("INSERT INTO events(timestamp,type,data)VALUES(?,?,?)",
            (3,"player_not_helped",'{"npc":"paren"}'))
con.commit()

