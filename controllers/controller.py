from models.employee import Employee
from models import DatabaseManager
from views import View
from datetime import date, datetime



class AppController:
    """ This is the controller for the whole employee tracker app """
    def run(self):
        today = date.today()
        running = True
        while running == True:
            manager = DatabaseManager()
            option = input("\nPlease select an option:\n [1] List all employees\n [2] Search employee\n [3] Add employee\n [4] Delete employee\n [5] Update employee\n [6] Exit Program\n ")
            # shows all options available to the user
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
                
                elif int(option) == 3: # Adding an employee to the database
                    first_name = input("Enter Employee First Name: ")
                    last_name = input("Enter Employee Last name: ")
                    id = input("Enter Employee ID number: ")
                    phone_num = input("Enter employee phone number: ")
                    last_login_time = datetime.now()
                    last_login = last_login_time.strftime("%Y-%m-%d %H:%M:%S")
                    position = input("Enter employee position: ")
                    # error checking below, returns to main menu
                    if first_name == '':
                        print('\nEmployee first name must be filled.')
                    elif last_name == '':
                        print('\nEmployee last name must be filled.')
                    elif manager.return_one(id):
                        print("\nEmployee ID already exists")
                    elif id == '':
                        print('\nEmployee ID must be filled.')
                    elif position == '':
                        print('\nEmployee position must be filled.')
                    else:
                        employee = manager.add_employee(first_name, last_name, id, phone_num, last_login, position)
                        print('\nEmployee has been added!')

                elif int(option) == 4: # Function to delete an employee
                    id = input("Enter Employee Id: ")
                    if manager.return_one(id):
                        confirm = 'N'
                        while confirm == 'N':
                            print()
                            confirm = input(f'Are you sure you want to delete {id}? [Y|N] ')
                            if confirm.upper() == 'Y':
                                manager.remove_employee(id)
                                print("Employee",id,"Removed")
                                confirm = 'Y'
                            elif confirm.upper() == 'N':
                                print('Employee,', id, 'not deleted')
                                confirm = 'Y'
                    else:
                        print("Employee does not exists\nTry Again\n")

                elif int(option) == 5: # Function to update an employee 
                    id = input("Enter Employee Id: ")
                    employee = manager.return_one(id)
                    if employee:
                        print(f'Press "Enter" to keep the pre-existing data')
                        employee_values = [employee.first_name, employee.last_name, employee.phone_num, employee.position]
                        first_name = input('New first name: ')
                        # if field does not need to be updated, user presses 'Enter' key
                        if first_name == '':
                            first_name = employee_values[0]
                        last_name = input('New last name: ')
                        if last_name == '':
                            last_name = employee_values[1]
                        phone_num = input('New phone number: ')
                        if phone_num == '':
                            phone_num = employee_values[2]
                        position = input('New job position: ')
                        if position == '':
                            position = employee_values[3]
                        last_login_time = datetime.now()
                        last_login = last_login_time.strftime("%Y-%m-%d %H:%M:%S")
                        confirm = input(f'Are you sure you want to update {id}? [Y|N] ')
                        if confirm.upper() == 'Y':
                            employee = manager.update_employee(first_name, last_name, id, phone_num, last_login, position)
                            print(f'Employee, {id} has been updated!')
                        elif confirm.upper() == 'N':
                            print(f'Employee, {id}, not updated')
                    else:
                        print("Employee does not exists\nTry Again\n")

                elif int(option) == 6: # Closes connection to database and exits program
                    print("Exiting program...")
                    manager.connection.close()
                    running = False

                else:
                    print("\nPlease enter a valid option")
            except Exception as error:
                print(f"\n{error}")
                continue
        return running # To check our test coverage