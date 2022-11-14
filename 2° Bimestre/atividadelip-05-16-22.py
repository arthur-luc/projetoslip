#sistema de porcentagem de ataques rpg

#dicionarios com elementos e classes
elementosBásicos = ['agua', 'necromancia', 'fogo', 'raio', 'vento']
tipoJogadores = ['mago necromante', 'guerreiro de fogo', 'paladino aquático']

#criacao do metodo para calcular ataque
def calcularAtaque (tipoJogador, elementosAtaque):
  
  if (tipoJogador == 'mago necromante' and elementosAtaque == 'necromancia') or (tipoJogador == 'guerreiro de fogo' and elementosAtaque == 'fogo') or (tipoJogador == 'paladino aquático' and elementosAtaque == 'água') or (tipoJogador == 'saqueador relâmpago' and elementosAtaque == 'raio'):
    return('50% de ataque')

  if tipoJogador == 'paladino aquático' and elementosAtaque == 'fogo':
    return ('-20% de ataque')

  if tipoJogador == 'paladino aquático' and elementosAtaque == 'raio':
    return ('70% de ataque')

#listagem das possibilidades
print(calcularAtaque ('mago necromante', 'necromancia'))
print(calcularAtaque ('guerreiro de fogo', 'fogo'))
print(calcularAtaque ('paladino aquático', 'água'))
print(calcularAtaque ('saqueador relâmpago', 'raio'))
print(calcularAtaque ('paladino aquático', 'fogo'))
print(calcularAtaque ('paladino aquático', 'raio'))
