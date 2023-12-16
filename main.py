def calculate():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print('''Enter + for addition operation\n
        enter - for subtract operation\n
        enter * for multiplication operation\n
        enter / for division operation\n'''
          )
    operation = input("Enter the operation to be performed : ")
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        if b == 0:
            print("ERROR : Zero can't be in denominator")
        else:
            print(a / b)


if __name__ == '__main__':
    calculate()
    more = True
    while more:
        conti = input("Want to continue the calculation press yes else print no : ").lower()
        if conti == 'no':
            break
        else:
            calculate()
