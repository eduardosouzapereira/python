nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? ').upper() #upper() converte o conteúdo da string para caixa alta

if idade >= 65:
    print(f'O paciente {nome} POSSUI atendimento prioritário!')
elif doenca_infectocontagiosa == 'SIM':
    print(f'O paciente {nome} deve ser direcionado para sala de espera reservada.')
else:
    print(f'O paciente {nome} NÃO possui atendimento prioritário e pode aguardar na sala comum!')
