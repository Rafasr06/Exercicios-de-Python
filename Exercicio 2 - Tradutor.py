dicionario = {}

while True:
    chave = input("Digite uma palavra em inglês para o dicionário (ou 'sair' para encerrar): ")
    if chave == 'sair':
        break
    valor = input("Digite a tradução da palavra que você digitou em inglês, agora em português, para o dicionário '{}': ".format(chave))
    dicionario[chave] = valor
    print("\nVocê cadastrou uma palavra no dicionário: '{}' -> '{}'".format(chave, valor))

while True:
    palavra = input("\nDigite uma palavra em inglês para consultar (ou 'sair' para encerrar): ")

    if palavra == 'sair':
        break

    if palavra in dicionario:
        print("Tradução:", dicionario[palavra])
    else:
        print("Palavra não encontrada no dicionário.")






