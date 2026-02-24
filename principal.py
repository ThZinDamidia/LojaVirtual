import estoque
import carrinho
import pagamento

def mostrar_lista(lista):
    """Exibe a lista de produtos"""
    for i in range(len(lista)):
        print(i + 1, "-", lista[i][0], "-", lista[i][1], "€")

def main():
    while True:
        print("\n==== LOJA DE COMPUTADORES ====")
        print("1 - Acer Trabalho")
        print("2 - Acer Gamer")
        print("3 - Apple Trabalho")
        print("4 - Apple Gamer")
        print("5 - Asus Trabalho")
        print("6 - Asus Gamer")                        
        print("7 - Componentes")
        print("8 - Ver Carrinho")
        print("9 - Finalizar Compra")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Escolha inválida! Por favor, insira um número.")
            continue

        if opcao == 1:
            mostrar_lista(estoque.acer_trabalho)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.acer_trabalho):
                    carrinho.adicionar(estoque.acer_trabalho[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 2:
            mostrar_lista(estoque.acer_gamer)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.acer_gamer):
                    carrinho.adicionar(estoque.acer_gamer[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 3:
            mostrar_lista(estoque.apple_trabalho)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.apple_trabalho):
                    carrinho.adicionar(estoque.apple_trabalho[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 4:
            mostrar_lista(estoque.apple_gamer)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.apple_gamer):
                    carrinho.adicionar(estoque.apple_gamer[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 5:
            mostrar_lista(estoque.asus_trabalho)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.asus_trabalho):
                    carrinho.adicionar(estoque.asus_trabalho[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 6:
            mostrar_lista(estoque.asus_gamer)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.asus_gamer):
                    carrinho.adicionar(estoque.asus_gamer[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 7:
            mostrar_lista(estoque.componentes)
            try:
                escolha = int(input("Escolha o produto: "))
                if 1 <= escolha <= len(estoque.componentes):
                    carrinho.adicionar(estoque.componentes[escolha - 1])
                else:
                    print("Escolha inválida!")
            except ValueError:
                print("Escolha inválida! Por favor, insira um número.")

        elif opcao == 8:
            carrinho.mostrar()

        elif opcao == 9:
            total = carrinho.mostrar()
            if total > 0:
                pagamento.pagar(total)
                carrinho.limpar()

        elif opcao == 0:
            print("Saindo da loja...")
            break

if __name__ == "__main__":
    main()
