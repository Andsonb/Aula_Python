
def divisao():
    n1 = input('digite um valor')
    n2 = input('digite')
    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2=int(n2)
        return n1 + n2
   # else:
    #    print('digite so numeros ')



divide = divisao()

if divide == None:
    print('conta deu erro.')
else:
    print(divide)



