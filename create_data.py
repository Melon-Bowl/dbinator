# Implementing sqlite3 using python
import sqlite3

def createTable(db_name, table_name, sql):
    # Allows us to connect to the database
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        # Uses 'qmark' style to dynamically select the name from the sqlite_master table based on the table_name variable
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        # The cursor.fetchall() function returns 1 if the table exists
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                # Deletes the table if it exists
                cursor.execute("drop table if exists {0}".format(table_name))
                # Commits the changes to the database
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
        # If the user decided not to keep the table, then the sql code is executed
        if not keep_table:
            cursor.execute(sql)
            db.commit()

# Checks if the code is run from within and then executes the code below
if __name__ == "__main__":
    db_name = "coffe_shop.db"
    sql = """create table Product
            (ProductID integer,
            Name text,
            Price real,
            primary key(ProductID))"""
    # Calls the createTable() function
    createTable(db_name, "Product", sql)