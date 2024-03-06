valor = float(input('Digite o valor do produto:'))
pgto = int(input('Escolha a forma de pagamento:\n1 - à vista dinheiro/cheque\n2 - à vista no cartão\n3 -em até 2x no cartão\n4 -Em até 3x ou mais no cartão'))
if pgto == 1:
    print('Como você está pagando à vista o você recebe 10% de desconto, o valor a pagar fica {}'.format(valor - (10/100*valor)))
elif pgto == 2:
    print('Como você está pagando à vista no cartão, você recebe 5% de desconto, o valor a pagar fica {}'.format(valor - (5 / 100 * valor)))
elif pgto == 3:
    print('Parcelando em 2x o valor fica: {:.2f} cada parcela'.format(valor/2))
elif pgto == 4:
    parcela = int(input('Em quantas parcelas você deseja pagar?? '))
    juros = (valor*(30/100))
    print('Em {} vezes recebe 30% de juros logo, o valor de cada parcela fica {:.2f}'.format(parcela, (valor / parcela) + juros))
