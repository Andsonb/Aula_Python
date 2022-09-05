def soma(arg1,arg2):
    return f'{arg1+arg2}'

def subi(arg1,arg2):
    return f'{arg1-arg2}'


var1=1
var2=8
seg= [1]
operacao = { 'chave1': 1
}
soma_recebe1=2
soma_recebe2=2
print(operacao.items())
if seg == operacao.values():
    print('111111')
    print(soma(soma_recebe1, soma_recebe2))
elif operacao == 'subitração' or '-':
    subi(soma_recebe1, soma_recebe2)
    print(subi(soma_recebe1, soma_recebe2))

