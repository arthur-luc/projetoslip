#conversao de celsius para fahrenheit

print('Bem vindo a transformadora de Celsius para Fahrenheit!')

#solicitacao de informacoes
ce = float(input('Quantos graus celsius você quer converter para fahrenheit: '))

#criacao e aplicacao do metodo
def converterCelsiusParaFahrenheit(celsius):
  return celsius * 1.8 + 35
  
print("Os graus celsius convertidos para fahrenheit são:", converterCelsiusParaFahrenheit(ce))