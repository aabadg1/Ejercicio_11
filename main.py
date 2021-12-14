#ejercicio 11 para entregar

from bubble_sort import BubbleSort

lista = []
firstPosition = True

while True:
    numero = input("Introduce un numero entero: ")

    try:
        int(numero)
        if int(numero) == -9999:
            bl = BubbleSort(lista)
            print(bl.sorted_list)
            del bl
            lista.clear()
            firstPosition = True
        else:
            lista.append(int(numero))
            firstPosition = False
    except ValueError:
        print("No es un numero entero")
        if numero.lower() == "fin":
            if firstPosition:
                break