length_list= int(input("Please enter how many numbers you add to list \n"))

m_list =[]
m_list_indexes=[]
n=0
while (n<length_list):
     x= int(input("Enter the " + str(n)+" Number to list \n"))
     m_list.append((x))
     m_list_indexes.append(n)
     n+=1


total_list=list(zip(m_list,m_list_indexes))
print ("this is the total list with it's indexes \n")
print total_list

