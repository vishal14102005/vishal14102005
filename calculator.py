                #    Simple Calculator
while True:

    x = float(input("Enter First Number: "))

    y = float(input("Enter Second Number: "))

    print("Select Operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    o = input("Enter Your Choice(1/2/3/4/5): ")

    if (o == "1") :
        print("Sum Of These Numbers is =",x+y)
    elif (o == "2"):
        print("Substraction of these Numbers is =",x-y)
    elif (o == "3"):
        print("Multiplication Of These Numbers is =",x*y)
    
    elif (o == "4"):
        try:
            y != 0
            print("Division Of These Numbers is =",x/y)
        except ZeroDivisionError as e:
            print(f"Zero Divison Error:{e}")
    elif(o == "5"):
        print("Exiting Calculator, GoodBye")
        break
    else:
        print("Invalid Operator")