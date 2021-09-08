# meten is weten
# twee getallen vergelijken

getal_1 = int(input('Schrijf hier getal 1: '))
getal_2 = int(input('Schrijf hier getal 2: '))
max = int()
min = int()
same = int()

if getal_1 > getal_2:
    max = getal_1
    min = getal_2
    print(f'Het maximum is: {max}.')
    print(f'Het minimum is: {min}.')
else:
    max = getal_2
    min = getal_1
    print(f'Het maximum is: {max}.')
    print(f'Het minimum is: {min}.')    
  

####################################
######   VORIGE UITBREIDING   ######
####################################
#if getal_1 > getal_2:
#    max = getal_1
#    print(f'Getal 1 is het grootste getal: {max}.')
# elif getal_1 < getal_2:
#    min = getal_2
#    print(f'Getal 1 is het kleinste getal: {min}.')
#else:
#    if getal_1 == getal_2:
#      same = getal_1
#      print(f'Getal 1 en getal 2 zijn even groot: {same}')
    




   
    

