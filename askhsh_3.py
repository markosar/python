keimeno = input("give me a text: ")
keimeno = keimeno.split()
print keimeno
P =""
for lexi in keimeno:
    l = []
    for i in range(len(lexi)):
        ascii = ord(lexi[i])
        print ascii
        if(ascii >= 65 and ascii <= 90):
            if(ascii<= 77):
                ascii+=13
            else:
                apostash_Z = 90 - ascii
                diafora = 13 - apostash_Z
                ascii = 64 + diafora
        elif(ascii >= 97 and ascii<= 122):
            if(ascii<= 109):
                ascii+=13
            else:
                apostash_z = 122 - ascii
                diafora = 13 - apostash_z
                ascii = 96 + diafora
        l.append(chr(ascii))
    p = ""
    for i in l:
        p +=i
    p +=" "
    print p
    P +=p
print P

