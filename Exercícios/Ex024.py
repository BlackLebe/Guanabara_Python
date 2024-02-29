cidade = input('insira o nome da cidade: ')
separarnome = cidade.capitalize().split()

print('A cidade em questão começa com santo? {}'.format('Santo' in separarnome[0]) )