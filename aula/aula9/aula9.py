def conexao():
    return login= input('digite seu login: ')
    return senha= input('digite sua senha: ')

conexao(2,2)

print(login, senha)
while login and senha != 'amanda':
    print('senha incorreta')
    conexao()


print('bem vindo')