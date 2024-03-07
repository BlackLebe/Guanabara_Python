from random import choice
jokenpo = (input('VAMOS JOGAR JOKENPO, ESCOLHA PEDRA PAPEL OU TESOURA HÁ ^^\n')).capitalize()
computador = choice(['Pedra', 'Papel', 'Tesoura'])
print(computador)
#Derrotas:
if jokenpo == 'Pedra' and computador == 'Papel':
    print(f'IIIH PARECE QUE VOCÊ PERDEU EU TIREI {computador} E {computador} GANHA DE {jokenpo}')
elif jokenpo == 'Papel' and computador == 'Tesoura':
    print(print('IIIH PARECE QUE VOCÊ PERDEU EU TIREI {} E {} GANHA DE {}'.format(computador,computador,jokenpo)))
elif jokenpo == 'Tesoura' and computador == 'Pedra':
    print('IIIH PARECE QUE VOCÊ PERDEU EU TIREI {} E {} GANHA DE {}'.format(computador, computador, jokenpo))
#Vitorias:
elif jokenpo == 'Pedra' and computador == 'Tesoura':
    print('Ahhw parece que eu perdi ]= eu tirei {} E {} perde para {} ),:'.format(computador, computador, jokenpo))
elif jokenpo == 'Papel' and computador == 'Pedra':
    print('Ahhw parece que eu perdi ]= eu tirei {} E {} perde para {} ),:'.format(computador, computador, jokenpo))
elif jokenpo == 'Tesoura' and computador == 'Papel':
    print('Ahhw parece que eu perdi ]= eu tirei {} E {} perde para {} ),:'.format(computador, computador, jokenpo))
elif jokenpo == computador:
    print('HA HA HA PARECE QUE EMPATAMOS PELA DESSA VEZ, MAS SERÁ A ÚLTIMA HAHAHAHAH [:<')