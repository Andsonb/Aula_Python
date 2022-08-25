'''#basico

def som(n1,n2,n3):
    return n1+n2+n3


somma=som(n1=2,n2=3,n3=5)

print(somma)
'''

#avancado
def soma():
    n1=input('digite um numero para somar ')
    n2=input('digite outro numero ')
    n3=input('mais um ')
    if n1.isdigit()and n2.isdigit()and n3.isdigit():
        n1=int(n1)
        n2=int(n2)
        n3=int(n3)
        return n1+n2+n3
    else:print('por farvor so digitar numeros')


resultado=soma()

print(resultado)