num: int = int(input('Escreva um número: '))
opção = input('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção:''')
if opção == '1':
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == '2':
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == '3':
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Esse não é um valor válido.')

 