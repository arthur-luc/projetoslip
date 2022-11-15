#sistema de batalha naval segundo prototipo

import random

#listas de cordenadas e de suas possibilidades
lista0 = ['0a', '0b', '0c', '0d']
zeroa = ['0b', '1a']
zerob = ['0a', '1b', '0c']
zeroc = ['0b', '1c', '0d']
zerod = ['0c', '0d']

lista1 = ['1a', '1b', '1c', '1d']
uma = ['0a', '1b', '2a']
umb = ['0b', '1a', '2b', '1c']
umc = ['0c', '1b', '2c', '1d']
umd = ['0d', '1c', '2d']

lista2 = ['2a', '2b', '2c', '2d']
doisa = ['1a', '2b', '3a']
doisb = ['1b', '2a', '3b', '2c']
doisc = ['1c', '2b', '3c', '2d']
doisd = ['1d', '2c', '3d']

lista3 = ['3a', '3b', '3c', '3d']
tresa = ['2a', '3b']
tresb = ['2b', '3a', '3c']
tresc = ['2c', '3b', '3d']
tresd = ['2d', '3c']

#escolher primeira parte do navio
listalistas = [lista0, lista1, lista2, lista3]
lista = random.choice(listalistas)
navio1 = random.choice(lista)

navio1 = '0a'
print(navio1)

print('Bem vindo ao jogo: Batalha Naval!')
print(
  'Esse é seu campo de batalha:\n\n  a b c d\n0 . . . .\n1 . . . .\n2 . . . .\n3 . . . .'
)

#malha
aa0 = '.'
bb0 = '.'
cc0 = '.'
dd0 = '.'
aa1 = '.'
bb1 = '.'
cc1 = '.'
dd1 = '.'
aa2 = '.'
bb2 = '.'
cc2 = '.'
dd2 = '.'
aa3 = '.'
bb3 = '.'
cc3 = '.'
dd3 = '.'

def malha (a0, b0, c0, d0, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
  print('\n  a b c d\n0', a0, b0, c0, d0, '\n1', a1, b1, c1, d1, '\n2', a2, b2, c2, d2, '\n3', a3, b3, c3, d3)

#possibilidade 0a
if navio1 == '0a':
  navio2 = random.choice(zeroa)
  print(navio2)

  valorbool = True
  while valorbool:
    escolha1 = input(
      '\nEscolha uma cordenada que você quer atirar: (exemplo: 2b)\n')

    if escolha1 == navio1:
      aa0 = 'o'
      malha (aa0, bb0, cc0, dd0, aa1, bb1, cc1, dd1, aa2, bb2, cc2, dd2, aa3, bb3, cc3, dd3)
      print('\nVocê acertou um pedaço do navio!')

      valorbool2 = True
      while valorbool2:
        escolha2 = input('\nAgora, escolha outra cordenada:\n')

        if escolha2 == '0b':
          bb0 = 'o'
          malha (aa0, bb0, cc0, dd0, aa1, bb1, cc1, dd1, aa2, bb2, cc2, dd2, aa3, bb3, cc3, dd3)
          print('\nVocê acertou o outro pedaço do navio, você venceu!')
          break

        elif escolha2 == navio1:
          print('\nVocê não pode atirar duas vezes na mesma cordenada!')
          continue

        else:
          print('\nO seu tiro foi na água! Repita o tiro')
          continue
      break

    elif escolha1 == navio2:
      bb0 = 'o'
      malha(aa0, bb0, cc0, dd0, aa1, bb1, cc1, dd1, aa2, bb2, cc2, dd2, aa3, bb3, cc3, dd3)
      print('\nVocê acertou um pedaço do navio!')

      valorbool2 = True
      while valorbool2:
        escolha2 = input('\nAgora, escolha outra cordenada:\n')

        if escolha2 == navio1:
          aa0 = 'o'
          malha(aa0, bb0, cc0, dd0, aa1, bb1, cc1, dd1, aa2, bb2, cc2, dd2, aa3, bb3, cc3, dd3)
          print('\nVocê acertou o outro pedaço do navio, você venceu!')
          break

        elif escolha2 == navio2:
          print('\nVocê não pode atirar duas vezes na mesma cordenada!')
          continue

        else:
          print('\nO seu tiro foi na água! Repita o tiro')
          continue
      break
    
    else:
      print('O seu tiro foi na água! Repita o tiro.')
      continue