numero = int(input('Insira um número de 0 a 9999: '))
u = numero // 1%10
d = numero // 10%10
c = numero // 100%10
m = numero // 1000%10
print('no número digitado\n{} equivale a Milhar,\n{} Equivale a Centena,\n{} Equivale a dezena e\n{} Equivale a Unidade'.format(m,c,d,u))
