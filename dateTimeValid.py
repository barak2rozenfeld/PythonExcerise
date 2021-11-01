y = int(input("Year: \n"))
m = int(input("Month: \n"))
d = int(input("Day: \n"))


day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y%4==0 and (y%100 != 0 or y%400==0):
    day_count_for_month[2] = 29 # todo: good solution to check leap year or not)

if (y>0 and m<13):
    if (d<=day_count_for_month[m]):
        print ("This Date is valid")
    else:
        print ("This date is not valid")
else:
    print ("this date is not valud.")

