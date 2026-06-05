personagens = {}

while True:

    print("\n=== MENU ===")
    print("1 - Adicionar personagem")
    print("2 - Consultar personagem")
    print("3 - Adicionar item ao inventário")
    print("4 - Remover item do inventário")
    print("5 - Listar personagens")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # Adicionar personagem
    if opcao == "1":

        nome = input("Nome: ")

        if nome in personagens:
            print("Personagem já cadastrado.")
            continue

        classe = input("Classe: ")
        nivel = int(input("Nível: "))

        if nivel < 0:
            print("O nível não pode ser negativo.")
            continue

        personagens[nome] = {
            "classe": classe,
            "nivel": nivel,
            "inventario": []
        }

        print("Personagem cadastrado com sucesso!")

    # Consultar personagem
    elif opcao == "2":

        nome = input("Digite o nome do personagem: ")

        if nome in personagens:

            print("\n=== PERSONAGEM ===")
            print(f"Nome: {nome}")
            print(f"Classe: {personagens[nome]['classe']}")
            print(f"Nível: {personagens[nome]['nivel']}")
            print(f"Inventário: {personagens[nome]['inventario']}")

        else:
            print("Personagem não encontrado.")

    # Adicionar item ao inventário
    elif opcao == "3":

        nome = input("Digite o nome do personagem: ")

        if nome in personagens:

            item = input("Digite o nome do item: ")
            personagens[nome]["inventario"].append(item)

            print("Item adicionado com sucesso.")

        else:
            print("Personagem não encontrado.")

    # Remover item do inventário
    elif opcao == "4":

        nome = input("Digite o nome do personagem: ")

        if nome in personagens:

            item = input("Digite o nome do item: ")

            if item in personagens[nome]["inventario"]:

                personagens[nome]["inventario"].remove(item)
                print("Item removido com sucesso.")

            else:
                print("Item não encontrado no inventário.")

        else:
            print("Personagem não encontrado.")

    # Listar personagens
    elif opcao == "5":

        if len(personagens) == 0:
            print("Nenhum personagem cadastrado.")

        else:

            print("\n=== PERSONAGENS ===")

            for nome, dados in personagens.items():

                print(nome)
                print(f"Classe: {dados['classe']}")
                print(f"Nível: {dados['nivel']}")
                print()

    # Sair
    elif opcao == "0":

        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")