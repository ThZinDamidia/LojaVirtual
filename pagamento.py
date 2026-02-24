 ==============================
# PAGAMENTO
# ==============================

def pagar(total):

    print("\n=== PAGAMENTO ===")
    print("Total a pagar:", total, "€")

    print("1 - Dinheiro")
    print("2 - Cartão")
    print("3 - PIX")

    forma = int(input("Escolha forma de pagamento: "))

    if forma == 1:
        valor = float(input("Digite valor pago: "))
        troco = valor - total
        print("Troco:", troco, "€")

    elif forma == 2:
        print("Pagamento no cartão aprovado!")

    elif forma == 3:
        print("Pagamento PIX aprovado!")

    print("Compra finalizada com sucesso!")
