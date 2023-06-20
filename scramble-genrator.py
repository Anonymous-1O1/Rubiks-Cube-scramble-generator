import random

notations=["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]
scramble=[]

def generator(a,b):
    x=random.randint(a,b)
    scramble.append(notations[x])

def generator_2(a,b,c,d):
    x=random.randint(a,b)
    y=random.randint(c,d)
    z=random.randint(1,2)
    if z==1:
        scramble.append(notations[x])
    else:
        scramble.append(notations[y])
for num in range (0,20):
    if num==0:
        a=0
        b=17
        generator(a,b)
    else: 
        if scramble[num-1]=="R" or scramble[num-1]=="R'" or scramble[num-1]=="R2":
            generator(3,17)
        elif scramble[num-1]=="B" or scramble[num-1]=="B'" or scramble[num-1]=="B2":
            generator(0,14)
        elif scramble[num-1]=="L" or scramble[num-1]=="L'" or scramble[num-1]=="L2":
            generator_2(0,2,6,17)
        elif scramble[num-1]=="U" or scramble[num-1]=="U'" or scramble[num-1]=="U2":
            generator_2(0,5,9,17)
        elif scramble[num-1]=="D" or scramble[num-1]=="D'" or scramble[num-1]=="D2":
            generator_2(0,8,12,17)
        else:
            generator_2(0,11,15,17)
print(" ".join(scramble))