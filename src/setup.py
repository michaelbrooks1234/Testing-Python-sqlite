import sqlite3
from sqlite3 import Error



class DataBase:

    def __init__(self, connection=None, cursor=None):
        self.connection = connection
        self.cursor = cursor

    def setup_database(self):
        result_tuple = self.cursor.execute("SELECT name FROM sqlite_master").fetchall()
        print(result_tuple)
        if(result_tuple == []):
            self.cursor.execute("CREATE TABLE movie(title, year, score)")
            result = self.cursor.execute("SELECT name FROM sqlite_master").fetchall()
            print(result)
            self.cursor.execute("""
                INSERT INTO movie VALUES
                    ('Nightmare On Elm street', 19, 10),
                    ('Whats:', 21, "youStupid"),
                    ('random Data', 123, 4332)
            """)
            # inserts have to be commited.
            self.connection.commit()
            # checking if everything went good.
            result = self.cursor.execute("SELECT score FROM movie").fetchall()
            print(result)
        else:
            result = self.cursor.execute("SELECT score FROM movie")
            if(result is None):
                self.cursor.execute("""
                    INSERT INTO movie VALUES
                        ('Nightmare On Elm street', 19, 10),
                        ('Whats:', 21, 1203),
                        ('random Data', 123, 4332)
                """)
                # inserts have to be commited.
                self.connection.commit()
                # checking if everything went good.
                result = self.cursor.execute("SELECT score FROM movie").fetchall()
                print(result)
            else:
                result = self.cursor.execute("SELECT title, year, score FROM movie").fetchall()
                print(result)


def create_connection(path):

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connetion Successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
