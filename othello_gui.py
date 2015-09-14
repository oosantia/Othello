#Omar Santiago
#32076043
import othello_class
import tkinter

DEFAULT_FONT = ('Helvetica', 20)



class GreetingsApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()

        welcome_frame = tkinter.Frame(master = self._root_window)
        welcome_frame.grid(
            row = 0, column = 0, padx = 10, pady = 10)

        welcome_label = tkinter.Label(
           master = welcome_frame, text = "Welcome to Othello!",
           font = DEFAULT_FONT)

        welcome_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._play_text = tkinter.StringVar()
        self._play_text.set("Press Start to begin or cancel to Quit")
        play_label = tkinter.Label(
           master = welcome_frame, textvariable = self._play_text,
           font = DEFAULT_FONT)

        play_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        Start_button = tkinter.Button(
            master = self._root_window, text = 'Start', font = DEFAULT_FONT,
            command = self._on_start)

        Start_button.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
        cancel_button = tkinter.Button(
            master = self._root_window, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel)

        cancel_button.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)


    def start(self) -> None:
        '''loops root_window'''
        self._root_window.mainloop()


    def _on_start(self) -> None:
        '''Event when start is clicked'''
        dialog = OptionsWindow()
        dialog.show()
        
        if dialog.was_ok_clicked():
            Othello_GUI(othello_class.Othello(int(dialog.get_rows()),int(dialog.get_columns()),dialog.get_first(),dialog.get_top(),dialog._default)).start()

    def _on_cancel(self) -> None:
        '''Destroy window when cancel is clicked'''
        self._root_window.destroy()



class OptionsWindow:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        self.top_player ="White"
        self.first_player = "Black"
        self.rows = 4
        self.col = 4
        self._ok_clicked = False
        self._default = True

        menu_frame = tkinter.Frame(master = self._dialog_window)

        menu_frame.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.S)
        self._col_scale = tkinter.Scale(master = menu_frame, command = self._on_col_scale, length = 275,font = DEFAULT_FONT, orient = tkinter.HORIZONTAL, from_ = 4, to = 16,resolution = 2,label = "Number of Columns")
        self._col_scale.grid(row = 0, column = 0,sticky = tkinter.W + tkinter.S)
        self._row_scale = tkinter.Scale(master = menu_frame,command = self._on_row_scale, length = 225, font = DEFAULT_FONT, orient = tkinter.HORIZONTAL, from_ = 4, to = 16,resolution = 2, label = 'Number of Rows')
        self._row_scale.grid(row = 0, column = 1,sticky = tkinter.W + tkinter.S)
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        First_label = tkinter.Label(master = button_frame, text = "First Player",font = DEFAULT_FONT)
        First_label.grid(row = 0, column = 0)
        self.black_button = tkinter.Button(
            master = button_frame, text = 'Black Player', font = DEFAULT_FONT,  relief = tkinter.SUNKEN,
            command = self._on_Black_button)

        self.black_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.white_button = tkinter.Button(
            master = button_frame, text = 'White Player', font = DEFAULT_FONT,
            command = self._on_White_button)

        self.white_button.grid(row = 0, column = 2, padx = 10, pady = 10)

        top_label = tkinter.Label(master = button_frame, text = "Top Player",font = DEFAULT_FONT)
        top_label.grid(row = 1, column = 0)

        self.black2_button = tkinter.Button(
            master = button_frame, text = 'Black Player', font = DEFAULT_FONT,
            command = self._on_Black2_button)

        self.black2_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.white2_button = tkinter.Button(
            master = button_frame, text = 'White Player', font = DEFAULT_FONT, relief = tkinter.SUNKEN,
            command = self._on_White2_button)

        self.white2_button.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        Win_label = tkinter.Label(master = button_frame, text = "Win Conditions",font = DEFAULT_FONT)
        Win_label.grid(row = 2, column = 0)
        
        self.high_button = tkinter.Button(
            master = button_frame, text = 'Higher Wins', font = DEFAULT_FONT,relief = tkinter.SUNKEN,
            command = self._on_high_button)

        self.high_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.low_button = tkinter.Button(
            master = button_frame, text = 'Lower Wins', font = DEFAULT_FONT,
            command = self._on_low_button)

        self.low_button.grid(row = 2, column = 2, padx = 10, pady = 10)

        button2_frame = tkinter.Frame(master = self._dialog_window)

        button2_frame.grid(
            row = 6, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button2_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button2_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def _on_row_scale(self, event_int:int)->None:
        '''sets rows to the given integer by scale event attaced to '''
        self.rows = event_int
    def _on_col_scale(self, event_int:int)->None:
        '''sets cols to the given integer by scale event attaced to '''
        self.col = event_int

    def _on_Black2_button(self) -> None:
        '''sets the top player to the corresponding string given by button and interchanges the selected choice'''
        self.top_player = "Black"
        self.black2_button.configure(relief = tkinter.SUNKEN)
        self.white2_button.configure(relief = tkinter.RAISED)

    def _on_White2_button(self) -> None:
        '''sets the top player to the corresponding string given by button and interchanges the selected choice'''
        self.top_player = "White"
        self.White2_button.configure(relief = tkinter.SUNKEN)
        self.black2_button.configure(relief = tkinter.RAISED)
        
    def _on_Black_button(self) -> None:
        '''sets the first player to the corresponding string given by button and interchanges the selected choice'''
        self.first_player = "Black"
        self.black_button.configure(relief = tkinter.SUNKEN)
        self.white_button.configure(relief = tkinter.RAISED)

    def _on_White_button(self) -> None:
        '''sets the first player to the corresponding string given by button and interchanges the selected choice'''
        self.first_player = "White"
        self.white_button.configure(relief = tkinter.SUNKEN)
        self.black_button.configure(relief = tkinter.RAISED)


    def _on_high_button(self) -> None:
        '''sets the dafault winning condition given by the user'''
        self._default = True
        self.high_button.configure(relief = tkinter.SUNKEN)
        self.low_button.configure(relief = tkinter.RAISED)

    def _on_low_button(self) -> None:
        '''sets the dafault winning condition given by the user'''
        self._default = False
        self.low_button.configure(relief = tkinter.SUNKEN)
        self.high_button.configure(relief = tkinter.RAISED)
        
    def was_ok_clicked(self) -> bool:
        '''Checks if ok button was pressed'''
        return self._ok_clicked
    
    def _on_ok_button(self) -> None:
        '''Changes ok button bool to true and destroys windows'''
        self._ok_clicked = True
        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        '''Destroys window when cancel is pressed'''
        self._dialog_window.destroy()

    def get_top(self)->str:
        '''Returns String of top player'''
        return self.top_player
    
    def get_first(self)->str:
        '''return string of first player'''
        return self.first_player

    def get_rows(self)->int:
        '''returns the number of rows'''
        return int(self.rows)

    def get_columns(self)->int:
        '''return the number of columns'''
        return int(self.col)


class Othello_GUI:
    def __init__(self,game:othello_class):
        self._root_window = tkinter.Toplevel()
        self._cell_height = 40
        self._cell_width = 40
        self._game = game
        self._canvas = tkinter.Canvas(master = self._root_window, background = '#600000',
                                    height = self._cell_height*self._game.rows,
                                    width = self._cell_width*self._game.columns)
        self._canvas.grid(
            row = 0, column = 0, columnspan = self._game.columns, rowspan = self._game.rows, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._status_text = tkinter.StringVar()
        self._status_text.set('Score: B:2 W:2')
        self._player_text = tkinter.StringVar()
        self._player_text.set('Its {} Turn!'.format(self._game.get_player()))
        status_frame = tkinter.Frame(master = self._root_window)
        status_frame.grid(
            row = self._game.rows+1, column = 0, padx = 10, pady = 10)
        status_label = tkinter.Label(
           master = status_frame, textvariable = self._status_text,width = 19,
           font = DEFAULT_FONT)

        status_label.grid(
            row = 0, column = 1,columnspan = self._game.columns-1, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._player_label = tkinter.Label(
           master = status_frame, textvariable = self._player_text,width = 18,
           font = DEFAULT_FONT,bg = self._game.get_player(),fg = self._game.opposite_player())

        self._player_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E)
                              
        self.bigger = self._game.rows
        if(self._game.columns > self._game.rows):
            self.bigger = self._game.columns
        for i in range(self._game.rows):
            self._canvas.create_line(0, i*self._cell_height,
                                   self._cell_width*self.bigger, i*self._cell_height)
        for i in range(self._game.columns):
            self._canvas.create_line(i*self._cell_width, 0,
                                   self._cell_width*self.bigger, self._cell_height*self.bigger)
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(self._game.rows ,weight = 1)
        
    def start(self):
        '''loops main window'''
        self._root_window.grab_set()
        self._root_window.wait_window()
        self._root_window.mainloop()
        
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''deletes all canvas items and redraws them by calling proper functions '''
        self._canvas.delete(tkinter.ALL)
        self._cell_width = self._canvas.winfo_width()/self._game.columns
        self._cell_height = self._canvas.winfo_height()/self._game.rows
        self._redraw_grid()
        self._redraw_board()

    def _redraw_grid(self):
        '''redrawas grid lines'''
        for i in range(self._game.rows):
            self._canvas.create_line(0, i*self._cell_height,
                                   self._cell_width*self.bigger, i*self._cell_height)
        for i in range(self._game.columns):
            self._canvas.create_line(i*self._cell_width, 0,
                                   self._cell_width*i, self._cell_height*self.bigger)

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''Checks if current cordinates given is a valid move'''
        try:
            self._game.make_move(int(event.y/self._cell_height),int(event.x/self._cell_width))
        except othello_class.InvalidOthelloMoveError:
            return
        except othello_class.OthelloGameOver:
            self._player_text.set('{}'.format(self._game.get_winner()))
        else:
            self._player_text.set('Its {} Turn!'.format(self._game.get_player()))
        finally:
            self._canvas.delete(tkinter.ALL)
            self._status_text.set('Score: B:{} W:{}'.format(self._game.black_points,self._game.white_points))
            self._player_label.configure(bg = self._game.get_player(), fg = self._game.opposite_player())
            self._redraw_grid()
            self._redraw_board()

    def _redraw_board(self) -> None:
        '''redrawsoard'''
        for row in range((self._game.rows)):
            for col in range(self._game.columns):
                 if not self._game.board[row][col] == " ":
                    self._canvas.create_oval(
                        col * self._cell_width, row *self._cell_height,(col * self._cell_width) + self._cell_width, row *self._cell_height + self._cell_height,
                        fill = self._game.board[row][col], outline = '#000000')

if __name__ == '__main__':
    GreetingsApplication().start()
