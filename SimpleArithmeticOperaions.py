x = input("Plese enter first number \n")
y = input("Please enter a secound number \n")
oper = input ("Please Enter an simple arithmetic operation (+,*,-,/) \n")
x = int(x)
y = int(y)

if (oper=="+"):
    res = x + y
    print(res)
elif(oper=="*"):
    res =x * y
    print(res)
elif(oper=="-"):
    res = x - y
    print(res)
elif(oper=="/"):
    res = x/y
    print(res) # todo: what about divizion by zero?
else:
    print("operation is no valid")

input("Press Enter to exit the program")

# todo: there is a good solution without if statement (using eval function)
