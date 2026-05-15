from menu import Menu


class Restaurant:

    def __init__(self, name):

        self.name = name
        self.menu = Menu()
        self.employees = []

    def add_employee(self, employee):

        self.employees.append(employee)

    def view_employee(self):

        print("\n===== Employee List =====")

        for emp in self.employees:

            print(f"Name : {emp.name}")
            print(f"Email : {emp.email}")
            print(f"Phone : {emp.phone}")
            print(f"Designation : {emp.designation}")
            print("----------------------")