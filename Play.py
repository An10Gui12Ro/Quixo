from BFSbest_modified_Quixo import Heuristics
from BFSbest_modified_Quixo import World
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

        bfs = World(self.my_symbol, self.opponent)

        while True:
            #Aquí se le cambian las heurísticas(1-4)
            #La 1 y la 3 fueron las mejores (la 1 si busca ganar, y con la 3 me tarde mucho en ganar porque me tapaba todo)
            board, move = bfs.bot(board, Heuristics.heuristic)

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
board = [[0] * 5 for _ in range(5)]
prueba.play(board)