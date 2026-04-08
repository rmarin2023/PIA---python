numeros = []

for i in range(3):
    n = int(input("Escriba un número: "))
    numeros.append(n)

# Eliminamos duplicados y obtenemos la cantidad de números que hay
son_iguales = len(set(numeros))
match son_iguales:
    case 1:
        print("Todos los números son iguales")
    case 2:
        print("Dos de los números son iguales")
    case 3:
        print("Todos los números son diferentes")