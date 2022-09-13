
def master(fucao):
    def slave(*args, **kwargs):
        print('agora estou')
        fucao(*args, **kwargs)
    return slave


@master
def fala_oi(msg):
    print(msg)


fala_oi('ola')
