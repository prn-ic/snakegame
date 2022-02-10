from tkinter import *
from random import randint as r
from math import floor

class GameLoop:

    __SCORE = 0
    _WINDOW_WIDTH = 800
    _WINDOW_HEIGHT = 600
    DEFAULT_BODYPARTS = 1
    _PX = 25
    COLOR_SNAKE = 'green'
    COLOR_APPLE = 'red'
    SPEED = 100
    __root = Tk()
    table = Label(__root, text=f"Score: {__SCORE}", font=("Consolas", 16))
    table.pack()
    canvas = Canvas(__root, width=_WINDOW_WIDTH, height=_WINDOW_HEIGHT, bg='black')
    canvas.pack()


    def __init__(self):
        GameLoop.__root.title('SnakeGame')
        GameLoop.__root.resizable(False, False)
        GameLoop.__root.geometry(f'{GameLoop._WINDOW_WIDTH}x{GameLoop._WINDOW_HEIGHT}')
        self._direction = 'down'

    def movement(self, snake, apple):
        for x, y in snake.coord:
            GameLoop.canvas.create_rectangle(x, y, x + GameLoop._PX, y + GameLoop._PX, fill=GameLoop.COLOR_SNAKE)

        x, y = snake.coord[0]

        if self._direction == 'down':
            y += GameLoop._PX
        elif self._direction == 'up':
            y -= GameLoop._PX
        elif self._direction == 'left':
            x -= GameLoop._PX
        elif self._direction == 'right':
            x += GameLoop._PX

        snake.coord.insert(0, (x, y))
        GameLoop.canvas.create_rectangle(x, y, x+GameLoop._PX, y+GameLoop._PX, fill=GameLoop.COLOR_SNAKE)

        if x == apple.coord[0] and y == apple.coord[1]:
            GameLoop.__SCORE += 1
            self.table.config(text=f'Score: {GameLoop.__SCORE}')
            self.canvas.delete('self.apple')
            apple = Apple()
            print('new apple')
        else:
            x, y = snake.coord[-1]
            GameLoop.canvas.create_rectangle(x, y, x + GameLoop._PX, y + GameLoop._PX, fill='black')
            del snake.coord[-1]

        if self.collision(snake):
            print('end')
        else:
            GameLoop.__root.after(GameLoop.SPEED, self.movement, snake, apple)


    def change_move(self, move):
        if (move == 'down'):
            if (self._direction != 'up'):
                self._direction = move
        elif (move == 'up'):
            if (self._direction != 'down'):
                self._direction = move
        if (move == 'left'):
            if (self._direction != 'right'):
                self._direction = move
        if (move == 'right'):
            if (self._direction != 'left'):
               self._direction = move

    def collision(self, snake):
        if snake.coord[0][0] < 0 or snake.coord[0][0] >= GameLoop._WINDOW_WIDTH:
            return True
        elif snake.coord[0][1] < 0  or snake.coord[0][1] >= GameLoop._WINDOW_HEIGHT:
            return True
        for i in snake.coord[1:-1]:
            if snake.coord[0][0] == i[0] and snake.coord[0][1] == i[1]:
                return True 

    def run(self):
        #OBJECTS
        
        #KEYBIND
        GameLoop.__root.bind('<Down>', lambda event: self.change_move('down'))
        GameLoop.__root.bind('<Up>', lambda event: self.change_move('up'))
        GameLoop.__root.bind('<Left>', lambda event: self.change_move('left'))
        GameLoop.__root.bind('<Right>', lambda event: self.change_move('right'))
        #LOOP
        snake = Snake()
        apple = Apple()
        self.movement(snake, apple)
        GameLoop.__root.mainloop()


class Snake:

    def __init__(self):
        self.coord = [[0,0]] * GameLoop.DEFAULT_BODYPARTS
        self.squares = []

        for k, v in self.coord:
            GameLoop.canvas.create_rectangle(k, v, k+GameLoop._PX, v+GameLoop._PX, fill=GameLoop.COLOR_SNAKE)


class Apple:

    def __init__(self):
        #FOR APPLE CREATE IN GAME
        x = r(0, floor(GameLoop._WINDOW_WIDTH/GameLoop._PX)-1) * GameLoop._PX #0-775
        y = r(0, floor(GameLoop._WINDOW_HEIGHT/GameLoop._PX)-1) * GameLoop._PX #0-575
        self.coord = [x, y]

        GameLoop.canvas.create_rectangle(x, y, x+GameLoop._PX, y+GameLoop._PX, fill=GameLoop.COLOR_APPLE)

if __name__ == "__main__":
    GameLoop().run()

