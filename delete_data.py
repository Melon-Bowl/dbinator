# Program that deletes data from a database
import sqlite3
def delete_product(db_name, table_name, productId):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "delete from '{}' where ProductID=?".format(table_name)
        cursor.execute(sql, productId)
        db.commit()

if __name__ == "__main__":
    data = ("Latte",)
    delete_product(data)