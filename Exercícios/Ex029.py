velo = float(input('Insira a velocidade do carro: '))
ultrapassado = velo - 80
multa = ultrapassado*7
if velo > 80:
    print('CARAMBA VOCÊ TÁ RÁPIDO, PASSOU DE 80, VAI SER MULTADO KKKKK A MULTA EQUIVALE A R${}'.format(multa))
else:
    print('Tá suave, continua dirigindo ae')
