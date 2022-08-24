from random import randint

numero = str(randint(100000000, 999999999))
nov_cpf = numero
conta=0
reverso = 10

for i in range(19):
    if i > 8:
        i -= 9
    conta += int(nov_cpf[i]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        n= 11 - (conta % 11)

        if n > 9 :
            n=0
        conta = 0
        nov_cpf += str(n)
print(f'cpf valido gerado :{nov_cpf}')