import json
import csv

filename = 'employees.json'

employees = [
    {"id": 1, "name":"Rahul Sharma", "department":"IT", "salary":50000.0, "days_present":25, "status":"Eligible"},
    {"id": 2, "name":"Priya Mehta", "department":"HR", "salary":45000.0, "days_present":22, "status":"Regular"},
    
]
idx_counter = len(employees) +1

#-------------------------------
def welcome():
    menu = '''
    [1] Add Employee
    [2] View Employee
    [3] Search Employee
    [4] Update Employee
    [5] Delete Employee
    [6] Calculate Payroll
    [7] Save to JSON
    [8] Load from JSON
    [9] Exit
    [10] Save to text
    [11] Save to CSV
    '''
    print('-'*80)
    print(f"{' Employee Attendance and Payroll Management System ':=^80}")
    print('_'*80)

    print(menu)
    print('*'*80)
    
    
    
# ----------------------------------------
def get_status(days_present):
    status = ''
    if days_present >= 24 :
        status += "Eligible"
    elif days_present >= 20 and days_present < 24 :
        status += "Regular"
    elif days_present >= 15 and days_present < 20:
        status += "Warning"
    elif days_present < 15 and days_present >=0:
        status += "Critical"
    else:
        return
    return status

#------------------------------------

def validate_input(name,department,salary,days):
    if name.strip() == "" or department.strip() == "":
        print("Name and Department Cannot be empty...")
        return False

    if salary <=  0:
        print("Salary Cannot be less than 0")
        return False

    if  days< 0 or days > 26:
        print("days cannot be more than 26")
        return  False

    return  True


def add_employee(employees, next_id):
    name = input("Enter Name of the Employee : ")
    department = input("Enter Department of the Employee : ")
    salary = float(input("Enter Salary : "))
    days_present = int(input("Enter days Present : "))
    status = get_status(days_present)

    if not validate_input(name,department,salary,days_present):
        return next_id

    employees.append(dict(
        id=next_id,
        name=name,
        department=department,
        salary=salary,
        days_present=days_present,
        status=status
    ))

    next_id += 1

    print("Employee Added Successfully.")

    return next_id

    
# ------------------------------

def display_employees(employees):
    if len(employees) == 0:
        print("No employees in database .")
        return

    print('-'*75)
    print(f'{'ID':<5}{'Name':<20}{'Depatment':<15}{'Salary':<10}{'Days Present':<15}{'Status':<15}')
    print('-'*75)
    for e in employees:
        id,name,depart,salary,days,status = e.values()
        print(f'{id:<5}{name:<20}{depart:<15}{salary:<10}{days:<15}{status:<15}')
    print('-'*75)
    
def calculate_payroll(employees):
    print(f"{'Payroll Processed':-^75}")
    for e in employees:
        daily_salary = (e["salary"]/26)
        absent = 26 - e["days_present"]
        deduction = daily_salary * absent
        final = e["salary"] - deduction
        
        print(f'{e["name"]} payroll generated, final salary - {final:.2f}')
        
def save_to_json(filename,employees):
    try:
        with open(filename, mode='w') as file:
            json.dump(employees, file, indent=4)
            
        print("File Updated...")
    except:
        print("Error Occured")
        
        
def load_from_json(filename):
    global employees
    try:
        with open(filename, mode='r') as file:
            employees = json.load(file)
            
            print("Employees Updated ...")
            next_id = len(employees) +1
        return next_id
    except:
        print("Error Occured")
        
def search_employee(employees, emp_id):
    try:
        res = [e for e in employees if e["id"] == emp_id ]
        if not res:
            print("No employee Found")
            return
        id,name,depart,salary,days,status = res[0].values()
        print(f'{id:<5}{name:<20}{depart:<15}{salary:<10}{days:<15}{status:<15}')
        
    except:
        print("Error")

def search_employee_by_name(employees, name):
    try:
        res = [e for e in employees if name.lower() in e["name"].lower()]
        if not res:
            print("No employee Found...")
            return
        display_employees(res)
    except:
        print("Error")

def search_employee_by_dept(employees, dept):
    try:
        res = [e for e in employees if dept.lower() in e["department"].lower()]
        if not res:
            print("No employee Found...")
            return
        display_employees(res)
    except:
        print("Error")

def update_employee():
    try:
        pid = int(input("Enter Emp ID to Update Details : "))

        res = [e for e in employees if e["id"] == pid]

        if not res:
            print("No employee found")
            return

        print('-' * 60)
        print("Current Details of Emp")
        print(f"ID              {res[0]['id']}")
        print(f"Name            {res[0]['name']}")
        print(f"Department      {res[0]['department']}")
        print(f"Salary          {res[0]['salary']}")
        print(f"Days Present    {res[0]['days_present']}")
        print(f"Status          {res[0]['status']}")

        name = input("Enter New Name : ")
        dept = input("Enter New Department : ")
        salary = float(input("Enter New Salary : "))
        days_present = int(input("Enter New Days Present : "))

        new_status = get_status(days_present)

        if not validate_input(name,dept,salary,days_present):
            return

        res[0]["name"] = name
        res[0]["department"] = dept
        res[0]["salary"] = salary
        res[0]["days_present"] = days_present
        res[0]["status"] = new_status

        print("Record Updated Successfully ...")

    except Exception as e:
        print("Error Occured:", e)


def delete_employee(employees,pid):
    res = [e for  e in employees if e["id"] == pid]
    if not res:
        print("NO employee found. ")
        return

    display_employees(res)
    confirmation = input("Are You sure u want to delete (Y/N) : ")
    if confirmation.lower() == "y":
        employees.remove(res[0])
        print("Deleted Successfully ...")
    else:
        return

def save_to_text(employees):
    try:
        with open('employees.txt', mode='w') as file:
            for e in employees:
                line = f'{e["id"]}|{e["name"]}|{e["department"]}|{e["salary"]}|{e["days_present"]}|{e["status"]}\n'
                file.write(line)

        print("Record Updated SuccessFully ...")
    except:
        print("Error")

def load_from_text(employees):
    try:
        with open("employees.txt", mode='r') as file:
            for line in file:
                if line == "":
                    continue

                data = line.split("|")
                employee = {
                    "id": int(data[0]),
                    "name": data[1],
                    "department": data[2],
                    "salary": float(data[3]),
                    "days_present": int(data[4]),
                    "status": data[5]
                }

                employees.append(employee)

        print("Loaded Successfully ...")
    except:
        print("Error")


def load_from_csv(employees):
    try:
        with open("employees.csv", mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                employee = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "salary": float(row["salary"]),
                    "days_present": int(row["days_present"]),
                    "status": row["status"]
                }
                employees.append(employee)
        print("Loaded...")
    except:
        print("error")




def save_to_csv(employees):
    try:
        with open('employees.csv', mode='w') as file:
            fieldnames= ["id","name","department","salary","days_present","status"]
            writer =  csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(employees)

        print("CSV Updated Successfully ")
    except:
        print("Error")


def main():
    global employees
    global filename

    next_id = len(employees)+1

    while True:
        welcome()

        try:
            choice = int(input("Enter Your Choice : "))

            match choice:

                case 1:
                    next_id = add_employee(employees, next_id)

                case 2:
                    display_employees(employees)

                case 3:
                    print("Enter 1 to Search with ID, 2 with Name, 3 with Department.")

                    try:
                        user_choice = int(input("Enter Your Preference : "))

                        if user_choice == 1:
                            pid = int(input("Enter Emp id to Search : "))
                            search_employee(employees, pid)

                        elif user_choice == 2:
                            name = input("Enter Name of Emp to Search : ")
                            search_employee_by_name(employees, name)

                        elif user_choice == 3:
                            dept = input("Enter Dept to Find : ")
                            search_employee_by_dept(employees, dept)

                        else:
                            print("Invalid Search Choice.")

                    except ValueError:
                        print("Please enter a valid number.")

                case 4:
                    update_employee()

                case 5:
                    try:
                        pid = int(input("Enter the Id of Employee : "))
                        delete_employee(employees, pid)

                    except ValueError:
                        print("Invalid Employee ID.")

                case 6:
                    calculate_payroll(employees)

                case 7:
                    save_to_json(filename, employees)

                case 8:
                    next_id = load_from_json(filename)
                case 9:
                    print("Thank you for using the system.")
                    break

                case 10:
                    save_to_text(employees)

                case 11:
                    save_to_csv(employees)
                case 12:
                    load_from_text(employees)
                case 13:
                    load_from_csv(employees)

                case _:
                    print("Invalid Choice.")

        except ValueError:
            print("Invalid input. Please enter a number.")

        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break
if __name__ == '__main__':
    main()
