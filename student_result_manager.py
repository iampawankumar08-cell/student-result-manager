student = {}

while True:
    print("/n----Student Manager App----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add student
    if choice == "1":
        name = input("Enter student name :")
        marks = int(input("Enter Marks :"))
        student[name] = marks
        print(f"{name} Successfully Added")    
                  
    #view student
    elif choice == "2":
        if not student:
            print("no student found")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    #check result
    elif choice == "3":
        name = input("enter student name: ")

        if name in student :
            marks = student[name]

            if marks >= 40:
                print("Pass")

            else:
                print("reappear")

        else:
                print("student not found")

    #exit
    elif choice == "4":
        print("exiting....")
        break

    else:
        print("in-valid output")
