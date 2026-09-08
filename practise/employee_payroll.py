import json

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

def add_employee(employees, next_id):
    name = input("Enter Name of the Employee : ")
    department = input("Enter Department of the Employee : ")
    salary = float(input("Enter Salary : "))
    days_present = int(input("Enter days Present : "))
    status = get_status(days_present)

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
def main():
    global employees
    global filename
    next_id = len(employees) +1
    while True:
        welcome()
        
        choice= int(input("Enter Your Choice : "))
        
        match(choice):
            case 1:
                next_id = add_employee(employees,next_id)
            case 2:
                display_employees(employees)
            case 3:
                pid = int(input("Enter Emp id to Search : "))
                search_employee(employees,pid)
            case 6:
                calculate_payroll(employees)
            case 7:
                save_to_json(filename,employees)
            case 8:
                next_id = load_from_json(filename)
            case 9:
                break
            case _:
                print("Invalid Input")
                
                
if __name__ == '__main__':
    main()