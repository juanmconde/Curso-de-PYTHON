print("Bienvenidos a la calculadora")
print("Para salir escriba Salir")
print("Las operaciones pueden ser: sumar - restar - dividir - multiplicar")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operacion a realizar: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma" or op == "+":
        resultado += n2
    elif op.lower() == "resta" or op == "-":
        resultado -= n2
    elif op.lower() == "divide" or op == "/":
        resultado /= n2
    elif op.lower() == "multiplicar" or op == "*":
        resultado *= n2
    else:
        print("Operacion no valida")
        break

    print(f"el resultado es: {resultado}")
