# CALCULADORA COM REPETIÇÃO

print("=" * 40)
print("CALCULADORA REPETINDO")
print("=" * 40)

# Laço de repetição (pode usar várias vezes)
continuar = "s"
while continuar == "s":

    print("\n" + "-" * 30)

    # Pedir os números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Mostrar opções
    print("\nEscolha a operação:")
    print("1 - SOMA (+)")
    print("2 - SUBTRAÇÃO (-)")
    print("3 - MULTIPLICAÇÃO (×)")
    print("4 - DIVISÃO (/)")

    # Pedir a escolha
    escolha = input("Digite o número da operação (1, 2, 3 ou 4): ")

    # Fazer a operação escolhida
    if escolha == "1":
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")

    elif escolha == "2":
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")

    elif escolha == "3":
        resultado = num1 * num2
        print(f"\nResultado: {num1} × {num2} = {resultado}")

    elif escolha == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("\nERRO: Não é possível dividir por zero!")

    else:
        print("\nOpção inválida! Digite apenas 1, 2, 3 ou 4.")

    # Perguntar se quer continuar
    print("\n" + "-" * 30)
    continuar = input("Deseja fazer outra operação? (s/n): ").lower()

print("\nObrigado por usar a calculadora!")
