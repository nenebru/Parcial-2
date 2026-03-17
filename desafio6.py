# Solicitar o número de segundos
segundos = int(input("Digite o número de segundos: "))

# Calcular horas, minutos e segundos
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

# Exibir o resultado
print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
