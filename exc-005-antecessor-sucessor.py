# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

number = int(input('Digite um número: '))

antecessor = number - 1
sucessor = number + 1

print('O antecessor de {} é {} e o seu sucessor é {}'.format(number, antecessor, sucessor))
