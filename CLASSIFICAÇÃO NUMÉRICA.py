# NÚMERO POSITIVO, NEGATIVO OU ZERO
# 10/03/2026

print('#################### Classificação Numérica ######################') 

x = input('\n Digite um número para ser classificado entre: \n .Positivo \n .Negativo \n .Zero \n .O número é: ') 
x = int(x) 

if (x > 0) :
    print('\n O número', x, ' é positivo.') 
    
elif (x < 0) :
    print('\n O número', x, ' é negativo.')
    
else:
    print('\n O número é Zero') 
    
input()  