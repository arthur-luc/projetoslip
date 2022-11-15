#sistema de descricao de elementos do rpg

#dicionario com elementos
poderes = ['Fogo', 'Água', 'Raio', 'Necromancia']

#dicionario com descricao dos elementos
definicao = ['É o elemento de maior destruição de todos. Quando bem manipulado transforma tudo em cinzas.', 'É o elemento capaz de arrastar tudo com sua força. Poderes do tipo água exigem muita mana, contudo causa devastação na mesma proporção. ', 'É o elemento que tem maior velocidade. Manipuladores deste tipo de poder tem como característica principal a agilidade.', 'É o elemento responsável por trazer os mortos para a vida novamente. Somente quem tem conhecimentos bruxos pode manipular esse elemento. ']

#escolha do usuario
num = int(input('Bem vindo ao jogo Os magos ensandecidos. O jogo ainda está em desenvolvimento, porém temos alguns poderes que podemos mostrar. Escolha um:\n0 - Fogo \n1 - Água \n2 - Raio \n3 - Necromancia \n'))

#criacao e aplicacao do metodo que retorna descricao
def funcao (numero):
  print(poderes [numero], '=', definicao [numero])

funcao (num)