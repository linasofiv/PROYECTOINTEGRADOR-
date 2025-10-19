"""
Integrantes: Lina Sofía Vallejo Cerón-Arturo Velasquez-Ayrin Florez Téllez

Los juegos de palabras son un pasatiempo muy antiguo que involucra la capacidad
de conocimiento del lenguaje de los participantes. Son muy comunes como forma
de entretenimiento y poseen un valor educativo y pedagógico, como método de
ejercitación del léxico, redacción u ortografía.

"""
import random # Se importa desde la biblioteca para los números aleatorios

# Función para crear una matriz vaCia
def crear_tablero(filas, columnas):
    tablero = []
    for fila in range(filas):
        tablero.append([])  # Crear una matriz vacía
        for columna in range(columnas):
            tablero[fila].append(0)
    return tablero

# Creación del tablero
tablero = [[64 - (8 * columna + fila) for fila in range(8)] for columna in range(8)]

def imprimir_tablero(tablero):
    for n in tablero:
        alineacion = " | ".join([f"{num:2}" for num in n])  
        print(f"| {alineacion} |")

imprimir_tablero(tablero)

# Listas de frutas
Respuesta1 = ["Bacuri", "Badia", "Badea", "Bajo", "Banano", "Banana", "Barbadina", "Baya", "Berenjena", "Bergamota", "Betabel", "Bolaina", "Bolilla", "Borojó", "Bota", "Bremia", "Breva", "Breadfruit", "Bignay"]
Respuesta2 = ["Papaya", "Pera", "Pimiento", "Piña", "Pistacho", "Pitahaya", "Pitanga", "Plátano", "Pomelo", "Pasas", "Pepino dulce", "Paraguayos"]

# Función para obtener las coordenadas en el tablero
def obtener_coordenadas(posicion):
    num_filas = 8
    num_columnas = 8
    # Determinar la fila
    fila = num_filas - 1 - ((posicion - 1) // num_columnas)
    # Evaluar la condición para determinar la columna
    if ((posicion - 1) // num_columnas) % 2 == 0:
        columna = (posicion - 1) % num_columnas
    else:
        columna = num_columnas - 1 - ((posicion - 1) % num_columnas)
    return fila, columna

# Función para intentar adivinar frutas con B
def Intentos_b():
    cont = 0  
    while cont < 3:  # Se permite un máximo de 3 intentos
        palabra = input("Escribe el nombre de una fruta que comience con 'B': ").capitalize()
        if palabra in Respuesta1:
            print("¡Has acertado! Puedes avanzar.")
            return True  # Se acierta y termina
        else:
            print("Incorrecto. Intenta de nuevo.")
        cont += 1
    print("Has fallado 3 veces.")
    return False  # Si falló 3 veces, pierde

# Función para intentar adivinar frutas con P
def Intentos_p():
    cont = 0  
    while cont < 3:  # Se permite un máximo de 3 intentos
        palabra = input("Escribe el nombre de una fruta que comience con 'P': ").capitalize()
        if palabra in Respuesta2:
            print("¡Has acertado! Puedes avanzar.")
            return True  # Se acierta y termina
        else:
            print("Incorrecto. Intenta de nuevo.")
        cont += 1
    print("Has fallado 3 veces.")
    return False  # Si falló 3 veces, pierde


# Juego principal

pos = 1
opcion = "si"
incremento_escalera = 18
puntaje = 0
Mejor_puntaje = 0
lista_mejores_puntajes = []  # Lista para almacenar los mejores puntajes
nombre = input("Digite su nombre: ")
with open("arhivo_nombres.txt","w") as archivo:
        archivo.write(nombre)
# Juego principal
while opcion.lower() == "si":
    opcion = input("¿Quiere seguir lanzando el dado? (si/no) ")
    if opcion.lower() != "si":
        break

    dado = random.randint(1, 6)  # Lanzar el dado
    pos += dado
    print("Su lanzamiento fue:", dado)
    print("Su nueva posición es:", pos)

    fila, columna = obtener_coordenadas(pos)
    print("Fila:", fila)
    print("Columna:", columna)
    
    numero = tablero[fila][columna]
    print("En esa posición se encuentra el número:", numero)

    # 

    nueva_posicion = numero + incremento_escalera
    if numero in [6,15,21,38]:
        nueva_posicion = numero + incremento_escalera
        print("Estas en la escalera! Tu nueva posición es: ", nueva_posicion)
    if numero in [19,43,53,60]:
        nueva_posicion = numero - incremento_escalera
        print("Oh no caiste en la serpiente! Tu nueva posición es: ", nueva_posicion)
    if numero == [64]:
        print("Felicitaciones")
        print("Completaste la meta")
        break

    # Si el número es par, juega con frutas que comienzan con B, si es impar, con frutas que comienzan con P
    
    if numero % 2 == 0:
        acierto = Intentos_b()  # Frutas con B
    else:
        acierto = Intentos_p()  # Frutas con P

    if not acierto:  # Si no acertó, el jugador pierde
        print("¡Lo siento, has perdido!")
        break
    else:
        print("¡Sigue jugando!")

    # Almacena los mejores puntajes

    Mejor_puntaje = 0

    puntaje+=1

    if puntaje > Mejor_puntaje:
        Mejor_puntaje = puntaje
        print("El mejor puntaje es: ", Mejor_puntaje)

         # Guardar el mejor puntaje en la lista
        lista_mejores_puntajes.append(Mejor_puntaje)

        # Guardar los mejores puntajes en un archivo
        with open("archivo_puntajes.txt", "w") as archivo_puntajes:
            for p in lista_mejores_puntajes:
                archivo_puntajes.write(f"{nombre}: {p}\n")

# Al final del juego, imprimir la lista de mejores puntajes
print("Lista de mejores puntajes:", lista_mejores_puntajes)


