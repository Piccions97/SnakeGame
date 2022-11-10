from src.main import *
import tkinter as tk

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
newSnake=Snake(newCanvas)

def test_change_direction():
    newDirection='right'
    direction=change_direction(newDirection)
    assert (direction==newDirection)

def test_check_collision():
    newSnake.coordinates[0]=[-1, 0]
    assert check_collisions(newSnake)
    newSnake.coordinates[0]=[1001, 0]
    assert check_collisions(newSnake)
    newSnake.coordinates[0]=[0, -1]
    assert check_collisions(newSnake)
    newSnake.coordinates[0]=[0, 701]
    assert check_collisions(newSnake)
    newSnake.coordinates[1]=newSnake.coordinates[0]
    assert check_collisions(newSnake)

def test_correct_istances():
    newSnake=Snake(newCanvas)
    assert isinstance(newSnake, Snake)

def test_next_turn():
    

