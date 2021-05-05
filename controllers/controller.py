from models import DatabaseManager

class AppController:
    def run(self):
        running = True
        while running == True:
            manager = DatabaseManager()
            option = input("\nPlease select an option:\n [1] List all employees\n [2] Search employee\n [4] Exit Program\n ")
            try:
                if int(option) == 1: # Loops through list of employees and prints them
                    print("\n First name    Last Name      Employee ID        Phone Number       Last Login               Position")
                    print("------------------------------------------------------------------------------------------------------------------------")
                    employee_list = manager.list_all()
                    for employee in employee_list:
                        print(employee)
                        print("------------------------------------------------------------------------------------------------------------------------")
                    exit_list_all = input("Press Enter to Continue ")

                elif int(option) == 2: # Loop through the list of employees and find the employee that matches the input 
                    search = input("Enter the Employee ID: ")
                    if manager.return_one(search):
                        employee = manager.return_one(search)
                        print("\n First name    Last Name      Employee ID        Phone Number       Last Login               Position")
                        print("------------------------------------------------------------------------------------------------------------------------")
                        print(employee)
                        print("------------------------------------------------------------------------------------------------------------------------")
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