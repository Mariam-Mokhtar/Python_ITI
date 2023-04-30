from employee import Employee
import sys
sys.path.append("F:/OS_ITI/python/Lab3")
from DataBase.handler import DbHandle
from prettytable import PrettyTable

db_handler=DbHandle("localhost","root","",'python_lab_2',"employees")
class Manager(Employee): 
    def __init__(self,first_name,last_name,age,department,salary,Managed_department):
       super().__init__(first_name,last_name,age,department,salary)
       self.Managed_department=Managed_department
       db_handler.update_managed_dept(self.Managed_department,self.id)
   
    
    @classmethod
    def show(cls,id):
        employee=None
        for emp in Manager.all_employee:
           if emp.id==id:
               employee=emp
               break
        if employee:
            if employee.Managed_department:
                employee.salary="confidential"
            cls.print_employee(employee,"one")
        else:
            print(f"No Employee with this id {id}")
                    