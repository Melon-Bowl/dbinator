# Main file which lets you create, insert, update, select and deleta data from a database
# By Egor Vert

# Import all of the functions:
from create_data import createTable as create
from insert_data import insert_data as insert
from update_data import update_product as update
from delete_data import delete_product as delete
from select_data import select_all_products as select_all 
from select_data import select_product as select_one


# Initialise program
if __name__ == "__main__":
    # Show header
    print("\033[1;34;40m \n### Welcome to Egor's database management system ### \n")

    print("\033[1;37;40m Please input the name of the database you are working with.")
    db_name = input("\033[0;32;40m Name >> ")

    print("\033[1;37;40m \n What would you like to do? (C)reate data // (I)nsert data // (U)pdate data // (D)elete data // (S)how all data // (P)ick one row to show")
    command = input("\033[0;32;40m Command >> ")

    try:
        if command.lower() == 'c':
            print("\033[1;37;40m \n Creating data. Please input the name of new entity.")
            table_name = input("\033[0;32;40m Table name >> ")
            print("\033[0;37;40m")
            sql = """create table {}
                    (ProductId integer,
                    Name text,
                    Price real,
                    primary key(ProductId))""".format(table_name)
            create(db_name, table_name, sql)

        elif command.lower() == 'i':
            print("\033[1;37;40m \n Inserting data. Please enter the name of the entity you would like to add data to.")
            table_name = input("\033[0;32;40m Table name >> ")

            print("\033[1;37;40m \n Please enter the name of the new record.")
            name = input("\033[0;32;40m Name >> ")

            print("\033[1;37;40m \n Please enter the new price.")
            price = input("\033[0;32;40m Price >> ")
            
            print("\033[0;37;40m")
            insert(db_name, name, price, table_name)

        elif command.lower() == 'u':
            print("\033[1;37;40m \n Updating data. Please enter the name of the entity you would like to update data in.")
            table_name = input("\033[0;32;40m Table name >> ")

            print("\033[1;37;40m \n Please enter the ID of the product you would like to update.")
            product_id = input("\033[0;32;40m Id >> ")

            print("\033[1;37;40m \n Please enter the new name.")
            name = input("\033[0;32;40m Name >> ")

            print("\033[1;37;40m \n Please enter the new price.")
            price = input("\033[0;32;40m Price >> ")

            print("\033[0;37;40m")
            update(db_name, name, price, product_id, table_name)

        elif command.lower() == 'd':
            print("\033[1;37;40m \n Deleting data. Please enter the name of the entity you would like to delete data from.")
            table_name = input("\033[0;32;40m Table name >> ")

            print("\033[1;37;40m \n Please enter the Id of the product you would like to delete.")
            product_id = input("\033[0;32;40m Id >> ")

            print("\033[0;37;40m")
            delete(db_name, table_name, product_id)

        elif command.lower() == 's':
            print("\033[1;37;40m \n Selecting data. Please enter the name of the entity you would like to see the data of.")
            table_name = input("\033[0;32;40m Table name >> ")
            output = select_all(db_name, table_name)
            print(output)
        
        elif command.lower() == 'p':
            print("\033[1;37;40m \n Selecting data. Please enter the name of the entity where the data is located.")
            table_name = input("\033[0;32;40m Table name >> ")

            print("\033[1;37;40m \n Please enter the Id of the product you would like to see.")
            product_id = input("\033[0;32;40m Id >> ")

            output = select_one(db_name, table_name, product_id)
            print(output)
        else:
            print("\033[1;31;40m ### Invalid Command. Please try again ###")
            exit()
    except:
        print("\033[1;31;40m ### An Unknown Error has Occurred. Now Exiting...")
        exit()

