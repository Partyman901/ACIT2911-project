from models import DatabaseManager
from views import View

class AppController:
    def run(self):
        running = True
        while running == True:
            manager = DatabaseManager()
            option = input("\nPlease select an option:\n [1] List all employees\n [2] Search employee\n [4] Exit Program\n ")
            try:
                if int(option) == 1: # Loops through list of employees and prints them
                    employee_list = manager.list_all()
                    View().list_employees(employee_list)
                    exit_list_all = input("Press Enter to Continue ")

                elif int(option) == 2: # Loop through the list of employees and find the employee that matches the input 
                    search = input("Enter the Employee ID: ")
                    if manager.return_one(search):
                        employee = manager.return_one(search)
                        View().one_employee(employee)
                        exit_list_all = input("Press Enter to Continue ")
                    else:
                        print("\nThat employee is not in the database!")

                elif int(option) == 4: # Closes connection to database and exits program
                    print("Exiting program...")
                    manager.connection.close()
                    running = False

                else:
                    print("\nPlease enter a valid option")
            except:
                print("\nPlease enter a valid option")
                continue
        return running    