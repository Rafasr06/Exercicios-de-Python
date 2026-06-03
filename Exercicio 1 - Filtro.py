nomes = []

while True:
    nome = input("Digite um nome (ou PARA para encerrar): ")

    if nome.upper() == "PARA":
        break

    nomes.append(nome)

letra = input("Digite a letra para filtrar: ")

resultado = []

for nome in nomes:
    if nome.upper().startswith(letra.upper()): #Startswith verifica se o nome começa com uma determinada letra.
        resultado.append(nome)

resultado.sort()

print("\nNomes encontrados:")

for nome in resultado:
    print(nome)