salario = float(input('Dgite seu salário: R$'))
aumento1 = salario+((10/100)*salario)
aumento2 = salario+((15/100)*salario)

if salario > 1250.00:
    print('Seu novo salário aumentou para {}R${}'.format('\033[34m', aumento1))
else:
    print('Seu novo salário aumentou para {}R${}'.format('\033[35m', aumento2))
