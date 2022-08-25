'''
def fun1():
    varr='anderson'
    return varr

def fun2():
    var='saudaçoes meu caro'
    return var

def fun3():
    print(f'{var1} {var2}')

var1=fun2()
var2=fun1()

fun3()
'''


def metre(fincao,*args, **kwargs):
    return fincao(*args, **kwargs)

def dale(nome):
    return f' salve meu amigo {nome}'


var=metre(dale,'anderson')

print(var)
