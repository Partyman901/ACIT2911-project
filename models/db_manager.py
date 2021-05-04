import sqlite3

class DatabaseManager:
    def __init__(self, database="employee.db"):
        self.connection = sqlite3.connect(database) # Connects to the database
        self.cursor = self.connection.cursor() # Allows us to execute SQL commands 

    def list_all(self):
        """ Function that lists all employees in the database """
        self.cursor.execute("SELECT * FROM myTable")
        employee_list = self.cursor.fetchall()
        # self.connection.commit()
        return employee_list

    def create_database(self):
        """ Creates the database. Only run if you are having trouble with the current database and need to recreate it for some reason """
        pass