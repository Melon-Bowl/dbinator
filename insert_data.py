# Program which inserts data into a database
import sqlite3

def insert_data(db_name, name, price, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "insert into '{}' (Name, Price) values (?,?)".format(table_name)
        product = (name, price)
        cursor.execute(sql, product)
        db.commit()

if __name__ == "__main__":
    product = ("GFuel", 1.99)
    insert_data(product)