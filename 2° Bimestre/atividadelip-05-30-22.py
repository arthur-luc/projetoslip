#sistema de informacoes basicas com impar ou par

#variaveis com informacoes solicitadas e definicoes
nomeUser = input("Qual seu nome?\n")
idadeUser = int(input("Agora, qual sua idade?\n"))
idadePar= "Seja bem vindo {}! Sua idade é {} e está tudo corretamente registrado!"
idadeImpar = "Obrigado por usar nosso sistema {}. O seguinte registro foi executado: nome: {}, Idade: {}"

#criacao e aplicacao do metodo de exibicao da mensagem
def exibirMensagem(nome, idade):
  if idade %2 == 0:
    print(idadePar.format(nome, idade))
  else:
    print(idadeImpar.format(nome, nome, idade))
    
exibirMensagem(nomeUser, idadeUser)