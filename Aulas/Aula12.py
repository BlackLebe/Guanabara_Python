nome = input('Qual é o seu nome?? ').capitalize()
if nome == 'Calebe':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
elif nome == 'Edmo':
    print('A vai se catar Edmo')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))