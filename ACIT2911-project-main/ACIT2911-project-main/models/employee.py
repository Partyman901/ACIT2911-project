class Employee:
    def __init__(self, first_name, last_name, id, phone_num, last_login, position):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.phone_num = phone_num
        self.last_login = last_login
        self.position = position


    def __str__(self):
        """ Returns the employee data in the proper format """
        return f" {self.first_name:<13}| {self.last_name:<13}| {self.id:<17}| {self.phone_num:<17}| {self.last_login:<23}| {self.position:<20}"
