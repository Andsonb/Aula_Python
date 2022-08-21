nome = 'anderson'

idade= 27

altura = 1.80

maioridade= idade>18

peso=80

imc= peso//(altura**2)

print(nome, 'tem', idade, 'de idade e seu imc é ',imc)

print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')

print('{}tem {}anos de idade e seu imc e {}'.format (nome,idade,imc))

print('{0}tem {1}anos de idade e seu imc e {2}'.format (nome,idade,imc))

print('{w}'.format(w=nome))