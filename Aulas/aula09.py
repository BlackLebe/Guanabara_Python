frase = 'Curso em Vídeo Python'
print(frase.replace('C', 'J'))
##Basicamente sou eu brincando com as formas de manipular string no python
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))
print(frase.upper())
print(frase.split())
separado = frase.split()
print(separado[2])
print(separado[2][3])
print('Curso' in separado[0])
