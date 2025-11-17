import sqlite3
DB_PATH="/opt/wg-gui/config.db"
def db(): return sqlite3.connect(DB_PATH)
def fetchone(q,p=()): c=db();x=c.cursor();x.execute(q,p);r=x.fetchone();c.close();return r
def fetchall(q,p=()): c=db();x=c.cursor();x.execute(q,p);r=x.fetchall();c.close();return r
def execute(q,p=()): c=db();x=c.cursor();x.execute(q,p);c.commit();c.close()