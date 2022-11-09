from src.main import *
import tkinter as tk

def test_change_direction():
    root=tk.Tk()
    newCanvas=Canvas(root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    newCanvas.pack()
    root.update()

    window_width=root.winfo_width()
    window_height=root.winfo_height()
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()

    x=int((screen_width/2 - window_width/2))
    y=int((screen_height/2 - window_height/2))

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    direction='down'
    #newSnake=Snake(newCanvas)
    #newFood=Food(newCanvas)
    newDirection='right'
    direction=change_direction(direction, newDirection)
    assert (direction==newDirection)


 

