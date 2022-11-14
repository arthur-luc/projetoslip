#sistema de restricao de bebidas

print('======= Começo processamento ======')

#solicitacao de informacoes
fulano = input('Qual seu nome?\n')
idade = input('Qual sua idade?\n')

#condicoes e aplicacoes
if int(idade) >= 18:
    if int(idade) > 130:
        print('Você ainda existe?')
    print('Escolha sua bebida e divirta-se.... Com moderação!')
else:
    print('Caro usuário {}, você não tem idade suficiente para beber, compre refri e divirta-se.'.format(fulano))
print('======== Fim processamento =======')