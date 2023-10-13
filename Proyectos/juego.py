
import random

jugador1 = {"nombre": "Jugador 1", "puntos": 0, "bonus": 0}
jugador2 = {"nombre": "Jugador 2", "puntos": 0, "bonus": 0}

tablero = [["*", "*", "*", "*", "*", "*"],["*", "*", "*", "*", "*", "*"],["*", "*", "*", "*", "*", "*"],["*", "*", "*", "*", "*", "*"],["*", "*", "*", "*", "*", "*"],["*", "*", "*", "*", "*", "*"]]
cartas = [[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18],[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18]]

random.shuffle(cartas)

# Barajar los elementos dentro de cada fila
for fila in cartas:
    random.shuffle(fila)

def obtener_puntaje_carta(valor):
    if valor <= 6:
        return 1
    elif valor <= 12:
        return 1
    elif valor <= 18:
        return 1
    elif valor==6 or valor ==10 or valor ==14:
        return 800
    else:
        return 0

def imprimir_tablero():
    print('  0  1  2  3  4  5 \n')

    for i in range(6):
        print(i, '', end=' ')
        for j in range(6):
            if tablero[i][j] != "*":
                print(tablero[i][j], '', end=' ')
            else:
                print("*  ", end=' ')
        print('\n')

def seguir_jugando():
    respuesta = input("¿Quieres seguir jugando? (si/no): ")
    return respuesta.lower() == "si"

def casilla_valida(x, y):
    return 0 <= x < 6 and 0 <= y < 6 and tablero[y][x] == "*" 


def obtener_carta(x, y):
    return cartas[y][x]

def obtener_puntaje_turno(jugador, carta1, carta2):
    if carta1 == carta2:
        puntos_carta1 = obtener_puntaje_carta(carta1) + jugador["bonus"]
        puntos_carta2 = obtener_puntaje_carta(carta2) + jugador["bonus"]
        jugador["puntos"] += puntos_carta1 + puntos_carta2
        jugador["bonus"] += 10
        print("¡Encontraste una pareja! +{} puntos, +{} bonus".format(puntos_carta1 + puntos_carta2, jugador["bonus"]))
        return True
    else:
        jugador["bonus"] = max(jugador["bonus"], 0)
        print("Las cartas no coinciden. Volviendo a los asteriscos. Bonus actual: {}".format(jugador["bonus"]))
        return False

def turno(jugador):
    pares_encontrados = 0
    total_pares = 18

    while pares_encontrados < total_pares :
        imprimir_tablero()
        print(f"Turno de {jugador['nombre']}")
        x1, y1=-1,-1
        while not casilla_valida(x1, y1):
            x1 = int(input("Ingresa la columna de la primera carta: "))
            y1 = int(input("Ingresa la fila de la primera carta: "))
            if not casilla_valida(x1, y1)  :
                print("Casilla inválida, por favor intenta de nuevo.")
        valor1 = obtener_carta(x1, y1)
        tablero[y1][x1] = str(valor1)
        imprimir_tablero()
        print(f"Elegiste el número {valor1}")

        x2, y2=-1,-1
        while not casilla_valida(x2, y2) or (x2 == x1 and y2 == y1):
            x2 = int(input("Ingresa la columna de la segunda carta: "))
            y2 = int(input("Ingresa la fila de la segunda carta: "))
            if not casilla_valida(x2, y2) or (x2 == x1 and y2 == y1):
                print("Casilla inválida, por favor intenta de nuevo.")
        carta2 = obtener_carta(x2, y2)
        tablero[y2][x2] = str(carta2)
        imprimir_tablero()
        print(f"Elegiste el número {carta2}")

        if obtener_puntaje_turno(jugador, valor1, carta2):
            pares_encontrados += 1
        else:
            tablero[y1][x1] = '*'
            tablero[y2][x2] = '*'

        if not seguir_jugando():
            print("Juego terminado.")
            print(f"Puntos de {jugador1['nombre']}: {jugador1['puntos']}")
            print(f"Puntos de {jugador2['nombre']}: {jugador2['puntos']}")
            return False


        jugador = jugador1 if jugador == jugador2 else jugador2

    print("¡Juego terminado!")
    print(f"{jugador['nombre']} gana con {jugador['puntos']} puntos")
    return True


jugador_actual = jugador1
turno(jugador_actual)
