with open('abc.txt', 'w+')as file:
    file.write('linha1\n')
    file.write('linha2\n')
    file.write('linha3\n')

    file.seek(0)
    print(file.read())
