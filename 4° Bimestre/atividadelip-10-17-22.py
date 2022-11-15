#sistema de pedra papel ou tesoura com placar

#importacao da funcao import
import random

#dicionario de maos
maos = ['Pedra', 'Papel', 'Tesoura']

#selecao aleatoria da mao do bot
valorbot = random.choice(maos)

#escolha da mao do usuario
valorplayer = input('Escolha um deles:\n1 - Pedra \n2 - Papel \n3 - Tesoura\n')

#placar dos jogadores
placarplayer = 0
placarbot = 0

#repeticao do jogo
valorbool = True
while valorbool:

  #condicoes do jogo
  if valorplayer == '1' and valorbot == 'Pedra':
    print('O computador escolheu: {}'.format(valorbot))
    print('Empate!\n')

  elif valorplayer == '1' and valorbot == 'Papel':
    print('O computador escolheu: {}'.format(valorbot))
    print('Você perdeu!\n')

    placarbot = placarbot + 1

  elif valorplayer == '1' and valorbot == 'Tesoura':
    print('O computador escolheu: {}'.format(valorbot))
    print('Você venceu!\n')

    placarplayer = placarplayer + 1

  elif valorplayer == '2' and valorbot == 'Pedra':
    print('O computador escolheu: {}'.format(valorbot))
    print('Você venceu!\n')

    placarplayer = placarplayer + 1

  elif valorplayer == '2' and valorbot == 'Papel':
    print('O computador escolheu: {}'.format(valorbot))
    print('Empate!\n')

  elif valorplayer == '2' and valorbot == 'Tesoura':
    print('O computador escolheu: {}'.format(valorbot))
    print('Você perdeu!\n')

    placarbot = placarbot + 1

  elif valorplayer == '3' and valorbot == 'Pedra':
    print('O computador escolheu: {}'.format(valorbot))
    print('Você perdeu!\n')

    placarbot = placarbot + 1

  elif valorplayer == '3' and valorbot == 'Papel':
    print('O computador escolheu: {}'.format(valorbot))
    print('Você venceu!\n')

    placarplayer = placarplayer + 1

  elif valorplayer == '3' and valorbot == 'Tesoura':
    print('O computador escolheu: {}'.format(valorbot))
    print('Empate!\n')

  repetir = input('Você quer repetir o jogo? Responda com sim ou não:\n')

  if repetir == 'sim':
    continue

  else:
    print(
      '\nObrigado por jogar o jogo!\n\nO placar foi:\n\nVocê ganhou {} vezes\nO computador ganhou {} vezes'
      .format(placarplayer, placarbot))
    break
