 ==============================
# SISTEMA DE CARRINHO
# ==============================

carrinho = []

def adicionar(produto):
    carrinho.append(produto)
    print("Produto adicionado ao carrinho!")

def mostrar():
    total = 0

    if len(carrinho) == 0:
        print("Carrinho vazio!")
        return 0

    print("\n=== SEU CARRINHO ===")

    for item in carrinho:
        print(item[0], "-", item[1], "€")
        total += item[1]

    print("Total:", total, "€")
    return total

def limpar():
    carrinho.clear()
    print("Carrinho limpo!")
