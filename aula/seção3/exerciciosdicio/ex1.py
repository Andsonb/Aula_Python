
perguntas={'pergunta1': {'pergunta': 'quanto é 2+2 ?',
                         'alterna': {'a': '2', 'b': '3', 'c': '4'},
                         'resposta_certa': 'c'},

           'pergunta2': {'pergunta': 'quanto é 2-2 ?',
                         'alterna': {'a': '1', 'b': '3', 'c': '0'},
                         'resposta_certa': 'c'}
           }

contador=0

for chave_p, chave_r in perguntas.items():
    print(f'{chave_p} : {chave_r["pergunta"]}')

    for alternativa1, alternativa2 in chave_r['alterna'].items():
        print(f'{alternativa1} - {alternativa2}')

    print()

    resposta=input('digite sua resposta: ')

    print()
    if resposta == chave_r['resposta_certa']:
        print('parabens voce acertouuu!')
        contador += 1
    else:
        print('voce errou :( ')

qtd_perg=len(perguntas)

media= contador / qtd_perg * 100

if media > 40:
    print(f'Parabens sua media de acerto foi de, {media}%')
else:
    print(f'voce precisa estudar mais, {media}%')

