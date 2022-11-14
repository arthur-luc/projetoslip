#calculadora com estruturas de condicoes

#solicitacao de informacoes
nome_usuario = input('Qual seu nome? ')
num1 = input('Digite um número:')
num2 = input('Digite outro número:')

#escolha da operacao
operacao = input('Qual o tipo de operação você quer utilizar?\n Para soma digite 1\n Para subtração digite 2\n Para multiplicar digite 3\n Para dividir digite 4\n Para potenciação digite 5\n Para exibição digite 6\n')

#condicoes e aplicacoes
if operacao == "1":
  print("A operação escolhida por", nome_usuario, "foi", operacao, ". O resultado desta operação considerando os números", num1, "e", num2, "teve como resultado:", int(num1) + int(num2))
if operacao == "2":
  print("A operação escolhida por", nome_usuario, "foi", operacao, ". O resultado desta operação considerando os números", num1, "e", num2, "teve como resultado:", int(num1) - int(num2))
if operacao == "3":
  print("A operação escolhida por", nome_usuario, "foi", operacao, ". O resultado desta operação considerando os números", num1, "e", num2, "teve como resultado:", int(num1) * int(num2))
if operacao == "4":
  print("A operação escolhida por", nome_usuario, "foi", operacao, ". O resultado desta operação considerando os números", num1, "e", num2, "teve como resultado:", int(num1) / int(num2))
if operacao == "5":
  print("A operação escolhida por", nome_usuario, "foi", operacao, ". O resultado desta operação considerando os números", num1, "e", num2, "teve como resultado:", int(num1) ** int(num2))
if operacao == "6":
  print("A operação escolhida por", nome_usuario, "foi", operacao, ". O resultado desta operação considerando os números", num1, "e", num2, "teve como resultado:", int(num1) , "e o número:", int(num2))