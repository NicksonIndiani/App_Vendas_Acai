def main():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Bem-vindo ao nosso app de vendas.")

    precos = {"CP": {"P": 9.00, "M": 14.00, "G": 18.00},
              "AC": {"P": 11.00, "M": 16.00, "G": 20.00}}

    total = 0.0

    while True:
        sabor = input("Escolha o sabor (CP para Cupuaçu, AC para Açaí): ").upper()
        if sabor not in ["CP", "AC"]:
            print("Sabor inválido. Tente novamente.")
            continue

        tamanho = input("Escolha o tamanho (P/M/G): ").upper()
        if tamanho not in ["P", "M", "G"]:
            print("Tamanho inválido. Tente novamente.")
            continue

        valor = precos[sabor].get(tamanho, 0)
        if valor == 0:
            print("Combinação inválida de sabor e tamanho. Tente novamente.")
            continue

        total += valor

        mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
        if mais_pedidos != "S":
            break

    print(f"Total a pagar: R${total:.2f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro: {e}")