def manage_student_database():
    students=[]
    studentId=1
    while True:
        name=input("Please enter the student's name (or type 'stop' to finish):").strip()
        if name.lower()=='stop':
            break
        if any(student[1] == name for student in students):
            print(f"Student with name '{name}' is already in the database.")
            continue
        students.append((studentId,name))
        studentId+=1
        
    print('\n--- Complete list of students')
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}")
                
    print(f' \n Total number of students: {len(students)}')
    
    
    totalStudentsNameLength=sum(len(student[1]) for student in students)
    print(f'\n Total Length of student names:{totalStudentsNameLength}')
    
    if(students):
        maxLengthName=max(students,key=lambda s:len(s[1]))
        print(f"Student with the longest name: {maxLengthName[1]} (ID: {maxLengthName[0]})")

        # Find the student with the shortest name
        shortest_name_student = min(students, key=lambda s: len(s[1]))
        print(f"Student with the shortest name: {shortest_name_student[1]} (ID: {shortest_name_student[0]})")
manage_student_database()