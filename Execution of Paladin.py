execution=0
Old_murk_eye_attack=2
Bluegill_warrior_attack=2

#input_Murloc=['Old Murk-Eye','Coldlight Oracle','Muloc Warleader','Bluegill Warrior']
#HP=16
f=open('input.txt','r')
#f.readline()
#print f.readline()
Old_murk_eye_number=0
Muloc_Warleader_number=0
Bluegill_Warrior_number=0

i=0
num=int(f.readline(1))+1

for i in range(num):

    if f.readline()=='Old Murk-Eye\n':
       	Old_murk_eye_number+=1
f.seek(0)
for i in range(num):
    if f.readline()=='Muloc Warleader\n':
        Muloc_Warleader_number+=1
f.seek(0)
for i in range(num):
    if f.readline()=='Bluegill Warrior\n':
        Bluegill_Warrior_number+=1

f.seek(0)

#print Old_murk_eye_number,Muloc_Warleader_number,Bluegill_Warrior_number

execution=Old_murk_eye_number*(Old_murk_eye_attack+int(f.readline(1))-1)+Bluegill_Warrior_number*Bluegill_warrior_attack+Muloc_Warleader_number*2*(Bluegill_Warrior_number+Old_murk_eye_number)

f.seek(2)

if int(f.readline())<execution:

    print 'Mrghllghghllghg!'

else:

    print 'Tell you a joke, the execution of Paladin.'