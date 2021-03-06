import sqlite3
import os
from sqlite3.dbapi2 import Cursor, SQLITE_INSERT, SQLITE_UPDATE
from models.employee import Employee



class DatabaseManager:
    """ Manages everything to do with the database """
    def __init__(self, database="employee.db"):
        """ Creates the database """
        self.connection = sqlite3.connect(database) # Connects to the database
        self.cursor = self.connection.cursor() # Allows us to execute SQL commands 
        self.employees = dict()

        self.cursor.execute("SELECT * FROM myTable")
        employee_data = self.cursor.fetchall()
        for employee in employee_data:
            new_employee = Employee(first_name=employee[0], last_name=employee[1], id=employee[2], phone_num=employee[3], last_login=employee[4], position=employee[5])
            self.employees[str(employee[2])] = new_employee # Adds employee instance to dictionary


    def list_all(self):
        """ Function that lists all employees in the database """
        employee_list = list()
        for employee in self.employees.values():
            employee_list.append(employee)
        return employee_list


    def return_one(self, search):
        """ Function that returns an employee that matches the ID """
        for id, employee in self.employees.items():
            if id == search:
                return employee
        return None # Returns nothing if employee is not found


    def add_employee(self, first_name, last_name, id, phone_num, last_login, position):
        """function which adds new employee to database"""
        sqlite_insert = """INSERT INTO myTable
                          (`First_Name`,`Last_Name`,`IDnumber`,`Phone_Number`,`Last_login_date_time`,`Job_Title`)
                          VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (first_name, last_name, id, phone_num, last_login, position)
        self.cursor.execute(sqlite_insert, data_tuple)
        self.connection.commit()
        return True


    def remove_employee(self,id):
        """ function that deletes employee from database """
        sql = f"delete from myTable where IDnumber= '{id}'"
        self.cursor.execute(sql)
        self.connection.commit()
        return True

    def update_employee(self,first_name, last_name, id, phone_num, last_login, position):
        """ function which updates existing employee in the database """
        sqlite_update = """UPDATE myTable
                        SET First_Name = ?, Last_Name = ?, IDnumber= ?, 
                        Phone_Number = ?, Last_login_date_time = ?, Job_Title = ?
                        WHERE IDnumber = ?;"""
        data_tuple = (first_name, last_name, id, phone_num, last_login, position, id)
        self.cursor.execute(sqlite_update, data_tuple)
        self.connection.commit()
        return True