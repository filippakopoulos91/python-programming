sum = 0

while True:
    num = float(input("Enter any number [zero to stop]: "))
    if num != 0:
        sum += num
        print("Total: %.2f" % sum)
    else:
        print("You entered zero!")
        break
