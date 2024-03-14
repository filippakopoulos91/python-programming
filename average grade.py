def avgGrade():
    total = 0

    for i in range(1, 11):
        print("Test", i)
        grade = float(input("Enter the test's grade: "))
        print("\n") #add a blank line before entering the next grade
 
        while(grade > 20) or (grade < 0):
            print("Test", i)
            grade = float(input("Invalid value! Enter again.\n"))
            print("\n") #add a blank line if the above error message needs to repeat
            
        total += grade
    print("The average grade is ", total / 10)

avgGrade()
