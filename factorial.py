n1 = int(input("Give the first integer number: "))

#number check and factorization of the first given number

factorial = 1

if n1 < 0:         
    print("Negative numbers don't have factorial!")
elif n1 == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n1 + 1):
        factorial = factorial * i
   
    print("The factorial of", n1, "is", factorial)

n2 = int(input("Give the second integer number: ")) 

#number check and factorization of the second given number

factorial = 1

if n2 < 0:
    print("Negative numbers don't have factorial!")
elif n2 == 0:
    print("The factorial of 0 is 1")
else:
    for y in range(1, n2 + 1):
        factorial = factorial * y
   
    print("The factorial of", n2, "is", factorial)

n3 = int(input("Give the third integer number: "))

#number check and factorization of the third given number

factorial = 1

if n3 < 0:
    print("Negative numbers don't have factorial!")
elif n3 == 0:
    print("The factorial of 0 is 1")
else:
    for x in range(1, n3 + 1):
        factorial = factorial * x
   
    print("The factorial of", n3, "is", factorial)
