import random
s = 0 ## to s einai to athroisma twn forwn pou trexei to paixnidi mexri kapoios na pei "bingo"
for game in range(1000):
    l = []              #dhmiourgw mia lista
    for i in range(100):
        l.append([])#pou tha periexei tis 100 listes opou kathe mia tha periexei tous 5 arithmous twn 100 paiktwn
        j = 0
        while (j < 5):
            z = random.randint(1,80)
            if z not in l[i]:#elegxw pws den exw xana valei ton arithmo z sthn ekastote lista mou
                l[i].append(z)
                j+=1         
    print "h lista me tous arithmous twn paixtwn einai: "
    print l
    m = []
    for i in range(1,81):
        m.append(i)#dhmiourgia lista m me tous arithmous 1,2,3,...,80
    bingo = False #elegxos gia to an eipe kaneis bingo
    fores = 0 ##poses fores trexei to paixnidi 
    while(bingo == False and len(m) > 0):
        r = random.choice(m)#tuxaia epilogh arithmou apo thn lista m
        print r # ektypwnw ton arithmo poy "epelexe" to pc
        p = m.index(r)#pou einai to r 
        del m[p]#diagrafh tou r apo thn lista m
        print m #ektypwnw thn lista tou pc meta thn afairesh toy prohgoymenoy arithmoy
        for i in l:
            if r in i:#an uparxei to r sthn ekastote lista
                p1 = i.index(r)#vres thn thesi tou
                del i[p1]#kai diegrapse to  
            if (i == []):## an kapoia lista twn paixtwn einai kenh..."bingo"
                bingo = True
        fores += 1
    s += fores
print s/1000 ##emfanizw to meso oro

