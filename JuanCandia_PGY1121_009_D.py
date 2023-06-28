sw = True
ciu = []
#Funciones
def menu():
    print("1.\tGrabar ciudadano\t\t")
    print("\n2.\tBuscar ciudadano \t\t")
    print("\n3.\tImprimir certificados \t\t")
    print("\n4.\tSalir \t\t")

def grabar():
    NIF = str(input("Ingrese NIF del ciudadano: " ))
    try:
            if len(NIF) >= 8:
                 ciu.insert(0,NIF)
    except:
            print("NIF NO VALIDO")
            return       
    nom = str(input("Ingrese nombre del ciudadano: "))
    ciu.insert(1,nom)
    edad = int(input("Ingrese edad del ciudadano: "))
    try:
         if edad >= 0:
              ciu.insert(2,edad)
    except:
         print("Edad no válida")
    print("El ciudadano se ha grabado correctamente")
    print(f"{ciu}")

def buscar():
     int(input("Ingrese NIF del ciudadano: "))
     print("No me acuerdo como se buscaban elementos")
     if ciu.index(20948109):
        print(f"{ciu}")

def imprimir():
     print(";_;")


#Menu
while sw == True:
    menu()
    opc1 = int(input("\n Por favor, seleccione una opción: "))
    if opc1 == 1:
        grabar()
    if opc1 == 2:
         buscar()
    if opc1 == 3:
         imprimir()
    if opc1 == 4:
         print("Hasta pronto")
         print("Hecho por Juan Candia, VER: 1.22474487139")
         sw = False