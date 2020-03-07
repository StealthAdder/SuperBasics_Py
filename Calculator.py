num1 = input("Enter number ")
num2 = input("Enter another number ")
op = input("Enter an operator ")

if(op == "+") :
    solve = int(num1) + int(num2)
elif (op == "-") : 
    solve = int(num1) - int(num2)
elif(op == "*") :
    solve = int(num1) * int(num2)
elif(op == "/") :
    solve = int(num1) / int(num2)
else:
    print("Check for operator")
print("VALUE = " + str(solve))
