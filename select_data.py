# Program which selects data from a database and then prints it in the console
import sqlite3

def select_all_products(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "select * from '{}'".format(table_name)
        cursor.execute(sql)
        products = cursor.fetchall()
        return products

def select_product(db_name, table_name, product_id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "select * from {} where ProductID=?".format(table_name)
        cursor.execute(sql, product_id)
        product = cursor.fetchone()
        return product

if __name__ == "__main__":
    products = select_all_products()
    print(products)
    product = select_product(3)
    print(product)
