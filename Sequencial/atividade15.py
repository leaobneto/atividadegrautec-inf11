valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("\n+ Salário Bruto: R$", round(salario_bruto, 2))
print("- IR (11%): R$", round(ir, 2))
print("- INSS (8%): R$", round(inss, 2))
print("- Sindicato (5%): R$", round(sindicato, 2))
print("= Salário Líquido: R$", round(salario_liquido, 2))