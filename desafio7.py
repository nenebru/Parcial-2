# Solicitar os valores de C, I e T ao usuário
capital = float(input("Digite o valor do capital (C): "))
taxa = float(input("Digite a taxa de juros (I): "))
tempo = float(input("Digite o tempo (T) em anos: "))

# Calcular os juros simples
juros = (capital * taxa * tempo) / 100

# Exibir o resultado
print(f"O valor dos juros simples é: {juros}")
