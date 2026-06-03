produtos_armazenados = (
    (1, "Notebook", 3500.00),
    (2, "Mouse",80.00,),
    (3, "Keyboard", 150.00),
    (4, "Monitor", 1200.00),
)
print(produtos_armazenados[1][1])
print(produtos_armazenados[3][2])
for codigo, nome, valor in produtos_armazenados:
    print(nome)
for codigo, nome, valor in produtos_armazenados:
    if valor > 3000:
        print(f"O produto {nome} é o mais caro")
valor_total_produtos = 0
for codigo, nome, valor in produtos_armazenados:
    valor_total_produtos = sum([valor_total_produtos, valor])
print(f"O valor total dos produtos é {valor_total_produtos}")

def buscar_produto_por_codigo(codigo):
    for codigo_produto, nome, valor in produtos_armazenados:
        if codigo_produto == codigo:
            return (nome)
    return "Produto não encontrado"

codigo = int(input("Digite o código do produto: "))
print(buscar_produto_por_codigo(codigo))
#Explique por que uma tupla pode ser uma escolha melhor que uma lista para representar um produto?
#Uma tupla pode ser uma escolha melhor que uma lista para representar um produto porque as tuplas são imutáveis
#, com isso valores não podem ser alterados após a criação, isso é ideal para garantir a integridade dos dados do produtos.



