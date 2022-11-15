#sistema de range com estrutura de repeticao e par ou impar

#criacao do metodo range
def range (num):
  if num <0 or num >100:
    return False
  else:
    return True

#criacao do metodo de par ou impar
def imparoupar (num):
  if num %2 == 0:
    print('Seu número é par.')
  else:
    print('Seu número é ímpar.')

#solicitacao da informacao
num = int(input('Insira um número que esteja entre 0 e 100:\n'))

#aplicacao do metodo range
range (num)

#repeticao do programa
while range (num) == False:
  num = int(input('Seu número é inválido, insira outro desde que ele esteja entre 0 e 100:\n'))

#aplicacao do metodo impar ou par
imparoupar (num)