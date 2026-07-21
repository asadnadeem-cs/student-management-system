#Main Menu: User Chooses the function to use.
def main():
    #Loop runs the function till 10(exit) is choose.
    while True:
        print  ("1. Add Student")
        print  ("2. View Students")
        print  ("3. Search Student")
        print  ("4. Update Student")
        print  ("5. Delete Student")
        print  ("6. Average age ")
        print  ("7. Toppers")
        print  ("8. Total Students")
        print  ("9. Back Up")
        print  (f"{'10. Exit'}\n")    
        #I have applied the iterate_input() function here .
        #It will check if the field is empty and ask user for input again and again till field is not empty.
        choose = iterate_input(input("Choose: "))
        find_function(choose)             

#This function calls the function that use choosed.
def find_function(choose):
    match choose:
        case "1":
            add_student()
        case "2":
            view_students()
        case "3":
            search_student()
        case "4":
            update_student()
        case "5":
            delete_student()
        case "6":
            average_age()
        case "7":
            toppers_list()
        case "8":
            total_students()
        case "9":
            stbackup()
        case "10":
            exit()
        #If any value other than these is choosed case _: prints invalid
        case _:
            print("Invalid")   

#This function is used to add a new student.
def add_student():
    #file is opened as append so it adds the student at last line.
    with open("student.txt","a") as  file:
        #iterate_input() is used again.
        student_id = iterate_input(input("Enter ID: "))
        #id_duplicate() is used to check if entered id is already in the file or not.
        flag = id_duplicate(student_id)
        #if flag is false then other details are asked for input.
        if not flag:
            #file.write() writes the details in file.
            file.write(student_id)
            file.write(",")
            name = iterate_input(input("Enter Name: "))
            file.write(name)
            file.write(",")                   
            age = iterate_input(input("Enter Age: "))
            file.write(age)
            file.write(",") 
            grade = iterate_input(input("Enter Grade: "))
            #grade is capitalized so can be used to find toppers later.
            grade = grade.capitalize()
            #(f"{}\n") used so that the cursor moves to secound line.
            file.write(f"{grade}\n")
            print("Student Added Auccessfully!")
        #if id alreaady exists in file else is executed.              
        else:
                print("ID Already Exists")

#This function is used to see all students and their details.
def view_students():
    #try and except is used if file does not exist.
    try:
        with open("student.txt","r") as file:
            for line in file:
                line2 = line.rstrip()
                student_id , name , age , grade = line2.split(",")
                print("ID:",student_id)
                print("Name:",name)
                print("Age:",age)
                print("Grade:",grade)
    except FileNotFoundError:
        print("Student Not Found.")

#This function is used to search a specific student through id and see his details.
def search_student():
    try:
        with open("student.txt","r") as file:
            student_id = iterate_input(input("Enter ID: "))   
            #flag is used to see if student is found or not after lines are executed.
            flag = False
            for line in file:
                    #strip() is used so all unwanted spaces are removed from left and right.
                    line_1 = line.strip()
                    #split() is used to split all details.
                    student_id2 , name , age , grade = line_1.split(",")
                    if student_id == student_id2:
                        print(f"{'Student Found'} \n")
                        print("ID:",student_id)
                        print("Name:",name)
                        print("Age:",age)
                        print("Grade:",grade)
                        flag = True
                        break
            if not flag:
                print("Student Not Found")                 
    except FileNotFoundError:
        print("No Student Found.")

#This function is used to update a previous student details.
def update_student():
    try:
        #file is read and stored in lines because we can not directly read and write at the same time in a file.
        with open("student.txt","r") as file:
            lines = file.readlines()
            student_ID = input("Enter ID: ")
            #flag is used to see if student is found or not after lines are executed.
            flag = False
            if not flag:
                #enumirate() is used with i so we know which line to update.
                for i, line in enumerate(lines):
                    line_2 = line.strip()
                    student_ID2 , name , age , grade = line_2.split(",")
                    if student_ID == student_ID2:
                        flag = True
                        break
            if not flag:
                print("Student Not Found") 
                #return is used if no student found to update to get out of the function.    
                return             
        with open("student.txt","w") as file:                                       
            student_id3 = input("Enter ID: ")
            #id_duplicate is used to see if id already exists.
            if not id_duplicate(student_id3):
                newname = input("Enter new Name: ")
                newage = input("Enter new Age: ")
                newgrade = input("Enter new Grade: ")
                #details are stored in line on index i and then written in file.
                lines[i] = f"{student_id3},{newname},{newage},{newgrade}\n"
                print("Student Updated Successfully")
                for line in lines:
                    file.write(line)        
    except FileNotFoundError:
         print("No Studnets Found")

#This function is used to delete a student.
def delete_student():
    try:
        #file is read and stored in lines because we can not directly read and write at the same time in a file.
        with open("student.txt","r") as file:
            lines = file.readlines()             
        student_ID = input("Enter ID: ")
        #flag is used to know if we find the student to delete.
        flag = False
        if not flag:
            for i, line in enumerate(lines):
                line_2 = line.strip()
                student_ID2 , name , age , grade = line_2.split(",")
                if student_ID == student_ID2:
                    flag = True
                    #del lines(i) is used to del the line of student details
                    del lines[i]
                    print("Student Deleted Successfully")
                    break                    
            if not flag:
                print("Student Not Found")
                return
        #line is deleted from lines and then written in file.
        with open("student.txt","w") as file:
            for line in lines:
                file.write(line)           
    except FileNotFoundError:
        print("No Student Found")

#This function checks if a field is left empty.
def empty_field(n):
    if n == "":
        return True
    else:
        return False
    
#This funtion calls empty_field() to check if a field is left empty. 
def iterate_input(n):
    if empty_field(n):
        #if field is empty it asks for input again and again till field is not empty.
        while True:       
            n = input("Enter again ")          
            if not empty_field(n):
                return n              
    return n

#This function checks if the enterd id already exists in file.
def id_duplicate(n):
    try:
        with open("student.txt","r") as file:
            for line in file:
                line_2 = line.strip()
                student_id2 , name , age , grade = line_2.split(",")
                if student_id2 == n:
                    return True     
    except FileNotFoundError:
        return False            

#This funtions is used to calculate the total number of students in the file.
def total_students():
 try:
        with open("student.txt","r") as file:
            lines = file.readlines()  
        #len() is used to find total lines because each line equals one student.     
        i = len(lines)
        print("Total Students: ",i)
 except FileNotFoundError:
     print("No Student Found")

#This function is used to find the average age of all the students in the file.
def average_age():
    total = 0
    try:  
        with open("student.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                student_id, name , age , grade = line.strip().split(",")
                #age contains string so int() is used to add it into total.
                total = total + int(age)
            average = total/len(lines)
            print("Average Age: ",average) 
    except FileNotFoundError:
            print("No Student Found")
    #zerodivisionerror is handled if file contains no lines.
    except ZeroDivisionError:
        print("No Student Found")

#This funcction is used to find toppers in the file.
def toppers_list():
    try:
        with open("student.txt","r") as file:
            lines = file.readlines()
        #c is used to count toppers if no toppers found in file then "Student Not Found" is printed.
        c = 0
        for line in lines:
            student_id , name , age , grade = line.strip().split(",")          
            if grade == "A*":
                print("ID: ",student_id)
                print("Name: ",name)
                print("Age: ",age)
                print("Grade: ",grade)
                c+=1
            else:
                continue
        if c == 0:
            print("Student Not Found")
            return
    except FileNotFoundError:
        print("No Student Found")

#This functions is used to back-up the file into student_backup.txt.
def stbackup():
    try:
        with open("student.txt","r") as file:
            lines = file.readlines()
        with open("student_backup.txt","w") as file:
            for line in lines:
                file.write(line)
    except FileNotFoundError:
        print("No Students Found")

#Main is called at the end to start the Student Management System.
if __name__=="__main__":
    main()
