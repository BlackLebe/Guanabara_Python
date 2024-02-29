numero = input('Insira um número de 0 a 9999: ')
separar = numero.split()

print('no número digitado\n{} equivale a Milhar,\n{} Equivale a Centena,\n{} Equivale a dezena e\n{} Equivale a Unidade'.format(separar[0][0],separar[0][1],separar[0][2],separar[0][3]))
