from BFSbest_modified_Quixo import World, Heuristics
from BFS_H5 import Heuristics_H5
from BFS_H5 import World_H5
from BFS_H6 import Heuristics_H6
from BFS_H6 import World_H6
from BFS_H7 import Heuristics_H7
from BFS_H7 import World_H7
from BFS_H8 import Heuristics_H8
from BFS_H8 import World_H8
from BFS_H9 import Heuristics_H9
from BFS_H9 import World_H9
from QuixoMovements import Movements

class QuixoBot:
    # symbol sera un numero representando el simbolo con el que me
    # toca jugar. Puede tener el valor 1 o -1;
    def __init__(self, symbol):
        self.my_symbol = symbol

        if self.my_symbol == 1:
            self.opponent = -1
        else:
            self.opponent = 1

    # board es el estado actual del tablero. Sera una matriz de 5x5 que contiene
    # los siguientes numeros enteros.
    #  0 - blank cubit
    #  1 - X cubit
    # -1 - O cubit
    def play_turn(self, board):
        #Se importa cada archivo y después creo el objeto y mando a llamar a la función y que me regrese el tablero
        
        # Esta funcion debe tomar el tablero actual, simular el movimiento deseado
        # y regresarlo al evaluador.
        # return new_board
        pass

    # Esta funcion sera llamada antes de empezar una nueva partida,
    # por lo que su proposito es resetear cualquier estado que sea necesario
    # para empezar desde 0.
    # Tambien recibe el nuevo simbolo con el que empezara la partida.
    def reset(self, symbol):
        pass



    def play(self):
        board = [[0] * 5 for _ in range(5)]
        w1 = 0
        w2 = 0
        print("Welcome to Quixo!")
        self.print_board(board)

        bfs8 = World_H8(self.my_symbol, self.opponent)
        bfs9 = World_H9(self.opponent, self.my_symbol)

        for i in range(20):
            board = [[0] * 5 for _ in range(5)]
            for j in range(100):
                board, move = bfs9.bot(board, Heuristics_H9.heuristic_9)
                
                winner = Movements(board)
                if winner.i_win(self.my_symbol):
                    w1 += 1
                    break
                if winner.i_win(self.opponent):
                    w2 += 1
                    break
                
                board, move = bfs8.bot(board, Heuristics_H8.heuristic_8)

                winner = Movements(board)
                if winner.i_win(self.my_symbol):
                    w1 += 1
                    break
                if winner.i_win(self.opponent):
                    w2 += 1
                    break

            self.print_board(board)
        print( "bfs8 = ", w1)
        print("bfs9 = ", w2)
    
    
    
    def print_board(self, board):
        for i in range(5):
            print("-----------------------------")
            for j in range(5):
                print(board[i][j], end = "  |  ")
            print()



"""# Ejemplo de uso

# Creamos el tablero inicial
board = [0 * 5 for _ in range(5)]
# Inicializamos el bot 
bot = QuixoBot(1)

# Jugamos un turno con este bot y recibimos el nuevo estado del tablero.
new_board = bot.play_turn(board)"""

prueba = QuixoBot(1)
prueba.play()