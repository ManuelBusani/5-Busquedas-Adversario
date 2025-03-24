"""
Juego del Otello

El estado se va a representar como una tupla de 64 elementos 
pensandolo como una matriz de 8x8, donde `estado[8*i + j]`
es la casilla en la fila `i` y la columna `j`.

0  1  2  	3  4  	5  6  7
8  9  10 	11 12 	13 14 15
16 17 18 	19 20 	21 22 23

24 25 26 	27 28 	29 30 31
32 33 34 	35 36 	37 38 39

40 41 42	43 44 	45 46 47
48 49 50 	51 52	53 54 55
56 57 58 	59 60 	61 62 63

Esta tupla va a guardar el estado de cada casilla

0 si está vacía
1 si hay una ficha negra
-1 si hay una ficha blanca

Las negras empiezan primero en Otello.

Las acciones van a ser representadas como una tupla de números
`(i,j)` que representa la casilla en la que se pone una ficha,
donde `i` es el índice de la fila y `j` es el índice de la
columna.

En Otello, cuando no hay acciones legales para un jugador
pero si para el otro se omite el turno.

En dicho caso consideraré omitir turno como una acción legal
y la representaré como `None`.

"""

from juegos_simplificado import ModeloJuegoZT2
from juegos_simplificado import juega_dos_jugadores
from minimax import jugador_negamax
from minimax import minimax_iterativo

class Otello(ModeloJuegoZT2):
    def inicializa(self):
        return ((0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0,-1, 1, 0, 0, 0,
        		 0, 0, 0, 1,-1, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,),
        		1)

    def jugadas_legales(self, s, j):
        acciones = ()
        for fila in range(8):
            for columna in range(8):
                accion = (fila, columna)
                if self.es_legal(accion, s, j):
                    acciones += (accion,)

        if acciones != ():
            return acciones

        for fila in range(8):
            for columna in range(8):
                accion = (fila, columna)
                if self.es_legal(accion, s, -j):
                    acciones += (accion,)

        # caso en el que es estado terminal
        if acciones == ():
            return ()

        # caso en el que `j` no tiene acciones legales pero `-j` si,
        return (None,) 

    def es_legal(self, a, s, jugador):
        if s[a[0] * 8 + a[1]] != 0:
            return False

        for inc_i in (-1,0,1):
            for inc_j in (-1,0,1):
                i = a[0] + inc_i
                j = a[1] + inc_j

                if((inc_i == inc_j == 0) or
                   (not (0 <= i < 8)) or 
                   (not (0 <= j < 8)) or
                   (s[i * 8 + j] != -jugador)):
                        continue

                i += inc_i
                j += inc_j

                while (0 <= i < 8) and (0 <= j < 8): 
                    if s[i * 8 + j] == jugador:
                        return True
                    if s[i * 8 + j] == 0:
                        break
                    i += inc_i
                    j += inc_j
        return False

    def transicion(self, s, a, jugador):
        if a == None:
            return s

        estado = list(s)
        for inc_i in (-1,0,1):
            for inc_j in (-1,0,1):
                if inc_i == inc_j == 0:
                    continue

                i, j = a
                contador = 0

                while(True):
                    i += inc_i
                    j += inc_j

                    if ((not (0 <= i < 8)) or
                        (not (0 <= j < 8)) or
                        (estado[i * 8 + j] == 0)):
                            contador = 0
                            break

                    if estado[i * 8 + j] == jugador:
                        break

                    contador += 1

                while contador > 0:
                    i -= inc_i
                    j -= inc_j
                    contador -= 1
                    estado[i * 8 + j] = jugador

        estado[a[0]*8 + a[1]] = jugador
        return tuple(estado)

    def ganancia(self, s):
        suma_piezas = sum(s)
        return (1 if suma_piezas > 0 else
                0 if suma_piezas == 0 else -1)


    def terminal(self, s):
        return (self.jugadas_legales(s,1) == () ==
                self.jugadas_legales(s,-1))

def pprint(s):
    print(' |', end='')
    for i in 'abcdefgh':
        print(i + '|', end='')
    print('')

    for i in range(8):
        print('-+'*9)

        print(i+1, end='|')
        for j in range(8):
            print(' NB'[s[i*8 + j]],end='|')
        print('')

# función de evaluación del estado para estimar utilidad
def evaluar(s):
	return 'todo'

# heurística para ordenar jugadas.
# regresa las jugadas de mejor a peor.
def ordenar(jugadas, jugador):
	return 'todo'

def crear_jugador_artificial():

    def jugador_primera_accion(juego, estado, jugador):
        acciones = juego.jugadas_legales(estado,jugador)
        return (acciones[0] if acciones != () else None)

    return jugador_primera_accion

def jugador_manual(juego, s, j):
    acciones = juego.jugadas_legales(s,j)
    accion = 0

    while accion not in acciones and acciones != (None,):
        print('\nJugador ' + ('', 'negro', 'blanco')[j])
        for a in acciones:
            print('abcdefgh'[a[1]] + str(a[0]+1), end=' ')
        print('Introduzca acción:')
        entrada = input()

        accion = (int(entrada[1]) - 1, 'abcdefgh'.find(entrada[0]))

    if acciones == (None,):
        print('No hay acciones legales para las piezas ',end='')
        print(('', 'negras', 'blancas')[j],end='\n\n')
        return None

    print(accion, end='\n\n')
    return accion

# `jugador1 son las piezas negras 
# `jugador2 son las piezas blancas
def simulacion(jugador1, jugador2):
    juego = Otello()
    estado, jugador = juego.inicializa()

    while not juego.terminal(estado):
        pprint(estado)
        print('')

        accion = (jugador1 if jugador == 1 else jugador2
                 )(juego, estado, jugador)

        estado = juego.transicion(estado, accion, jugador)

        jugador = -jugador

    print(juego.ganancia(estado))

def main():
    j = crear_jugador_artificial()
    simulacion(j, j)

if __name__ == '__main__':
    main()