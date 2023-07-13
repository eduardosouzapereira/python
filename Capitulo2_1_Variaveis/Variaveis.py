'''
Comentário com mais de uma linha (utilização de três aspas simples)
'''

'''
PARTE 1
nome = 'Humberto Delgado' #Variável string
empresa = 'FIAP' #Variável string
qtde_funcionarios = 500 #Variável int
mediaMensalidade = 856.50 #variavel double

print(nome + ' trabalha na empresa ' + empresa) #sinal de + concatena strings
print('Possui: ', qtde_funcionarios, ' funcionários.') #vírgula concatena strings com variáveis numéricas
print('A média da mensalidade é de: ' + str(mediaMensalidade)) #função str() converte valores numéricos para string
'''

#PARTE 2
nome = input('Digite um funcionário: ')
empresa = input('Digite a instituição: ')
qtde_funcionarios = int(input('Digite a qtde de funcionários: ')) #Função int() converte a entrada para inteiro
mediaMensalidade = float(input('Digite a média da mensalidade: ')) #Função float() converte a entraa para float
print(nome, "trabalha na empresa", empresa) #Python coloca espaço automaticamente após os prints
print('Possui:', qtde_funcionarios, 'funcionários')
print ('A média da mensalidade é de:', str(mediaMensalidade))
print('==========Verifique os tipos de dados abaixo:==========')
print('O tipo de dado da variável [nome] é:', type(nome))
print('O tipo de dado da variável [empresa] é:', type(empresa))
print('O tipo de dado da variável [qtde_funcionarios] é:', type(qtde_funcionarios))
print('O tipo de dado da variável [mediaMensalidade] é:', type(mediaMensalidade))
