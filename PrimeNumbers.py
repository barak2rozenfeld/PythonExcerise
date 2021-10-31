


num=1
while (num<1000):
    flag = False
    for i in range(2, num):

        if (num % i) == 0:
            flag = True
            break


    if flag==False:
        print(num, "is a prime number")
        #print(num, "is not a prime number")
    #else:
    num+=1
