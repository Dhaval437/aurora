import sqlite3
import sqlite3


def init_db(path:str)->sqlite3.Connection:
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY,
        timestamp INTEGER NOT NULL,
        type TEXT NOT NULL,
        data TEXT NOT NULL)""")
    con.commit()
    return con


def add_event(con:sqlite3.Connection,timestamp:int,type:str,data:str)->None:
    con.execute("INSERT INTO events (timestamp,type,data) VALUES(?,?,?)",
               (timestamp,type,data))
    con.commit()


def get_events(con: sqlite3.Connection,since: int=0)->list:
    cur =con.execute(
        "SELECT timestamp, type, data FROM events WHERE timestamp >=? ORDER BY timestamp",
        (since,))
    return cur.fetchall()
