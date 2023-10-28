numero1 = input("Escolha um numero: ")
operador = input("Qual operador vc deseja: ")
numero2 = input("Escolha outro numero: ")


if numero1.isnumeric() and numero2.isnumeric():   
    numero1 = float (numero1)
    numero2 = float(numero2)

    if operador == "+":
        print(numero1 + numero2)
    elif operador == "x":
        print(numero1 * numero2)
    elif operador == "/":
        print(numero1 / numero2)
    elif operador == "-":
        print(numero1 - numero2)
else:
    print("Você não digitou um numero ")