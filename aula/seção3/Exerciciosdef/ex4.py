import teste

escolhas = {'soma': '+', 'subtração': '-', 'divisão': '/', 'multiplicação': '*', 'porcentagem': '%'}

print('Qual operação voce que fazer ?')
print()
for e, i in escolhas.items():
    print(f'[{e}], [{i}]')
while True:
    print()
    operacao = input('Operaçao desejada ?: ')
    soma_recebe1 = input('digite seu primeiro numero: ')
    soma_recebe2 = input('digite seu segundo numero: ')

    if soma_recebe2.isdigit() and soma_recebe1.isdigit():
        soma_recebe2 = int(soma_recebe2)
        soma_recebe1 = int(soma_recebe1)
    else:
        print('por farvor usar so numeros e o operadores validos ')
        continue

    if operacao == 'soma' or operacao == "+":
        print('')
        print(teste.soma(soma_recebe1, soma_recebe2))

    elif operacao == 'subtração' or operacao == '-':
        print(teste.sub(soma_recebe1, soma_recebe2))

    if operacao == 'divisão' or operacao == '/':
        print(teste.div(soma_recebe1, soma_recebe2))

    if operacao == 'multiplicação' or operacao == '*':
        print(teste.mult(soma_recebe1, soma_recebe2))

    if operacao == 'porcentagem' or operacao == '%':
        print(teste.posentagem(soma_recebe1, soma_recebe2))

    print('')
    parar_operacao = input('deseja continuar a operação, [ s ] sim  [n] não: ')
    if parar_operacao == 'n':
        break
