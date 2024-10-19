import sqlite3
from datetime import datetime
import dbapi as db

def collectnewrecords():
    paralist = list()
    output = ""
    try:
        date = input('Enter date (MM/DD/YYYY): ')
        date = datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
        paralist.append(date)
        itemName = input('Enter Item Name: ')
        itemName = itemName.lower()
        paralist.append(itemName)
        qty = int(input('Enter Item Quantity: '))
        paralist.append(qty)
        itemCost = float(input('Enter Per Item Cost: '))
        totalItemCost = itemCost * qty
        paralist.append(totalItemCost)
        type = input('Ordered for? (Breakfast/Lunch/Dinner): ')
        type = type.lower()
        paralist.append(type)
        name = input('Ordered by?: ')
        name = name.lower()
        paralist.append(name)
        output = db.insertnewrecords(paralist)
    except:
        output = 'Bad data is entered. Please try again.'
    return output



print(collectnewrecords())