from src.setup import *


def main():
    
    path = "test.db"

    connection = create_connection(path)
    cursor = connection.cursor()

    database = DataBase(connection, cursor)

    database.setup_database()



main()