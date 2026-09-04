import json

students = [
    {"id": 1, "name": "Abhinav", "course": "Python core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Rahul", "course": "Python core", "marks": 76.0, "grade": "B"},
    {"id": 3, "name": "Priya", "course": "Data Science", "marks": 92.5, "grade": "A"},
    {"id": 4, "name": "Ananya", "course": "Web Development", "marks": 84.0, "grade": "B"},
    {"id": 5, "name": "Vikram", "course": "Python core", "marks": 69.5, "grade": "C"}
]
id_counter = len(students)

filename = 'students.json'

def menu():
    menu = '''
    1. Enroll Student
    2. Cohort Directory
    3. Query Records
    4. Revise Evaluation
    5. Purge Record
    6. Save to JSON
    7. Load from JSON
    8. Terminate
    '''
    print('*'*60)
    print(f"{'Welcome To Student Record Management System...':^60}")
    print('*'*60)
    print(menu)
 
def grade_cal(marks):
    grade = ""
    if marks >= 85.0:
        grade+='A'
    elif marks >= 70.0 and marks <= 85.0:
        grade+= "B"
    elif marks >= 50.0 and marks<= 70.0:
        grade += "C"
    else:
        grade+= "F"
    return grade 
    
def enroll_students():
    global id_counter
    
    try:
        name = input("Enter Students Name : ")
        course = input("Enter course name : ")
        
        if name == '' or course == '':
            print("Name and course cannot be empty")
            return
        marks = float(input("Enter marks : "))
        if marks not in range(0,100+1):
            print("Makrs should be in range 0 - 100")
            return
        student_id = id_counter + 1
        student_grade = grade_cal(marks)
        
        students.append(dict(id=student_id,name=name,course=course,marks=marks,grade=student_grade))
        
        print("Record Added Successfully ...")
    except:
        print("Error Occured")
        
    
def list_students():
    if len(students) == 0:
        print("No students in database !")
        return
    elif len(students) == 1:
        print_one_student(students[0])
    else:
        print_all_students(students)
        
def print_one_student():
    pass

def print_all_students(student_list):
    print('_'*75)
    print(f'{'ID':<5}{"Candidate Name":<20}{"Course/Module":<20}{"Marks(100)":<15}{"Awarded Grade":<10}')
    print('_'*75)
    for student in student_list:
        id,name,course,marks,grade = student.values()
        print(f'{id:<5}{name:<20}{course:<20}{marks:<15}{grade:<10}')
    print('_'*75)
    
        
def main():
    while True:
        menu()
        print('_'*60)
        choice = int(input("Enter Your Choice : "))
         
        match(choice):
            case 1 :
                enroll_students()
            case 2:
                list_students()
            case 3:
                pass
            case 4:
                pass
            case 6:
                save_to_json()
            case 7:
                load_from_json()
            case 8:
                break
            case _ :
                print("Invalid")
         

def save_to_json():
    global filename
    try:
        with open(filename,mode="w") as file:
            json.dump(students, file)
        print("File Saved ...")
    except:
        print("Error saving in file ... ")

def load_from_json():
    global filename
    global students
    try:
        with open(filename, mode="r") as file:
            students = json.load(file)
            print("Students data loaded from database")
    except:
        print("Error Occured")




if __name__ == '__main__':
    main()