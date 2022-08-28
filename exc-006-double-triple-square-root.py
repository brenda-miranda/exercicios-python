# Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada

number = int(input('Digite um número: '))

double = number * 2
triple = number * 3
squareRoot = number ** (1/2)

print('O número digitado é {}. \nSeu dobro é {}. \nSeu triplo é {}. \ne a sua raiz quadrada é {:.2f}'.format(number, double, triple, squareRoot))



