from tabulate import tabulate
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



    def play(self, board):
        print("Welcome to Quixo!")
        self.print_board(board)

        """bfs_h5 = World_H5(self.my_symbol, self.opponent)"""
        bfs_h6 = World_H6(self.my_symbol, self.opponent)
        #SI ME TRATA DE TAPAR PERO CUANDO TIENE LA OPORTUNIDAD PREFIERE HACERLA PARA ÉL Y SI POR EJEMPLO YO TENIA 4 ÉL LA HACIA PARA EL DE TAL FORMA QUE YO NO
        # JUNTARA LOS 5 DONDE ESTABAN ESOS 4 (ese es el chiste de la heurística, de mis mejores agarro la peor, por lo tanto la que yo tenía pensado hacer no 
        # la hice e hice otra que obviamente iba a ser mejor para él)
        """bfs_h7 = World_H7(self.my_symbol, self.opponent)"""
        #E LA 8 NO ESTA NADA MAL, JUEGA MUY BIEN (no le tenía tanta fe pero si es buena)
        """bfs_h8 = World_H8(self.my_symbol, self.opponent)"""
        #TAMBIÉN ES BUENA EEE
        """bfs_h9 = World_H9(self.my_symbol, self.opponent)"""

        while True:
            """board, move = bfs_h5.bot(board, Heuristics_H5.heuristic_5)"""
            board, move = bfs_h6.bot(board, Heuristics_H6.heuristic_6)
            """board, move = bfs_h7.bot(board, Heuristics_H7.heuristic_7)"""
            """board, move = bfs_h8.bot(board, Heuristics_H8.heuristic_8)"""
            """board, move = bfs_h9.bot(board, Heuristics_H9.heuristic_9)"""

            print("Computer's move:", move)
            self.print_board(board)

            winner = Movements(board)
            if winner.i_win(self.my_symbol) or winner.i_win(self.opponent):
                break
            
            #A PARTIR DE AQUI ES PARA EL MOVIMIENTO MANUAL#
            #-------------------------------------------------------------#
            x = True
            while x:
                mov = input("Insert your move like this 00D, the first number represents the rows (0-4), the second the columns (0-4), and the direction (Down 'D', Up 'U', Right 'R', Left 'L') \n")   
                i = int(mov[0])
                j = int(mov[1])
                m = mov[2]

                if (board[i][j] == 0 or board[i][j] == self.opponent) and (not 1 <= i <= 3 or not 1 <= j <= 3):
                    if (m == 'U' and i != 0) or (m == 'R' and j != 4) or (m == 'D' and i != 4) or (m == 'L' and j != 0):
                        x = False
                        movs = Movements(board)
                        board = movs.moves(mov, self.opponent)

                        self.print_board(board)
                    else:
                        print("Move not allowed, try again")
                else:
                    print("Move not allowed, try again")
            
            winner = Movements(board)
            if winner.i_win(self.my_symbol) or winner.i_win(self.opponent):
                break
    #AQUI AQUI AQUI
    """def print_board(self, board):
        for i in range(5):
            print("-----------------------------")
            for j in range(5):
                print(board[i][j], end = "  |  ")
            print()"""
    #AQUI AQUI AQUI
    def print_board(self, board=None):
        if board is None:
            board = self.board
        headers = [""] + [str(i) for i in range(1, 6)]
        rows = [[str(i + 1)] + ['O' if cell == -1 else 'X' if cell == 1 else ' ' for cell in row] for i, row in enumerate(board)]
        print(tabulate(rows, headers=headers, tablefmt="grid"))



"""# Ejemplo de uso

# Creamos el tablero inicial
board = [0 * 5 for _ in range(5)]
# Inicializamos el bot 
bot = QuixoBot(1)

# Jugamos un turno con este bot y recibimos el nuevo estado del tablero.
new_board = bot.play_turn(board)"""

prueba = QuixoBot(1)
board = [[0] * 5 for _ in range(5)]
prueba.play(board)