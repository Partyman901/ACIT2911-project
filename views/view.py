from models import DatabaseManager



class View:
    """ this class is used to format repetitive output """
    def __init__(self):
        """ prints this each time the class is called in order to format output """
        print("\n First name    Last Name      Employee ID        Phone Number       Last Login               Position")
        print("------------------------------------------------------------------------------------------------------------------------")


    def list_employees(self, employee_list):
        """ formats output in list form """
        for employee in employee_list:
            print(employee)
            print("------------------------------------------------------------------------------------------------------------------------")


    def one_employee(self, employee):
        """ formats output for one employee """
        print(employee)
        print("------------------------------------------------------------------------------------------------------------------------")