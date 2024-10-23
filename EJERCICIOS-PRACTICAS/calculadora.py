
# Crea un programa en Python que pida al usuario dos números enteros y luego:
# Le pregunte al usuario si desea sumar, restar, multiplicar o dividir los números.
# Según la operación seleccionada, realice la operación correspondiente y muestre el resultado.
# Si el usuario elige una opción no válida, muéstrale un mensaje de error.

try:
    numero1 = int(input("ingresa un numero: "))
    operacion = input("ingresa la operacion que quieres hacer (suma +)-(resta -)-(multiplicar *)-(dividir /): ")
    numero2 = int(input("ingresa el numero para hacer esa operacion: "))

    def suma():
        total = numero1 + numero2
        return float(total)

    def resta():
        total = numero1 - numero2
        return float(total)
        
    def multiplicar():
        total = numero1 * numero2
        return float(total)

    def dividir():
        if numero2 == 0:
            return "Error: no se puede dividir por cero."
        total = numero1 / numero2
        return float(total)

    if operacion == "+" or operacion == "suma":
        print(f"el resultado de la suma es {suma()}")
    elif operacion == "-" or operacion == "resta":
        print(f"el resultado de la resta es {resta()}")
    elif operacion == "*" or operacion == "multiplicar":
        print(f"el resultado de la multiplicacion es {multiplicar()}")
    elif operacion == "/" or operacion == "dividir":
        resultado = dividir()
        if isinstance(resultado, str):
            print(resultado)  # Esto muestra el mensaje de error
        else:
            print(f"el resultado de la division es {resultado}")
    else:
        print("Error: operación no válida. Por favor, ingresa una operación válida.")

except ValueError:
    print("Error: por favor, ingresa un número válido.")
