# MAIOR OU MENOR DE IDADE
# 10/03/2026

print('################### MAIOR OU MENOR DE IDADE ######################') 

id = input(' Digite a sua idade: ')
id = int(id)

if (id < 18) :
    print('\n Menor de Idade >> Acesso Negado')
    
elif (id > 18) :
    print('\n Maior de Idade >> Acesso Liberado') 
    
else:
    print('\n Passou por pouco >> Acesso Liberado') 
    
input() 