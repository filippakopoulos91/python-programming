total = 0
grade = 0

print("Enter ten grades")

for i in range(1, 11):
    if (grade >= 0) and (grade <= 20):
        grade = float(input(""))
        total += grade
        avg = total / 10 # avg stands for average
    else:
        print("Invalid value! Enter again!")
        grade = float(input(""))
        total += grade
        avg = total / 10 
            
print("The average grade is %.2f" % avg)   
