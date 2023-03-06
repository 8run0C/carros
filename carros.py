carro = int(input("1-BMW\n2-AUDI\n3-FIAT\n4-FERRARI\nColoque o modelo do carro: "))
tipo = int(input("1-Gasolina\n2-Álcool\nColoque tipo de combustivel ele usa: "))
if carro == 1:
    gas = 9.8
    alc = 8.9
elif carro == 2:
    gas = 12.8
    alc = 10.9
elif carro == 3:
    gas = 26.8
    alc = 24.9
else:
    gas = 13.8
    alc = 12.9
portas = int(input("1-2 portas\n2-4 portas\nQuantas portas tem o carro: "))
if portas == 1:
    gas2 = gas - 0.5
    alc2 = alc - 0.5
else:
    gas2 = gas - 1.2
    alc2 = alc - 1.2
bag = int(input("1-sim\n2-não\nO carro tem bagageiro: "))
if bag == 1:
    gas3 = gas2 - 0.2
    alc3 = alc2 - 0.2
else:
    gas3 = gas2
    alc3 = alc2
if carro == 1:
    print("BMW:")
elif carro == 2:
    print("AUDI:")
elif carro == 3:
    print("FIAT:")
else:
    print("FERRARI:")
if portas == 1:
    print("2 portas")
else:
    print("4 portas")
if bag == 1:
    print("tem bagageiro")
else:
    print("não tem bagageiro")
if tipo == 1:
    print(f"{gas:.2f} L/km ---> {gas3:.2f} L/km")
else:
    print(f"{alc:.2f} L/km ---> {alc3:.2f} L/km")