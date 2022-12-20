compra = []
print ("----------------")
print ("lista de la compra")
print ("-----------------")

while True:
    print ("1. Anadir producto.")
    print ("2. eliminar producto")
    print ("3. mostrar lista de comrpa")
    print ("4. salir del programa")
    print()
    opcion = input("--> ")
    print()

    if opcion =="1":
        producto = input("Introduce el producto: "). capitalize()
        if producto in compra:
            print("Ese producto ya esta en al lista")
        else:
            compra.append(producto)
    elif opcion =="2":
        producto = input("Introduce el producto: "). capitalize()
        if producto not in compra:
            print("Ese producto no esta en la lista. ")
        else:
            compra.remove(producto)
    elif opcion =="3":
        print("lista compra:")
        for e in compra:
            print(" -", e)
    elif opcion == "4":
        break
    else:
        print("introduce una opcion correcta.")

    print()