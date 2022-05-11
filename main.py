'''2)Faça um programa em linguagem Python que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. Por exemplo, se o usuário inseriu 4, a saída deve ser 10 (1+2+3+4=10).'''

quantfim = int(input('Digite a quantidade de elementos que deseja na PA: '))
soma = 0
for num in range (1,quantfim+1,1):
  print (num)
  soma = soma + num
print(f'A soma dos termos da PA é igual a {soma}')