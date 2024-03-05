n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva um número: '))

if n1 > n2:
    print('O Primeiro valor é maior, no caso {}'.format(n1))
elif n2 > n1:
    print('O Segundo valor é maior, no caso {}'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais')
