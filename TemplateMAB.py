from BFS_H5 import World_H5, Heuristics_H5
from BFS_H6 import World_H6, Heuristics_H6
from BFS_H7 import World_H7, Heuristics_H7
from BFS_H8 import World_H8, Heuristics_H8
from BFS_H9 import World_H9, Heuristics_H9

class QuixoBotMAB:
    # symbol sera un numero representando el simbolo con el que me
    # toca jugar. Puede tener el valor 1 o -1;
    def __init__(self): #SEGUN YO AQUI PUEDE NO RECIBIR COMO PARAMETRO EL 'symbol' PORQUE DE TODAS FORMAS EN EL 'reset' SE LO CAMBIO
        # define a name for your bot to appear during the log printing.
        self.name = "MAB"
        self.symbol = 0
        self.opponent = 0
        self.game = 0
        #self.rewards = [[0, 51], [0,0], [0,0]]
        self.rewards = [0,0,0]
        self.win = 0
        self.bfs_h5 = None
        self.bfs_h6 = None
        self.bfs_h7 = None
        self.bfs_h8 = None
        self.bfs_h9 = None
        self.bfs_final = None

    # board es el estado actual del tablero. Sera una matriz de 5x5 que contiene
    # los siguientes numeros enteros.
    #  0 - blank cubit
    #  1 - X cubit
    # -1 - O cubit
    def play_turn(self, board):
        # Esta funcion debe tomar el tablero actual, simular el movimiento deseado
        # y regresarlo al evaluador.
        # return new_board
        if self.game == 1:
            new_board, move = self.bfs_h9.bot(board, Heuristics_H9.heuristic_9)
        elif self.game == 2:
            new_board, move = self.bfs_h5.bot(board, Heuristics_H5.heuristic_5)
        elif self.game == 3:
            new_board, move = self.bfs_h8.bot(board, Heuristics_H8.heuristic_8)
        elif self.game == 4:
            new_board, move = self.bfs_h7.bot(board, Heuristics_H7.heuristic_7)
        elif self.game == 5:
            new_board, move = self.bfs_h6.bot(board, Heuristics_H6.heuristic_6)
        else:
            new_board = self.heuristic_bot_to_exploit(board)

        return new_board

    # Esta funcion sera llamada antes de empezar una nueva partida,
    # por lo que su proposito es resetear cualquier estado que sea necesario
    # para empezar desde 0.
    # Tambien recibe el nuevo simbolo con el que empezara la partida.
    def reset(self, symbol):
        if (self.game > 0) and (self.game <= 5):
            if self.win == self.symbol:
                self.rewards[0] = self.game
            elif self.win == self.opponent:
                self.rewards[2] = self.game
            else:
                self.rewards[1] = self.game
        self.game += 1
        self.symbol = symbol
        self.opponent = (symbol * -1)
        #Esto lo quite de la función 'play_turn' porque cada que se haga un turno se crea un objeto y solo me interesa crear el objeto al
        # momento de iniciar cada partida (si es necesario que en cada partida lo cree porque se cambian de símbolos)
        if self.game == 1:
            self.bfs_h9 = World_H9(self.symbol, self.opponent)
        elif self.game == 2:
            self.bfs_h5 = World_H5(self.symbol, self.opponent)
        elif self.game == 3:
            self.bfs_h8 = World_H8(self.symbol, self.opponent)
        elif self.game == 4:
            self.bfs_h7 = World_H7(self.symbol, self.opponent)
        elif self.game == 5:
            self.bfs_h6 = World_H6(self.symbol, self.opponent)
        else:
            self.heuristic_to_exploit()

    def who_win(self, s):
        self.win = s
    
    def heuristic_to_exploit(self):
        for i in range(len(self.rewards)):
            if self.rewards[i] != 0:
                if self.rewards[i] == 1:
                    self.bfs_final = World_H9(self.symbol, self.opponent)
                elif self.rewards[i] == 2:
                    self.bfs_final = World_H5(self.symbol, self.opponent)
                elif self.rewards[i] == 3:
                    self.bfs_final = World_H8(self.symbol, self.opponent)
                elif self.rewards[i] == 4:
                    self.bfs_final = World_H7(self.symbol, self.opponent)
                else:
                    self.bfs_final = World_H6(self.symbol, self.opponent)
                break
    
    def heuristic_bot_to_exploit(self, board):
        for i in range(len(self.rewards)):
            if self.rewards[i] != 0:
                if self.rewards[i] == 1:
                    new_board, move = self.bfs_final.bot(board, Heuristics_H9.heuristic_9)
                elif self.rewards[i] == 2:
                    new_board, move = self.bfs_final.bot(board, Heuristics_H5.heuristic_5)
                elif self.rewards[i] == 3:
                    new_board, move = self.bfs_final.bot(board, Heuristics_H8.heuristic_8)
                elif self.rewards[i] == 4:
                    new_board, move = self.bfs_final.bot(board, Heuristics_H7.heuristic_7)
                else:
                    new_board, move = self.bfs_final.bot(board, Heuristics_H6.heuristic_6)
                return new_board

#Si estaba funcionando bien, con lo de 'si gana y tiene menor turnos reemplazalo, o si empata reemplazalo o si pierde con mayor turnos reemplazalo'
#El problema  fue que no era tanta la exploración lo cual no me daba una respuesta tan precisa
#Ahora lo que intentaré es ordenarlas de peor heurística a mejor heurística y probarlas en ese orden, eso me asegura que si la mejor gana se quedará
# con esa y si no gana la mejor, tengo la seguridad de que una heurística anterior si pudo a ver si mejor y me quedo con esa
