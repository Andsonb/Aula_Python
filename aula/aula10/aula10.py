
num=input('digite um numero ')
num2=input('digite um numero' )

if num.isdigit() and num2.isdigit():
    num = int(num)
    num2 = int(num2)

    print(num+num2)
else:
    print('não posso calcular letras')