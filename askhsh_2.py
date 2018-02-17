import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
mynums=[]
for i in range(10):
    newnum = input("Give me a number(between 1-80): ")#numbers between 1-80
    while newnum < 1 or newnum > 80:
        print "WRONG INPUT.TRY AGAIN"
        newnum = input("Give me a number(between 1-80): ")
    mynums.append(newnum)
wins = []
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(mynums,tmp))
    wins_of_day = 0
    for n in r:
        if n > 4:# an oi arithmoi pou petixa einai panw apo 4 
            wins_of_day += 1# tote ua eixa mia akomh pithanothta na kerdisw authn thn mera
    wins.append(wins_of_day)#edw gemizei h lista pou periexei to plithos twn epituxiwn pou exw kathe mera tou perasmenou mhna
max = max(wins)#poia mera tha eixa tis perissoteres pithanothtes na exw kerdisei
k = wins.index(max)#pou vrisketai to max
N = k + 1
date_N_days_ago = datetime.datetime.now() - datetime.timedelta(N)
print "You would have been lucky, if you had played on:",date_N_days_ago.strftime("%d-%m-%Y")
