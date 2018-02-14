keimeno = input("give me some text(in quotes please): ")
keimeno = keimeno.split()## xwrizw to keimeno se lexeis
P =""##arxikopoihsh kainourgias protashs
for lexi in keimeno:##gia kathe lexi
    l = []##dhmiourgw kenh lista
    for i in range(len(lexi)):
        ascii = ord(lexi[i])##h antistoixhsh tou kathe grammatos ston kwdika ascii tou
        if(ascii >= 65 and ascii <= 90):##an einai kefalaio gramma
            if(ascii<= 77):##an to gramma einai mexri kai to gramma M
                ascii+=13##kanw + 13 sto antistoixo ascii
            else:##an einai apo to N kai meta
                apostash_Z = 90 - ascii##ypologizw thn apostash tou ascii tou apo to ascii tou Z(90)
                diafora = 13 - apostash_Z##afairw auth th apostash apo to 13 kai thetw to ascii tou xarakthra
                ascii = 64 + diafora##iso me to athroisma tou ascii tou prohgoumenou grammatos apo to A + thn diafora auth
        elif(ascii >= 97 and ascii<= 122):##an prokeitai gia mikro gramma
            if(ascii<= 109):##akolouthw thn antistoixh methodologia
                ascii+=13
            else:
                apostash_z = 122 - ascii
                diafora = 13 - apostash_z
                ascii = 96 + diafora
        l.append(chr(ascii))##antikathistw ta palia grammata me ta kainourgia se ROT13 apothikeyontas ta se mia lista
    p = ""##dhmiourgia ths neas lexis
    for i in l:##kathe gramma ths listas
        p +=i##prosthsese to sthn nea lexi
    p +=" "##prosthese ena keno meta thn kathe lexi
    P +=p##prosthese sthn nea protash thn nea lexi me to keno sto telos
print P##emfanizw thn kainourgia protash
