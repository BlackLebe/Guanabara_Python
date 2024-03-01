r1 = int(input('Insira uma reta que eu direi se pode formar um triângulo n1: '))
r2 = int(input('Insira uma reta que eu direi se pode formar um triângulo n2: '))
r3 = int(input('Insira uma reta que eu direi se pode formar um triângulo n3: '))
condicao1 = r1 + r2 > r3
condicao2 = r2 + r3 > r1
condicao3 = r1 + r3 > r2
if condicao1 and condicao2 and condicao3 == True:
    print('Com essas retas pode-se formar um triângulo')
else:
    print('Impossível fazer um triângulo com essas medidas')
