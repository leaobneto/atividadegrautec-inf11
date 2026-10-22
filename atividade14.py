pesototal = float (input("insira o valor total dos peixes"))
if pesototal > 50:
    excesso = pesototal - 50
    multa = excesso * 4
    print(f"Excedeu {excesso} - Deu R${multa} ")
