#sistema que exibe caracteres especificos de uma string

print('============= Inicio processamento ===============')

#solicitacao de informacoes
texto = input('Digite um texto: ')

execucao = input(' 1 Exibir o primeiro carácter do texto.\n 2 Exibir o ultimo carácter do texto.\n 3 Mostrar todo texto digitado com letra maiúscula.\n 4 Mostrar todo o texto digitado com letra minúscula.\nDigite o número da opção que você queira realizar: ')

#condicoes e aplicacoes
if execucao == "1":
  print('O primeiro carácter do texto é:', texto[0])
if execucao == "2":
  print('O último carácter do texto é:', texto[-1])
if execucao == "3":
  print('O texto em maiúsculo é esse:', texto.upper())
if execucao == "4":
  print('O texto em minúsculo é esse:', texto.lower())
  
print('============= Fim processamento ===============')