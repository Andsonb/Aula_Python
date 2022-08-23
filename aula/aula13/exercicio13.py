
while True :
    print()
    num1=input('digite seu numero: ')
    num2=input('digite seu numero: ')
    operador=input('digite seu operador "+", "-", "/" : ')
    sair=input('deseja sair ? S ou N: ')

    if sair == 's':
        break

    if num1.isdigit() or num2.isdigit():

        num1=int(num1)
        num2=int(num2)

        if operador == '+':
            print(f'{num1+num2}')
        elif operador == '-':
            print(f'{num1-num2}')
        elif operador == '/':
            print(f'{num1/num2}')
        else:
            print('operador invalido')
    else:
        print('digite um numero valido')

