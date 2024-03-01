dist = float(input('Digite a distância da viagem'))
preco1 = dist * 0.50
preco2 = dist * 0.45
if dist <= 200:
    print('Eita! sua viagem vai custar R${}'.format(preco1))
else:
    print('Carambolas! sua viagem vai custar R${}'.format(preco2))
