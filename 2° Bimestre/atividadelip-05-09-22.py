#simulacao de rpg

#dicionario de drops
baumagico = ["Cajado de fogo", "Cajado gélido", "Cajado do vento", "Cajado necromante", "Manopla dourada", "Manopla da perdição", "Tiara da lua"]

#criacao do metodo para selecionar drop
def pegarItem(numeroEscolhido):
  return (baumagico[numeroEscolhido])

print('===== Começo da simulação =====')
achado = input('Parabéns jogador, você encontrou um báu magico!\nDeseja abri-lo? (Responda com Sim ou Não): ')

#condicoes e aplicacoes
if achado == "Sim":
  numero = int(input('Ótimo!, agora escolha um número de 0 a 6 para receber o seu item: '))
  print('Você recebeu o item:', pegarItem(numero)) 
  print('===== Fim da simulação =====')
else:    
  print('*você ignora o báu*')
  print('===== Fim da simulação =====')