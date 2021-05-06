from models import DatabaseManager

class View:
    def __init__(self):
        print("\n First name    Last Name      Employee ID        Phone Number       Last Login               Position")
        print("------------------------------------------------------------------------------------------------------------------------")


    def list_employees(self, employee_list):
        for employee in employee_list:
            print(employee)
            print("------------------------------------------------------------------------------------------------------------------------")


    def one_employee(self, employee):
        print(employee)
        print("------------------------------------------------------------------------------------------------------------------------")