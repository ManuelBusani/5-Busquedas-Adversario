"""
Juego del Otello

El estado se va a representar como una tupla de 64 elementos 
pensandolo como una matriz de 8x8, donde `estado[8*i + j] 
es la casilla en la fila `i y la columna `j.

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

"""

from juegos_simplificado import ModeloJuegoZT2
from juegos_simplificado import juega_dos_jugadores
from minimax import jugador_negamax
from minimax import minimax_iterativo

class Otello(ModeloJuegoZT2):
    def inicializa(self):
        # estado = ([0 for _ in range(9*3)])
        # estado += (1,-1)
        # estado += ([0 for _ in range(6)])
        # estado += (-1,1)
        # estado += ([0 for _ in range(9*3)])
        # return (estado, 1)

        return ((0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 1,-1, 0, 0, 0,
        		 0, 0, 0,-1, 1, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,
        		 0, 0, 0, 0, 0, 0, 0, 0,),
        		1)

    def jugadas_legales(self, s, j):
        return 'todo';
    
    def transicion(self, s, a, j):
        return 'todo';

    def ganancia(self, s):
        return 'todo';

    def terminal(self, s):
        return 'todo';

def pprint(s):
		print('todo')

# función de evaluación del estado para estimar utilidad
def evaluar(s):
	return 'todo'

# heurística para ordenar jugadas.
# regresa las jugadas de mejor a peor.
def ordenar(jugadas, jugador):
	return 'todo'

def crear_jugador_artificial():
	return 'todo'

def jugador_manual(juego, s, j):
	return 'todo'


if __name__ == '__main__':
	juego = Otello()
	s0 = juego.inicializa()
	print(s0)
	print(len(s0))