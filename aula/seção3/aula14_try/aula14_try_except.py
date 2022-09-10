def convertevalor(args):
    try:
        args = int(args)
        return args
    except ValueError:
        try:
            args = float(args)
            return args
        except ValueError:
            pass


while True:
    numero = convertevalor(input('digite seu valor: '))

    if numero is None:
        print('valor digitadodo não e numero')
    else:
        print(numero + 2)
