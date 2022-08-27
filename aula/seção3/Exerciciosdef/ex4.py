
def soma(arg1,arg2):
    return f'{arg1+arg2}'

def subi(arg1,arg2):
    return f'{arg1-arg2}'

def divi(arg1,arg2):
    return f'{arg1/arg2}'

def mult(arg1,arg2):
    return f'{arg1*arg2}'

def posentagem(arg1,arg2):
    return f'{arg1/arg2*100}'

escolhas={'soma':'+' ,'subitração': '-' ,'divisão': '/' ,'mulplicação': '*' ,'posentagem':'%'}

print('Qual operação voce que fazer ?')
print()
for e, i in escolhas.items():
    print(f'[{e}] : [{i}]')
while True:
    print()
    operacao=input('Operaçao desejada ?: ')
    soma_recebe1=input('digite seu primeiro numero: ')
    soma_recebe2=input('digite seu segundo numero: ')
    if soma_recebe2.isdigit() and soma_recebe1.isdigit():
        soma_recebe2=int(soma_recebe2)
        soma_recebe1=int(soma_recebe1)
    else:
        print('por farvor usar so numeros e o operadores validos ')
        continue
    if operacao == 'soma' or '+':
        print(soma(soma_recebe1,soma_recebe2))
    elif operacao == 'subitração' or '-':
        subi(soma_recebe1,soma_recebe2)
        print(subi(soma_recebe1,soma_recebe2))

