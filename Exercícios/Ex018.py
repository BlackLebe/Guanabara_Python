from math import tan,sin,cos

angulo = float(input('digite um ângulo: '))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('dado esse ângulo, o seu seno equivale a {:.2f}\nseu cosseno equivale a {:.2f}\ne a sua tangente equivale a {:.2f}'.format(seno,cosseno,tangente))