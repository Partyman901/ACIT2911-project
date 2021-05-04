from models import DatabaseManager

class AppController:
    def run(self):
        running = True
        while running == True:
            manager = DatabaseManager()
            option = input("\nPlease select an option:\n [1] List all employees\n [2] Search employee\n [4] Exit Program\n ")
            
            if int(option) == 1: # Loops through list of employees and prints them
                print("\n First name    Last Name      Employee ID        Phone Number       Last Login               Position")
                print("------------------------------------------------------------------------------------------------------------------------")
                employee_list = manager.list_all()
                for employee in employee_list:
                    print(f" {employee[0]:<13}| {employee[1]:<13}| {employee[2]:<17}| {employee[3]:<17}| {employee[4]:<23}| {employee[5]:<20}")
                    print("------------------------------------------------------------------------------------------------------------------------")
                exit_list_all = input("Press Enter to Continue ")

            elif int(option) == 2: # Loop throgu the list of employees and find the employee that matches the input 
                search = input("Enter the Employee ID: ")
                print("\n First name    Last Name      Employee ID        Phone Number       Last Login               Position")
                print("------------------------------------------------------------------------------------------------------------------------")
                employee_list = manager.list_all()
                for employee in employee_list:
                    if employee[2] == search:
                        print(f" {employee[0]:<13}| {employee[1]:<13}| {employee[2]:<17}| {employee[3]:<17}| {employee[4]:<23}| {employee[5]:<20}")
                print("------------------------------------------------------------------------------------------------------------------------")
                exit_list_all = input("Press Enter to Continue ")

            elif int(option) == 4: # Closes connection to database and exits program
                print("Exiting program...")
                manager.connection.close()
                running = False

            else:
                print("Please enter a valid option")