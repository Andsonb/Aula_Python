def aula(nome,saudacao='Ola meu caro'):
    nome = input('digite seu nome: ')
    return nome, saudacao

var=aula(nome=())

print(f'{var[0]} {var[1]}')
