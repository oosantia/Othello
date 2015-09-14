class InvalidOthelloMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass


class OthelloGameOver(Exception):
    '''
    Raised whenever there is no moves left for both players
    '''
    pass


class Othello:
    def __init__(self,num_rows:int,num_columns:int,initial_player:str,top_position:str,deafault:bool):
        '''initiates all self values of the othello class'''
        self.rows = num_rows
        self.columns = num_columns
        self.current_player = initial_player
        self.other_player = initial_player
        self.current_p_points = 0;
        self.other_p_points = 0;
        self.black = "Black"
        self.white = "White"
        self.NONE = ' '
        self.default = deafault
        self.game_over = False
        self.black_points = 2
        self.white_points = 2
        self.board = self.initialize_board(self.rows,self.columns,top_position)
        self.set_initial_player();
        
    def initialize_board(self,rows:int,columns:int,top_position)->[str]:
        '''Initializes the board with given colums, rows and top left most position player'''
        self._require_valid_column_number(columns-1)
        self._require_valid_row_number(rows-1)
        board = []
        if(top_position == self.black):
            other = self.white
        else:
            other = self.black
        for row in range(rows):
            board.append([])
            for col in range(columns):
                board[-1].append(self.NONE)
        board[int(row/2)][int(columns/2)-1] = top_position
        board[int(row/2)+1][int(columns/2)-1] = other
        board[int(row/2)][int(columns/2)] = other
        board[int(row/2)+1][int(columns/2)] = top_position
        return board
    
    def set_initial_player(self):
        '''sets the initial pleyer and other player'''
        if self.current_player == self.black:
            self.other_player = self.white
        else:
            self.other_player = self.black
        
    def _is_in_board(self,row_num:int ,col_num:int):
        '''checks if given row and column is in the board returns false if they are not'''
        return (self._is_valid_row_number(row_num)and self._is_valid_column_number(col_num))

    def get_player(self):
        '''return current player'''
        return self.current_player
    def opposite_player(self):
        '''return non current player'''
        return self.other_player

    def make_move(self,x:int, y:int):
        '''Given a row and a column computes move if not able than raises a exeption'''
        if self.game_over == True:
            raise OthelloGameOver()
        self._require_valid_row_number(x)
        self._require_valid_column_number(y)
        if self._is_in_board(x,y) == False:
            raise invalidOthelloMove()
        move_set = self._is_valid_move(x,y)
        if(move_set != []):
            self._flip_tiles(x,y,move_set)
        else:
            raise InvalidOthelloMoveError()
        self._update_points()
        self._compute_player()

    def _flip_tiles(self,x:int,y:int,move_set:[list])->None:
        '''Flip the tiles corresponing with given coordinates'''
        self.board[x][y] = self.current_player
        self.current_p_points +=1
        for move in move_set:
            x_move = x + move[0]
            y_move = y + move[1]
            while(self.board[x_move][y_move] != self.current_player):
                self.board[x_move][y_move] = self.current_player
                self.current_p_points +=1
                self.other_p_points -=1
                x_move += move[0]
                y_move += move[1]
        
    def _is_valid_move(self,x:int,y:int)->[list]:
        '''checks if given cordinates is a valid move for current player'''
        to_return  = []
        if(self.board[x][y] != self.NONE):
            return to_return
        possible_moves = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for move in possible_moves:
            x_move = x + move[0]
            y_move = y + move[1]
            while(self._is_in_board(x_move,y_move)):
                if(self.board[x_move][y_move] == self.NONE):
                    break
                elif(self.board[x_move][y_move] == self.current_player):
                    if(x + move[0] == x_move and y + move[1]== y_move):
                        break
                    else:
                        to_return.append([move[0],move[1]])
                x_move += move[0]
                y_move += move[1]
        return to_return
    def get_winner(self)->str:
        '''returns the string contiang the winner in case of tie current is declare winner'''
        if(self.default == True):
            if(self.black_points > self.white_points):
                return 'The winnner is '+self.black
            elif(self.black_points < self.white_points):
                return 'The winnner is '+self.white
        else:
            if(self.black_points < self.white_points):
                return 'The winnner is '+self.black
            elif(self.black_points > self.white_points):
                return 'The winnner is '+self.white
            return "Game is a Tie"
        
    def has_valid_move(self,player:str)->bool:
        '''check if paramater player has a valid move'''
        prev_player = self.current_player
        self.current_player = player
        for i in range(self.rows):
            for j in range(self.columns):
                if(self._is_valid_move(i,j) != []):
                    self.current_player = prev_player
                    return True
        self.current_player = prev_player
        return False
    
    def _update_points(self)->None:
        '''Updates the points after flipping has occured'''
        if(self.current_player == self.black):
            self.black_points += self.current_p_points
            self.white_points += self.other_p_points
        else:
            self.black_points += self.other_p_points
            self.white_points += self.current_p_points
        self.other_p_points = 0
        self.current_p_points = 0
    def _compute_player(self):
        '''computes if players have valid moves if not raises exeption'''
        if(self.has_valid_move(self.other_player)):
            self._change_player()
        elif(self.has_valid_move(self.current_player)!= True and (self.has_valid_move(self.other_player) != True)):
            self.game_over = True
            raise OthelloGameOver()
     
    def _change_player(self):
        '''changes the player from current to other'''
        prev_player = self.current_player
        self.current_player = self.other_player
        self.other_player = prev_player
        
    def _require_valid_column_number(self,column_number: int) -> None:
        '''Raises a ValueError if its parameter is not a valid column number'''
        if type(column_number) != int or not self._is_valid_column_number(column_number):
            raise ValueError('column_number must be int between 0 and {}'.format(self.columns))

    def _require_valid_row_number(self,row_number: int) -> None:
        '''Raises a ValueError if its parameter is not a valid column number'''
        if type(row_number) != int or not self._is_valid_row_number(row_number):
            raise ValueError('row_number must be int between 0 and {}'.format(self.rows))
        
    def _is_valid_column_number(self,column_number: int) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        return 0 <= column_number< self.columns



    def _is_valid_row_number(self,row_number: int) -> bool:
        '''Returns True if the given row number is valid; returns False otherwise'''
        return 0<= row_number < self.rows
