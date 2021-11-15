length_list= int(input("Please enter how many numbers you add to list \n"))

m_list =[]
n=0
while (n<length_list):
     x= int(input("Enter the " + str(n)+" Number to list \n"))
     m_list.append((x))
     n+=1
unique_list=[]
for i in m_list:
    cnt=0
    for j in m_list:
        if (i==j):
            cnt+=1
    if (cnt==1):
        unique_list.append(i)
    if (cnt>1):
        exits=0
        for j in unique_list:
            if (j==i):
                exits=1
        if (exits==0):
            unique_list.append(i)

print (unique_list)

