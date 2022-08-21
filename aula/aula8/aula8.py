nome = 'anderson'
idade= 27
altura = 1.80
maioridade= idade>18
peso=80
imc= peso//(altura**2)
data_hoje=2022
data_resu = data_hoje-idade

print('{0} tem {1} anos, {2} de altura e pesa {3}kg.'.format(nome,idade,altura,peso))
print('O IMC de {} é {}.'.format(nome,imc))
print('{} nasceu em {}'.format(nome,data_resu))