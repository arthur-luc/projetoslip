#sistema de mistura de poderes para rpg com repeticao

#dicionario com poderes
poderesprimarios = ['Água', 'Fogo', 'Terra', 'Ar']
poderessecundarios = ['Planta', 'Lava', 'Combustão', 'Neve']

print('Bem vindo ao jogo Elementais banguelos! Você pode escolher dois dos poderes listados para gerar um elemento:\n\n', poderesprimarios, '\n')

#escolhas do usuario
pp1 = input('Escolha um poder:\n')
pp2 = input('\nEscolha outro poder:\n')

#metodo que combina poderes
def combinacaoPoderSecundário(p1, p2):

  #condicoes das escolhas
  if p1 == 'Água' and p2 == 'Terra':
    print('\nSeu poder secundário é de', poderessecundarios[0])

  elif p1 == 'Terra' and p2 == 'Água':
    print('\nSeu poder secundário é de', poderessecundarios[0])

  elif p1 == 'Fogo' and p2 == 'Terra':
    print('\nSeu poder secundário é de', poderessecundarios[1])

  elif p1 == 'Terra' and p2 == 'Fogo':
    print('\nSeu poder secundário é de', poderessecundarios[1])

  elif p1 == 'Fogo' and p2 == 'Ar':
    print('\nSeu poder secundário é de', poderessecundarios[2])

  elif p1 == 'Ar' and p2 == 'Fogo':
    print('\nSeu poder secundário é de', poderessecundarios[2])

  elif p1 == 'Ar' and p2 == 'Água':
    print('\nSeu poder secundário é de', poderessecundarios[3])

  elif p1 == 'Água' and p2 == 'Ar':
    print('\nSeu poder secundário é de', poderessecundarios[3])
    
  else: 
    print('\nÉ necessário informar somente poderes primários. O valor informado ou é um poder Secundário ou valor invalido.')
    valorbool = False

    #repeticao se houver erros
    while valorbool == False:
      print('\nValor inválido, repita o processo.\n')
      esc1 = input('Escolha um poder:\n')
      esc2 = input('\nEscolha outro poder:\n')

      if esc1 == 'Água' and esc2 == 'Terra':
        print('\nSeu poder secundário é de', poderessecundarios[0])
        break
        
      elif esc1 == 'Terra' and esc2 == 'Água':
        print('\nSeu poder secundário é de', poderessecundarios[0])
        break
        
      elif esc1 == 'Fogo' and esc2 == 'Terra':
        print('\nSeu poder secundário é de', poderessecundarios[1])
        break
        
      elif esc1 == 'Terra' and esc2 == 'Fogo':
        print('\nSeu poder secundário é de', poderessecundarios[1])
        break
        
      elif esc1 == 'Fogo' and esc2 == 'Ar':
        print('\nSeu poder secundário é de', poderessecundarios[2])
        break
        
      elif esc1 == 'Ar' and esc2 == 'Fogo':
        print('\nSeu poder secundário é de', poderessecundarios[2])
        break
        
      elif esc1 == 'Ar' and esc2 == 'Água':
        print('\nSeu poder secundário é de', poderessecundarios[3])
        break
        
      elif esc1 == 'Água' and esc2 == 'Ar':
        print('\nSeu poder secundário é de', poderessecundarios[3]) 
        break

      else:
        continue

  #solicitacao de repeticao
  repetir = input('\nQuer repetir o processo?\n')

  if repetir == 'Sim' or repetir == 'sim':
    repetir = False

  else:
    print('Obrigado por usar o programa!')
    repetir = True
    
  while repetir == False:
    opp1 = input('Escolha um poder:\n')
    opp2 = input('\nEscolha outro poder:\n')
    combinacaoPoderSecundário(opp1, opp2)

#aplicacao do metodo
combinacaoPoderSecundário(pp1, pp2)
