import sqlite3

class DatabaseManager:
    def __init__(self, database="employee.db"):
        self.connection = sqlite3.connect(database) # Connects to the database
        self.cursor = self.connection.cursor() # Allows us to execute SQL commands 

    def list_all(self):
        """ Function that lists all employees in the database """
        self.cursor.execute("SELECT * FROM myTable")
        employee_list = self.cursor.fetchall()
        return employee_list

    def return_one(self, search):
        """ Function that returns an employee that matches the ID """
        self.cursor.execute("SELECT * FROM myTable")
        employee_list = self.cursor.fetchall()
        for employee in employee_list:
            if employee[2] == search:
                return employee
        return None # Returns nothing if employee is not found
