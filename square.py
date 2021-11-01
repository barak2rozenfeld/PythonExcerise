import math

a = input("Please Enter the length of the square \n")
a=int(a)
perimiter=a*4
diagonal = a*math.sqrt(2)

print("The perimiter of the square is:{0} and the diagonal is:{1}".format(perimiter,diagonal))
#todo: there is another kind of formatting strings. Look at this:
print(f'The perimeter of the square is: {perimiter} and the diagonal is {diagonal}')