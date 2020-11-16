# Program which updates data in a database
import sqlite3

def update_product(db_name, name, price, productId, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "update {} set Name=?, Price=? where ProductID=?".format(table_name)
        data = (name, price, productId)
        cursor.execute(sql, data)
        db.commit()

if __name__ == "__main__":
    data = ("Latte", 2.45, 1)
    update_product(data)
