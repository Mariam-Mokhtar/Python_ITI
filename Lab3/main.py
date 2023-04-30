import sys
sys.path.append('F:/OS_ITI/python/Lab3/Classes')

from employee import *
from manager import *

class App:
    def run(self):
        flag=True
        while flag:
            print()
            print("Welcome to the Employee Database")
            print("Please select an option:")
            print("1. Add new employee")
            print("2. List employees")
            print("3. Transfer employee by id")
            print("4. Fire employee by id")
            print("5. Quit program")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.list_employees()
            elif choice == "3":
                self.transfer_employee()
            elif choice == "4":
                self.fire_employee()
            elif choice == "5":
                self.quit_program()
            else:
                print("Invalid choice. Please try again.")
    
    def add_employee(self):
        print("Please Enter Your data:")
        first_name = input("First Name: ")
        last_name = input("Last name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        salary = float(input("Salary: "))
        if input("Is this a manager or not? (y/n): ").lower() == "y":
            managed_department = input("Managed department: ")
            Manager(first_name, last_name, age, department, salary, managed_department)
        else:
            Employee(first_name, last_name, age, department, salary)
    
    def list_employees(self): 
        Employee.List_employees()

    def transfer_employee(self):
        id = int(input("Please Enter id you want to show: "))
        new_dept=input("Please Enter department you want to show: ")
        Employee.transfer(id,new_dept)
    
    def fire_employee(self):
        id = int(input("Please Enter id you want to fire: "))
        Employee.fire(id)     
    
    def quit_program(self):
        print("Exiting the program...")
        sys.exit()  
                    
app=App()
app.run()