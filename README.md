# Exercicios-de-Python
# Exercicio 1-Filtro:
 Crie um programa em Python que leia uma lista de nomes (Strings) informada pelo usuário. A entrada de nomes deve continuar até que o usuário digite a palavra “PARA”, que encerrará a leitura. Após isso, o programa deve solicitar uma letra para filtrar os nomes. Em seguida, exiba apenas os nomes que começam com essa letra, ignorando diferenças entre maiúsculas e minúsculas, e mostre o resultado em ordem alfabética.
Por exemplo, se a letra filtrada → A = Alice, Amanda, Ana.

# Exercicio 2-Tradutor:
Crie um programa que funcione como um mini dicionário de traduções.
O usuário deve poder adicionar palavras em inglês e suas traduções em português, e depois consultar a tradução de uma palavra digitada.
Exemplo:
Digite a palavra em inglês (ou 'sair'): car
Digite a tradução em português: carro
Digite a palavra em inglês (ou 'sair'): house
Digite a tradução em português: casa
Digite a palavra em inglês para buscar: house
Tradução: casa

# Exercicio 3- Loja de Produtos
Uma loja armazena seus produtos utilizando tuplas no formato:

(product_id, product_name, price)
Considere a seguinte coleção:

products = (
    (1, "Notebook", 3500.00),
    (2, "Mouse", 80.00),
    (3, "Keyboard", 150.00),
    (4, "Monitor", 1200.00),
)

Realize as seguintes tarefas:
 Exiba o nome do segundo produto. 
 Exiba o preço do último produto. 
 Percorra a coleção e imprima apenas os nomes dos produtos. 
 Encontre o produto mais caro. 
 Calcule o valor total de todos os produtos. 
 Crie uma função que receba um product_id e retorne a tupla correspondente ao produto. 
 Explique por que uma tupla pode ser uma escolha melhor que uma lista para representar um produto.

 # Exercicio 4- Permissões 
 Você está desenvolvendo um sistema de controle de acesso. Considere as permissões obrigatórias para acessar uma funcionalidade:

required_permissions = {"read", "write", "execute", "admin"}
e as permissões atualmente atribuídas ao usuário:

user_permissions = {"read", "write", "delete", "delete"}

Verifique se o usuário possui todas as permissões necessárias. Caso não possua, identifique quais permissões estão faltando e se há duplicatas na lista de permissões do usuário.

# Exercicio 5- Gerenciamento de Personagens
Crie um sistema de terminal para gerenciar personagens de RPG.
Cada personagem deve possuir os seguintes campos:
Nome
Classe
Nível
Inventário
O inventário deve armazenar vários itens.
Menu
Adicionar personagem
Consultar personagem
Adicionar item ao inventário
Remover item do inventário
Listar personagens
Sair
Regras
Adicionar personagem
Solicite:
Nome
Classe
Nível
Restrições:
Não permitir personagens com nomes duplicados.
O inventário deve iniciar vazio.
O nível não pode ser negativo.
Consultar personagem
Solicite o nome do personagem.
Exiba todas as informações cadastradas do personagem.
Caso ele não exista, informe ao usuário.
Adicionar item ao inventário
Solicite:
Nome do personagem
Nome do item
Adicione o item ao inventário do personagem.
Caso o personagem não exista, informe ao usuário.
Remover item do inventário
Solicite:
Nome do personagem
Nome do item
Remova o item apenas se ele existir no inventário.
Caso o personagem ou item não existam, informe ao usuário.
Listar personagens
Exiba o nome, classe e nível de todos os personagens cadastrados.

Exemplo:
=== PERSONAGENS ===
Arthur
Classe: Cavaleiro
Nível: 10
Merlin
Classe: Mago
Nível: 20



 


