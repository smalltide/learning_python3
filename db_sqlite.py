import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    sql = f"INSERT INTO store VALUES ('{item}', {quantity}, {price})"
    #print(sql)
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(sql)
    #cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows


insert('ice2', 100, 2.5)
print(view())
