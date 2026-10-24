import math

area = float(input("Digite a área a ser pintada em m²: "))

litros = area / 3
latas = math.ceil(litros / 18)
preco_total = latas * 80

print("Quantidade de latas:", latas)
print("Preço total: R$", f"{preco_total:.2f}")