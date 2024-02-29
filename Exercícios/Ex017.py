from math import hypot

catop = float(input('Digite o valor do cateto oposto ao ângulo: '))
catadj = float(input('Digite o valor do cateto adjacente ao ângulo: '))
hip = hypot(catop,catadj)

print('dado o cateto oposto e o adjacente, a hipotenusa equivale a: {}'.format(hip))