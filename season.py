month= input("Please enter a month \n")
month= int(month)
if (((month>1) and (month <2)) or (month==11) or (month==12)):
    print("It is winter time")
elif(month>=3 and month<=5):
    print("it is spring time")
elif (month >5 and month <9):
    print ("is is summer time")
elif (month >9 and month <11):
    print ("it is authon time")
