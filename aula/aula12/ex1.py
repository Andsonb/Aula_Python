numero = input('digite seu numero: ')

if numero.isdigit():
    numero = int(numero)
    soma = numero % 2
    if soma == 0:
        print(f'seu numero {numero}: é par ')
    else:
        print(f'seu numero {numero}: é impar ')
else:
    print(f'{numero} não é numero digite um numero validor')
