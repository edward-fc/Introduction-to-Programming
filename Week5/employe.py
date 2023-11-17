
class Employee():
    def __init__(self, first_name, last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = "{}.{}@imagine.com".format(self.first_name,self.last_name)
        print(self.first_name,self.last_name,self.salary,self.email)
    def employee_details(self):
        print("Name: {} {}".format(self.first_name,self.last_name))
        print("Email: " + self.email)
        print("Annual salary: {}".format(self.salary))

Emplyee1 = Employee("edward","Certer",10000)
Emplyee1.employee_details()