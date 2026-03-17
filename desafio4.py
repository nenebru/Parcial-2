# Função da calculadora simples
def calculadora():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Solicitar os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        print(f"O resultado da adição é: {num1 + num2}")
    elif operacao == '2':
        print(f"O resultado da subtração é: {num1 - num2}")
    elif operacao == '3':
        print(f"O resultado da multiplicação é: {num1 * num2}")
    elif operacao == '4':
        if num2 != 0:
            print(f"O resultado da divisão é: {num1 / num2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida!")

# Chamar a função calculadora
calculadora()
