from BFS_H6 import World_H6, Heuristics_H6

class QuixoBot:
    # symbol sera un numero representando el simbolo con el que me
    # toca jugar. Puede tener el valor 1 o -1;
    def __init__(self): #SEGUN YO AQUI PUEDE NO RECIBIR COMO PARAMETRO EL 'symbol' PORQUE DE TODAS FORMAS EN EL 'reset' SE LO CAMBIO
        # define a name for your bot to appear during the log printing.
        self.name = "GRH6"
        self.symbol = 0
        self.opponent = 0
        self.bfs_h6 = None

    # board es el estado actual del tablero. Sera una matriz de 5x5 que contiene
    # los siguientes numeros enteros.
    #  0 - blank cubit
    #  1 - X cubit
    # -1 - O cubit
    def play_turn(self, board):
        # Esta funcion debe tomar el tablero actual, simular el movimiento deseado
        # y regresarlo al evaluador.
        # return new_board
        new_board, move = self.bfs_h6.bot(board, Heuristics_H6.heuristic_6)
        return new_board

    # Esta funcion sera llamada antes de empezar una nueva partida,
    # por lo que su proposito es resetear cualquier estado que sea necesario
    # para empezar desde 0.
    # Tambien recibe el nuevo simbolo con el que empezara la partida.
    def reset(self, symbol):
        self.symbol = symbol
        self.opponent = (symbol * -1)
        #Esto lo quite de la función 'play_turn' porque cada que se haga un turno se crea un objeto y solo me interesa crear el objeto al
        # momento de iniciar cada partida (si es necesario que en cada partida lo cree porque se cambian de símbolos)
        self.bfs_h6 = World_H6(self.symbol, self.opponent)

"""# Ejemplo de uso

# Creamos el tablero inicial
board = [[0] * 5 for _ in range(5)]
# Inicializamos el bot 
bot = QuixoBot(1)

# Jugamos un turno con este bot y recibimos el nuevo estado del tablero.
new_board = bot.play_turn(board)"""
