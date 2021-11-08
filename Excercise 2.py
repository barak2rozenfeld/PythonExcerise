lst = []
n = int (input("Please Enter the total list of numbers:\n"))

for i in range(0,n):
    num= int(input("Please Enter Number " + str(i+1)  + ":\n"))
    lst.append(num)

sum=0

for i in range (len(lst)):
    sum+=lst[i]

print("the Sum of the list is: " + str(sum) +"\n")

min_val=lst[0]
min_index=0
max_val=lst[0]
max_index=0
for i in range(len((lst))):
    if (lst[i]<min_val):
        min_val=lst[i]
        min_index=i
    if (lst[i]>max_val):
        max_val=lst[i]
        max_index=i

print ("The Minimum Number Is: " +str(min_val) +" And The Position Is:" +str(min_index+1))
print ("The Maximum Number Is: " +str(max_val) +" And The Position Is:" +str(max_index+1))

lst_odd =[]
lst_even=[]

for i in (range (len(lst))):
    if (lst[i]%2==0):
        lst_even.append((lst[i]))
    else:
        lst_odd.append((lst[i]))

print ("the list for even numbers")
print (lst_even)
print  ("the list for odd numbers")
print (lst_odd)

