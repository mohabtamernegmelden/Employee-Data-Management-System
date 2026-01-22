
import os
import ast
os.system('cls' if os.name == 'nt' else 'clear')

class EmployeeManager:
    def __init__(self):
        self.all_employees = []
        self.ids = set()
        if os.path.exists("employees.csv"):
            with open("employees.csv", "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            employee = ast.literal_eval(line)
                            self.all_employees.append(employee)
                            self.ids.add(employee['id'])
                        except (ValueError, SyntaxError):
                            print(f"Warning: Skipping invalid line in CSV: {line}")
    def add_employee(self,id,name,position,salary):
        for id_existing in self.ids:
            if id_existing==id:
                print("This ID already exist. Please use a undique ID.")
                input("Press Enter to continue")
                return
        try:
            check=int(id)
            salary=float(salary)
        except ValueError:
            print("Invalid salary or id input.")
            input("Press Enter to continue")
            return
        
        employee={
            "id":id,
            "name":name,
            "position":position,
            "salary":salary
        }

        self.all_employees.append(employee)
        
        open("employees.csv","a").write(f"{employee}\n")
        self.ids.add(id)
        print("Employee added successfully")
        input("Press Enter to continue")
    def view_all_employees(self):
        print("All Employees:")
        for employee in self.all_employees:
            print(employee)
        print("End of employee list")
        input("Press Enter to continue")
    def update_employee(self,id,name=None,position=None,salary=None):
        for employee in self.all_employees:
            if employee["id"]==id:
                if name!=None:
                    employee["name"]=name
                if position!=None:
                    employee["position"]=position
                    
                if salary!=None:
                    try:
                        check=int(id)
                        salary=float(salary)
                    except ValueError:
                        print("Invalid salary or id input.")
                        input("Press Enter to continue")
                        return
                    employee["salary"]=float(salary)
                with open("employees.csv", "w") as f:
                    for emp in self.all_employees:
                        f.write(f"{emp}\n")
                print("Employee's data updated successfully")
                input("Press Enter to continue")
                break
        else:
            print("This ID doesn't exist")
            input("Press Enter to continue")
    def delete_employee(self,id):
        for employee in self.all_employees:
            if employee["id"]==id:
                self.all_employees.remove(employee)
                self.ids.remove(id)
                with open("employees.csv", "w") as f:
                    for emp in self.all_employees:
                        f.write(f"{emp}\n")
                print("Employee deleted successfully")
                input("Press Enter to continue")
                break
        else:
            print("This ID doesn't exist")
            input("Press Enter to continue")
    def search_employee(self,id):
        for employee in self.all_employees:
            if employee["id"]==id:
                print("Employee found:")
                print(employee)
                input("Press Enter to continue")
                break
        else:
            print("This ID doesn't exist")
            input("Press Enter to continue")
            
    def exit_system(self):
        print("Exiting the system.")

manager=EmployeeManager()
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        id=input("Enter Employee ID: ")
        name=input("Enter Employee Name: ")
        position=input("Enter Employee Position: ")
        salary=input("Enter Employee Salary: ")
        manager.add_employee(id,name,position,salary)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif choice==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        manager.view_all_employees()
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice==3:
        os.system('cls' if os.name == 'nt' else 'clear')
        id=input("Enter Employee ID to update: ")
        name=input("Enter new name (leave blank to keep unchanged): ")
        position=input("Enter new position (leave blank to keep unchanged): ")
        salary=input("Enter new salary (leave blank to keep unchanged): ")
        manager.update_employee(id,name if name else None,position if position else None,salary if salary else None)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif choice==4:
        os.system('cls' if os.name == 'nt' else 'clear')
        id=input("Enter Employee ID to delete: ")
        manager.delete_employee(id)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice==5:
        os.system('cls' if os.name == 'nt' else 'clear')
        id=input("Enter Employee ID to search: ")
        manager.search_employee(id)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif choice==6:
        manager.exit_system()
        break
    else:
        print("Invalid choice. Please try again.")
        os.system('cls' if os.name == 'nt' else 'clear')