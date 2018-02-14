import datetime
year = input("give me the year: ")
month = input("give me the month: ")
if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    stop = 31
elif (month == 4 or month == 6 or month == 9 or month == 11):
    stop = 30
else: #month == 2
    if (year % 4 == 0 and year % 100 != 0):#elegxw an ena etos
        stop = 29                         #einai disekto
    elif (year % 400 == 0):                #opou tote tha exei 
        stop = 29                         #29 hmeres
    else:                                  #enw alliws tha exei 
        stop = 28                         #28
for i in range (1,stop + 1):
    d = datetime.date(year, month , i)
    print d.weekday()

print "S","\t","M","\t","T","\t","W","\t","T","\t","F","\t","S","\t"

