fichas = ['o', 'x']

def mostrar_tablero(n, movimientos_jugadores):
    for i in range(n):
        for j in range(n):
            casilla_vacia = True
            for k, movimientos_jugador in enumerate(movimientos_jugadores):
                if i in movimientos_jugador and j in movimientos_jugador[i]:
                    print(fichas[k] + ' ', end='')
                    casilla_vacia = False
            if casilla_vacia:
                print('_ ', end='')
        print()  # salto de línea al final de la fila

if __name__ == "__main__":
    n = int(input('Introduce el tamaño del tablero cuadrado: '))

    movimientos_jugador_1 = {0: [0], 1: [1]}  # ejemplo: jugador 1 en (0,0) y (1,1)
    movimientos_jugador_2 = {0: [1]}         # ejemplo: jugador 2 en (0,1)

    movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]

    mostrar_tablero(n, movimientos_jugadores)

import pytest

@pytest.fixture
def tablero_dimension():
    return 3  # o el tamaño que uses para las pruebas

@pytest.fixture
def movimientos_ambos_jugadores():
    # diccionarios con movimientos de ejemplo
    jugador_1 = {0:[0], 1:[1]}
    jugador_2 = {0:[1], 2:[2]}
    return [jugador_1, jugador_2]
def test_mostrar_tablero(tablero_dimension, movimientos_ambos_jugadores, capsys):
    from juego_3_en_raya import mostrar_tablero

    mostrar_tablero(tablero_dimension, movimientos_ambos_jugadores)
    captured = capsys.readouterr()
    assert 'o' in captured.out
    assert 'x' in captured.out

def movimiento_valido(n, x, y, movimientos_otro_jugador):
    if x > n or y > n:
        return False
    
    if x in movimientos_otro_jugador:
        movimientos_en_columna= movimientos_otro_jugador[x]
        if y in movimientos_en_columna:
            return False

    return True
@pytest.fixture
def movimientos_vacios():
    return {}, {}

@pytest.fixture
def movimientos_vacios():
    return {}, {}

@pytest.fixture
def movimientos_ocupados():
    return {2: [3]}

@pytest.fixture
def movimientos_fuera_tablero(tablero_dimension):
    return tablero_dimension + 1, tablero_dimension + 1


def test_movimiento_columna_fuera_tablero(tablero_dimension, movimientos_vacios):
    movimientos_otro_jugador, _ = movimientos_vacios
    x = 1
    y = tablero_dimension + 1
    assert not movimiento_valido(tablero_dimension, x, y, movimientos_otro_jugador)


def test_movimiento_fila_y_columna_fuera_tablero(tablero_dimension, movimientos_vacios, movimientos_fuera_tablero):
    movimientos_otro_jugador, _ = movimientos_vacios
    x, y = movimientos_fuera_tablero
    assert not movimiento_valido(tablero_dimension, x, y, movimientos_otro_jugador)


def test_movimiento_incorrecto(tablero_dimension, movimientos_ocupados):
    x = 2
    y = 3
    assert not movimiento_valido(tablero_dimension, x, y, movimientos_ocupados)
