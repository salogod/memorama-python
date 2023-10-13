import random

def crear_matriz(num):
    matriz = []
    a = 0
    for i in range(6):
        matriz.append([])
        for j in range(6):
            matriz[i].append(num[a])
            a += 1
    for i in range(len(matriz)):
        print(matriz[i])
    return matriz

def crear_tablero():
    tablero = [
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"]
    ]

    for i in tablero:
        for j in i:
            print(j, " ", end="")
        print()
    return tablero

def mostrar(a, b, tablero, matriz):
    tablero[b - 1][a - 1] = matriz[a - 1][b - 1]
    for i in tablero:
        for j in i:
            print(j, " ", end="")
        print()
    return tablero[b - 1][a - 1]

def limpiar(a1, b1, a2, b2, tablero):
    tablero[b1 - 1][a1 - 1] = "-"
    tablero[b2 - 1][a2 - 1] = "-"
    for i in tablero:
        for j in i:
            print(j, " ", end="")
        print()

def cambio_jugador(jugador):
    if jugador == 1:
        jugador = 2
    else:
        jugador = 1
    return jugador

def validar(a, b, a2, b2, tablero):
    if a < 0 or a > 6 or b < 0 or b > 6 or tablero[b - 1][a - 1] != "-":
        print("Carta invalida")
        return False
    elif a == a2 and b == b2:
        print("Esta carta ya esta usada")
        return False
    else:
        return True

def sumar_puntos(puntos):
    puntos += 1
    return puntos

def dictar_ganador(puntos1, puntos2):
    if puntos1 > puntos2:
        print("El jugador 1 ha ganado", puntos1, "Puntos")
        ganador = True
    elif puntos2 > puntos1:
        print("El jugador 2 ha ganado", puntos2, "Puntos")
        ganador = True
    else:
        print("Hubo un empate")
        print("El jugador 1", puntos1, "Puntos")
        print("El jugador 2", puntos2, "Puntos")
        ganador = True
    return ganador

def checar_movimientos(tablero):
    guiones = 0
    for i in tablero:
        for j in i:
            if j == "-":
                guiones += 1
    return guiones

numeros = []
print("Empieza el juego")
for i in range(0, 18):
    numeros.append(i)
    numeros.append(i)
random.shuffle(numeros)
matriz = crear_matriz(numeros)
tablero = crear_tablero()
jugando = True
jugador = 1
puntos1 = 0
puntos2 = 0
ganador = False
guiones = 0

while jugando and not ganador:
    seguir = False
    print("Sigue jugador", jugador)
    valido1 = False
    valido2 = False
    while not valido1:
        a1 = int(input("Carta en a del primer numero: "))
        b1 = int(input("Carta en a del segundo numero: "))
        valido1 = validar(a1, b1, -1, -1, tablero)
    print("Elegiste el numero:", matriz[a1 - 1][b1 - 1])
    while not valido2:
        a2 = int(input("Carta en a del primer numero: "))
        b2 = int(input("Carta en a del segundo numero: "))
        valido2 = validar(a2, b2, a1, b1, tablero)
    print("Elegiste el numero:", matriz[a2 - 1][b2 - 1])
    tabla1 = mostrar(a1, b1, tablero, matriz)
    print("Primer numero")
    tabla2 = mostrar(a2, b2, tablero, matriz)
    print("Segundo numero")
    if tabla1 == tabla2:
        print("Encontraste un par!!")
        if jugador == 1:
            puntos1 = sumar_puntos(puntos1)
        else:
            puntos2 = sumar_puntos(puntos2)
        seguir = True
    else:
        print("No coinciden")
        limpiar(a1, b1, a2, b2, tablero)
    if checar_movimientos(tablero) == 0 and not ganador:
        seguir = True
    while not seguir:
        resp = input("Quieres seguir jugando? (si/no): ")
        if resp.lower() == "si":
            jugando = True
            jugador = cambio_jugador(jugador)
            seguir = True
        elif resp.lower() == "no":
            jugando = False
            print("Puntos finales del jugador 1:", puntos1)
            print("Puntos finales del jugador 2:", puntos2)
            ganador = dictar_ganador(puntos1, puntos2)
            seguir = True
        else:
            seguir = False
