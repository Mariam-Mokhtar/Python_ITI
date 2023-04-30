import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass

class DbHandle:
    
    def __init__(self, host, user, password, database,table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table=table
        self.connection = None
        self.create_table()
     
    def create_table(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f'''drop table if exists {self.table}''')
            cursor.execute(f'''create table {self.table}(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            first_name VARCHAR(255),
                            last_name VARCHAR(255),
                            age INT,
                            department VARCHAR(255),
                            salary Float,
                            managed_department VARCHAR(255) DEFAULT NULL
                            );''')
            self.connection.commit()
            # print('A Table has been created successfully')
            cursor.close()
            self.disconnect()
        except mysql.connector.Error as e:
            print(f"Error in Creating Table{e}")    
                
    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            # print(f"Connected to {self.database} database")
        except Error as e:
            print(e)
            
    def insert_employee(self,data):
        try:
            self.connect()
            query = f"INSERT INTO {self.table} (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"
            values = (data.first_name, data.last_name, data.age, data.department, data.salary)
            cursor = self.connection.cursor()
            cursor.execute(query,values)
            self.connection.commit()
            employee_id= cursor.lastrowid
            print("Record inserted successfully")
            cursor.close()
            self.disconnect()
            return employee_id
        except Error as e:
            print("Error inserting record: ", e)
        
    def update_dept(self,id,new_dept):
        try:
            self.connect()
            query = f"UPDATE {self.table} SET department = %s where id = %s"
            values=(new_dept,id)
            cursor = self.connection.cursor()
            cursor.execute(query,values)
            self.connection.commit()
            print("Record updated successfully")
            cursor.close()
            self.disconnect()
        except Error as e:
           print("Error Updating department record: ", e)
         
    def delete(self,id):
        try:
            self.connect() 
            query=f"""delete from {self.table} where id={id}"""
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Record Deleted successfully")
            cursor.close()
            self.disconnect()  
        except Error as e:
           print("Error Deleted department record: ", e)
             
    def get_all_employees(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = '''SELECT id, first_name, last_name, age, department, salary, managed_department
                    FROM employees'''
            cursor.execute(query)
            employees = cursor.fetchall()
            cursor.close()
            self.disconnect()
            return employees
        except mysql.connector.Error as e:
            print(f"Error in Getting All Employees from Database {e}")   
    
    def update_managed_dept(self,new_dept,id):
        try:
            self.connect()
            query = f"UPDATE {self.table} SET managed_department = %s where id = %s"
            values=(new_dept,id)
            cursor = self.connection.cursor()
            cursor.execute(query,values)
            self.connection.commit()
            print("Record updated successfully")
            cursor.close()
            self.disconnect()
        except mysql.connector.Error as e:
            print(f"Error in Getting All Employees from Database {e}")   
            
    def disconnect(self):
        if self.connection:
            self.connection.close()
            # print(f"Disconnected from {self.database} database")
        
   

 
