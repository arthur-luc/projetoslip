#sistema de range com numeros

#solicitacao da informacao
num = int(input('Informe um número:\n'))

#condicoes especificadas de range
if num >= 0 and num <=100:
  print('Dentro do range de 0 a 100')
  if num %2 == 0:
    print('Seu número é par.')
  else:
    print('Seu número é ímpar.')

elif num >100:
  print('Valor informado acima do esperado.')
  print('Valor máximo esperado: 100, valor informado: {}'.format(num))

else:
  print('Valor informado menor que o esperado.')
  print('Valor mínimo esperado: 0, valor informado: {}'.format(num))