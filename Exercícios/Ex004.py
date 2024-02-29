n = input('digite algo: ')
print('qual o tipo dele?',type(n))
print('ele é número?', n.isnumeric())#se é numério
print('ele é letra?', n.isalpha())#se é Alpha ou letra
print('ele é alphanumérico??',n.isalnum())#se é alphanumérico(letra ou número)
print('ele é ele está em maiúsculo??',n.isupper())
print('ele está minúsculo??', n.islower)