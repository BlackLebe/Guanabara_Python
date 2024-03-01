frase = input('Digite uma frase: ').upper().strip()
print('A Letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A Primera letra A aparece na posição {}'.format(frase.find('A')))
print('A Última letra A apareceu na posição {}'.format(frase.rfind('A')))