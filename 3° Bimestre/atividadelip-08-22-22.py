#sistema de preview do rpg

#dicionario com elementos
elementos = {
  "fogo" : "Fogo é o elemento de maior destruição de todos. Quando bem manipulado transforma tudo em cinzas.",
  "agua" : "Agua é o elemento capaz de arrastar tudo com sua força. Poderes do tipo agua exigem muita mana, contudo causa devastação na mesma proporção. ",
  "raio" : "Raio é o elemento que tem maior velocidade. Manipuladores deste tipo de poder tem como característica principal a agilidade.",
  "necromancia" : "necromancia é o elemento responsável por trazer os mortos para a vida novamente. Somente quem tem conhecimentos de bruxos podem manipular esse elemento."
}

escolha = input('Bem-vindo ao jogo Os magos ensandecidos. Nosso jogo ainda está em desenvolvimento, porém já temos alguns poderes prontos, sendo eles:\nagua \nfogo \nraio \nnecromancia\nQual deles você deseja saber?\n') 

#criacao do metodo que retorna elementos
def poderes (escolhido):
  print(elementos[escolhido])    

#aplicacao do metodo
poderes (escolha)