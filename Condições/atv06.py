num1 = int(input("insira o 1º numero"))
num2 = int(input("insira o 2º numero"))
num3 = int(input("insira o 3º numero"))

if num1 < num2 < num3 or num2 < num1 < num3:
    print (num3)

elif num3 <= num2 < num2 or num1 < num3 < num2:
    print(num2)