f=open('input.txt','r')
execution=0
Old_murk_eye_attack=2
Bluegill_warrior_attack=2

HP=[]
l=[]
for line in f:
    if str.isdigit(line[:1])==True:
        l.append(line[:1])
        HP.append(line[-3:])
a=0
b=0
c=0
for i in range(1,int(l[0])+1):
    f.seek(0)
    a=a+int(l[i])
    b=a-int(l[i])+i+1
    c=a+i+1
    Old_murk_eye_number=0
    Muloc_Warleader_number=0
    Bluegill_Warrior_number=0

    for j in range(int(l[i])):
        f.seek(0)
        if f.readlines()[b:c][j].strip('\n')=='Old Murk-Eye':
            Old_murk_eye_number+=1
        f.seek(0)
        if f.readlines()[b:c][j].strip('\n')=='Muloc Warleader':
            Muloc_Warleader_number+=1
        f.seek(0)
        if f.readlines()[b:c][j].strip('\n')=='Bluegill Warrior':
            Bluegill_Warrior_number+=1

#    print Old_murk_eye_number,Muloc_Warleader_number,Bluegill_Warrior_number

    execution=Old_murk_eye_number*(Old_murk_eye_attack+int(l[i])-1)+Bluegill_Warrior_number*Bluegill_warrior_attack+Muloc_Warleader_number*2*(Bluegill_Warrior_number+Old_murk_eye_number)

#    print execution,int(HP[i])

    if int(HP[i])<=execution:
        print 'Mrghllghghllghg!'
    else:
        print 'Tell you a joke, the execution of Paladin.'