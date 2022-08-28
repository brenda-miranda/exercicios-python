"""
Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ela.
"""
something = input('Digite algo: ')

types = type(something)
spaces = something.isspace()
number = something.isnumeric()
alpha = something.isalpha()
alphaNum = something.isalnum()
upper = something.isupper()
lower = something.islower()
title = something.istitle()

print('O tipo primitivo desse valor é {}'.format(types))
print('Só tem espaços? {}'.format(spaces))
print('É um número? {}'.format(number))
print('É alfabético? {}'.format(alpha))
print('É alfanumérico? {}'.format(alphaNum))
print('Está em maiúsculas? {}'.format(upper))
print('Está em minúsculas? {}'.format(lower))
print('Está capitalizado? {}'.format(title))


