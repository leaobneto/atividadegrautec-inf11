tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade da conexão em Mbps: "))

# Converte megabytes para megabits
tamanho_megabits = tamanho * 8

# Calcula o tempo em segundos
tempo_segundos = tamanho_megabits / velocidade

# Converte segundos para minutos
tempo_minutos = tempo_segundos / 60

print("Tempo aproximado de download:",
      round(tempo_minutos, 2), "minutos")