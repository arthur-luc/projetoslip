#sistema de par ou impar com palacras

#solicitacao da informacao
palavra = input('Digite uma palavra:\n')

#condicoes e aplicacoes
if len(palavra) %2 == 0:
  print('Sua palavra é par. Ela sem a última letra fica desse jeito:', palavra[:-1])

else:
  print('Sua palavra é ímpar. Ela sem a primeira letra fica desse jeito:', palavra[1:])
