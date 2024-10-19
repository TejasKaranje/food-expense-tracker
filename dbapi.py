#dbapi.py file for food-tracker project 
import sqlite3

conn = sqlite3.connect('foodtracker.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Records
    (order_date TEXT, item_name TEXT, quantity INTEGER,
    item_cost REAL, type TEXT, name TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Cost 
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    item_name TEXT UNIQUE, item_cost REAL)''')
cur.close()

def insertnewrecords(paramlist):
    output = ""
    try:
        cur = conn.cursor()
        cur.execute('''INSERT INTO Records
            (order_date, item_name, quantity, item_cost, type, name)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (paramlist[0], paramlist[1], paramlist[2], paramlist[3], paramlist[4], paramlist[5]))
        conn.commit()
        cur.close()
        output = "The record has been added successfully."
    except:
        output = "0"
    return output

def retrievedata():
    cur = conn.cursor()
    cur.execute('SELECT * FROM Records WHERE order_date=?', (date,))
    for row in cur:
        print(row)
    cur.close()

def addnewfooditem(itemName, itemCost):
    try:
        itemName = itemName.lower()
        itemCost = float(itemCost)
        cur = conn.cursor()
        cur.execute('SELECT * FROM Cost WHERE item_name =?', (itemName,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT OR IGNORE INTO Cost 
                (item_name, item_cost) 
                VALUES (?, ?)''',
                (itemName, itemCost))
            conn.commit()
            return 'New food item has been added.'
        else:
            return 'The food item already exists.'
        cur.close()
    except:
        return 'Bad data was entered.'

