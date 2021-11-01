deposit = input("Please Enter deposit \n")
precent= input("Please Enter the precent per year \n")
year = input("Please Enter for how many year woyld like to deposit \n")

deposit=int(deposit)
precent=int(precent)
year=int(year)
100 # todo: not needed digit
NewValue = deposit
i=0
while i<year:
    NewValue=NewValue*((1+precent/100)) # todo: operator *= can be used
    i+=1

print ("After {0} years the deposit will be worth {1} ".format(year,NewValue))