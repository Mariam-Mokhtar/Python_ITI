import sys
sys.path.append("F:/OS_ITI/python/Lab3")
from DataBase.handler import DbHandle
from prettytable import PrettyTable

db_handler=DbHandle("localhost","root","",'python_lab_2',"employees")

class Employee:
    
    all_employee=[]
    
    def __init__(self,first_name,last_name,age,department,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.department=department
        self.salary=salary
        self.Managed_department=None
        # Get auto-increment id from database
        self.id=db_handler.insert_employee(self)
        # Add new employee to list of all employees 
        Employee.all_employee.append(self)
        
    @staticmethod
    def transfer(id,new_dept):
        employee=None
        for emp in Employee.all_employee:
           if emp.id==id:
               employee=emp
               break
           
        if employee:
          employee.department=new_dept
          db_handler.update_dept(id,new_dept)
    
    @staticmethod
    def fire(id):
       # Find Employee with the give id 
       employee=None
       for emp in Employee.all_employee:
           if emp.id==id:
               employee=emp
               break
        
       if employee:
           # Remove Employee from the list of all employees
            Employee.all_employee.remove(employee)
           # Remove Employee from dataBase 
            db_handler.delete(id)
            print(f"{employee.first_name} {employee.last_name} has been fired.")
       else:
            print(f"No employee with id {id} found.")
            
    @classmethod
    def List_employees(cls):
         employees=db_handler.get_all_employees()
         cls.print_employee(employees,"all")

    @classmethod
    def show(cls,id):
        employee=None
        for emp in Employee.all_employee:
           if emp.id==id:
               employee=emp
               break
        if employee:
            if employee.Managed_department:
                employee.salary="confidential"
            cls.print_employee(employee,"one")
        else:
            print(f"No Employee with this id {id}")
   
    def print_employee(data,type):
        # Create a PrettyTable object
        table = PrettyTable()
        # Add columns to the table
        table.field_names = ["Id", "First_Name","Last_Name","Age","Department", "Salary","Managed_Department"]
        if data:
            if type=="one":
                table.add_row([data.id,data.first_name, data.last_name,data.age, data.department,data.salary,data.Managed_department])
        
            # Add data to the table
            else:
                for emp in data:
                    if emp[6]:
                       salary="confidential"
                    else:
                       salary=emp[5]
                    table.add_row([emp[0],emp[1], emp[2],emp[3], emp[4],salary,emp[6]])
            print(table)
        else:
            print(" \n \n ----No data available to show----")                  