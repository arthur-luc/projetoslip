#sistema que evita falhas sobre rpg

#dicionario dos poderes
primarios = ['agua', 'fogo', 'terra', 'ar']
secundarios = ['combustão', 'neve', 'lava', 'planta']

print(primarios)
print(secundarios)

#criacao do metodo para escolha do poder
def escolherPoderPrimário():
  escolha = input('Escolha um dos poderes listados acima:\n')

  #condicoes de escolhas
  if escolha == 'agua' or escolha == 'fogo' or escolha == 'terra' or escolha == 'ar':
    print('Escolha válida, poder escolhido: {}.'.format(escolha))
    valorbool = True
    
  elif escolha == 'combustão' or escolha == 'neve' or escolha == 'lava' or escolha == 'planta':
    print('Escolha inválida, poder: {} é um poder secundário, precisa ser um poder primário para prosseguir.'.format(escolha))
    valorbool = False

  else: 
    print('Valor inválido.')
    valorbool = False

  #sistema de repeticao que evita falhas
  while valorbool == False:
    escolha = input('Escolha outro poder:\n')
  
    if escolha == 'agua' or escolha == 'fogo' or escolha == 'terra' or escolha == 'ar':
      print('Escolha válida, poder escolhido: {}.'.format(escolha))
      break

    elif escolha == 'combustão' or escolha == 'neve' or escolha == 'lava' or escolha == 'planta':
      print('Escolha inválida, poder {} é um poder secundário, é preciso ser um poder primário para prosseguir.'.format(escolha))
    
    else:
      continue

#aplicacao do metodo
escolherPoderPrimário()