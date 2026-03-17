# Solicitar o número de segundos
segundos = int(input("Digite o número de segundos: "))

# Calcular horas, minutos e segundos
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

# Exibir o resultado
print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
# Solicitar horas, minutos e segundos
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

# Converter para segundos
total_segundos = horas * 3600 + minutos * 60 + segundos

# Exibir o resultado
print(f"O total de {horas} horas, {minutos} minutos e {segundos} segundos equivale a {total_segundos} segundos.")
