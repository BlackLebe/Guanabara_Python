peso= float(input('Indique seu peso: '))
altura = float(input('Indique a sua altura:'))
IMC = round(peso/pow(altura, 2), 2)
print(IMC)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC <= 25:
    print('Peso ideial')
elif IMC <= 30:
    print('SOBREPESO')
elif IMC <= 40:
    print('OBESIDADE')
elif IMC > 40:
    print('OBESIDADE MÓRBIDA')
    
