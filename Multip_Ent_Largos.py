# Función para multiplicación utilizando el truco de Gauss
def multi_Gauss(x, y, base):
    # Caso base: si n = 1, retornar el producto
    n = max(len(str(x)), len(str(y)))
    if n == 1:
        return x * y

    # División de los números en partes iguales
    n2 = n // 2

    xl, xr = divmod(x, base**n2)
    yl, yr = divmod(y, base**n2)

    # Recursión para calcular los productos intermedios
    P1 = multi_Gauss(xl, yl, base)
    P2 = multi_Gauss(xr, yr, base)
    P3 = multi_Gauss(xl + xr, yl + yr, base)

    # Combinación de resultados
    return P1 * base**(2*n2) + (P3 - P1 - P2) * base**n2 + P2

# Función para multiplicación divide y vencerás
def multiplicacion_divide_y_venceras(x, y):
    # Convierte los números en cadenas y obtén su longitud
    str_x, str_y = str(x), str(y)
    len_x, len_y = len(str_x), len(str_y)

    # Caso base: si alguno de los números tiene un solo dígito, usa la multiplicación convencional
    if len_x == 1 or len_y == 1:
        return x * y

    # Divide los números en partes más pequeñas
    m = min(len_x, len_y) // 2
    a, b = int(str_x[:-m]), int(str_x[-m:])
    c, d = int(str_y[:-m]), int(str_y[-m:])

    # Calcula las multiplicaciones recursivamente
    ac = multiplicacion_divide_y_venceras(a, c)
    bd = multiplicacion_divide_y_venceras(b, d)
    ad_bc = multiplicacion_divide_y_venceras((a + b), (c + d)) - ac - bd

    # Combina los resultados
    return (10 ** (2 * m)) * ac + (10 ** m) * ad_bc + bd


# Función para mostrar el menú
def show_menu():
    print("Menu:")
    print("1. Multiplicación Decimal")
    print("2. Multiplicación Binaria")
    print("3. Salir")

# Ciclo principal del programa
while True:
    show_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        tipo_multiplicacion = input("Elija el tipo de multiplicación (1 para divide y vencerás, 2 para truco de Gauss): ")
        if tipo_multiplicacion not in ['1', '2']:
            print("Por favor, ingrese 1 para divide y vencerás o 2 para truco de Gauss.")
            continue

        base = 10
        num1 = int(input("Ingrese el primer número en decimal: "))
        num2 = int(input("Ingrese el segundo número en decimal: "))

    elif opcion == '2':
        tipo_multiplicacion = input("Elija el tipo de multiplicación (1 para divide y vencerás, 2 para truco de Gauss): ")
        if tipo_multiplicacion not in ['1', '2']:
            print("Por favor, ingrese 1 para divide y vencerás o 2 para truco de Gauss.")
            continue

        base = 2
        num1 = int(input("Ingrese el primer número en binario: "), 2)
        num2 = int(input("Ingrese el segundo número en binario: "), 2)

    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    if tipo_multiplicacion == '1':
        resultado = multiplicacion_divide_y_venceras(num1, num2)
    else:
        resultado = multi_Gauss(num1, num2, base)

    print("El resultado de la multiplicación es:", resultado if base == 10 else bin(resultado))

