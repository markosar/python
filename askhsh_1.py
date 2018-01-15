def search(r,m):##sequential search opws thn mathame sto lykeio(se python of course)
    done = False # brethke to stoixeio;
    position = -1 ## arxikopoiw thn thesi tou stoixeiou pou anazhtw sthn lista 
    i = 0
    while (i < len(m) and done == False):##na mhn bgw ektos oriwn ths listas kia elegxw pws den vrethike akomh to stoixeio
        if(m[i]== r):
            done = True
            position = i
        else:
            i += 1
    return position        


import random
s = 0 ## to s einai to athroisma twn forwn pou trexei to paixnidi mexri kapoios na pei "bingo"
for game in range(1000):
    l = []
    N = 5
    for i in range(100):
        l.append([])
        for j in range(N):
            z = random.randint(1,80)
            ##parakatw einai o xeirokinhtos tropos pou den einai kai toso praktikos
            ##z = int(input('Choose a number(from 1 to 80): '))
            ##while(z < 1 or z > 80):
                ##print "Wrong input.Give again..."
                ##z = int(input('Choose a number(from 1 to 80): '))
            l[i].append(z)
    print "h lista me tous arithmous twn paixtwn einai: "
    print l
    m = []
    for i in range(1,81):
         m.append(i)
    bingo = False #elegxw an eipe kaneis bingo
    fores = 0 ##poses fores trexei to paixnidi 
    while(bingo == False and len(m) > 0):
        r = random.choice(m)
        print r # ektypwnw tonarithmo poy "epelexe" to pc
        p = search(r,m)
        if (p!= -1):
            del m[p]
        print m #ektypwnw thn lista tou pc meta thn afairesh toy prohgoymenoy arithmoy
        for i in l:
            p1 = search(r,i)
            if (p1 != -1):
                del i[p1]
            if (i == []):## an kapoia lista twn paixtwn einai kenh..."bingo"
                bingo = True
            ## apenergopihste to sxolio apo thn epomenh grammh gia na deite tis listes twn paixtwn se kathe "gyro" tou paixnidiou
            ##print i
        fores += 1
    s += fores
print s/1000 ##emfanizw to meso oro 
        
            
                
