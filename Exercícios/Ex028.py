from random import randint
from time import sleep

print('-=-'*20)
numaleatorio = randint(0,5)
print('Hmm... Pensei num número entre 0 e 5')
print('-=-'*20)
numero = int(input('adivinha aí: '))


print('PROCESSANDO...')
sleep(3)
if numero == numaleatorio:
    print('VOCÊ ACERTOU LESGO \o/ ^^^^^^^^')
else:
    print('Você errou que decepção, a resposta era {}'.format(numaleatorio))
print('========FIM===========')
