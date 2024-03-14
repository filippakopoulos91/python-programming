def factorial():

    n = int(input("Number: "))

    factorial = 1

    if n == 0:
        print("0! = 1")
    elif n > 0:
        for i in range(1, n + 1):
            factorial *= i
        print(n, "! = ", factorial)
    else:
         while n < 0:
            user_input = input("Negative numbers don't have factorial. Do you want to re-enter? (yes/no): ")
            if user_input.lower() in ["yes", "y"]:
                n = int(input("Number: "))
                if n == 0:
                    print("0! = 1")
                elif n > 0:
                    for i in range(1, n + 1):
                        factorial *= i
                    print(n, "! = ", factorial)
            else:
                break

factorial()
