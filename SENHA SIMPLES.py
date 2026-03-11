# SENHA SIMPLES
# 10/03/2026

print('############### COFRE DO BANCO ##################') 

senha = 'python-safadão'
print('>>>>>>>>>>>>>>>> ', senha, ' <<<<<<<<<<<<<<<<<<<<<') 

tentativa = input('Digite a Senha SECRETA para entrar no cofre: ') 

if (tentativa == senha) :
    print('ACESSO LIBERADO') 
    
else:
    print('ACESSO NEGADO')
    
input() 