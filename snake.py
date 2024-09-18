import tkinter #for grahics
import random  

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS #25*25 = 625

class Tile:#store x and y position of snake and food
    def __init__(self, x, y):
        self.x = x
        self.y = y


#game window
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas=tkinter.Canvas(window,bg="black",width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
canvas.pack()
window.update()

#to center the window
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize game
snake=Tile(5*TILE_SIZE,5*TILE_SIZE) #single tile, snake's head where here 5 is a pixel
food=Tile(10*TILE_SIZE,10*TILE_SIZE)
snake_body=[]#multiple snake tiles
velocityX=0
velocityY=0
game_over=False
score=0

def change_direction(e): #where e is the event (either up,down,left or right)
    #print(e.keysym) it print what key is entered from the keyboard
    global velocityX,velocityY,game_over

    if(game_over):
        return

    if(e.keysym=="Up" and velocityY!=1):
        velocityX=0
        velocityY=-1
    elif (e.keysym=="Down" and velocityY!=-1):
        velocityX=0
        velocityY=1
    elif (e.keysym=="Left" and velocityX!=1):
        velocityX=-1
        velocityY=0
    elif (e.keysym=="Right"and velocityX!=-1):
        velocityX=1
        velocityY=0
def move():
    global snake,food, snake_body,game_over,score

    #game over conditions
    if(game_over):
        return
    if(snake.x<0 or snake.x>=WINDOW_WIDTH or snake.y<0 or snake.y>=WINDOW_HEIGHT):#if snake moves over the boundary
        game_over=True
        return
    for tile in snake_body: #if snake collide with its body
        if(snake.x==tile.x and snake.y==tile.y):
            game_over=True
            return 
    

    #collision
    if(snake.x==food.x and snake.y==food.y):
        snake_body.append(Tile(food.x,food.y))
        food.x=random.randint(0,COLS-1) * TILE_SIZE
        food.Y=random.randint(0,ROWS-1) * TILE_SIZE
        score+=1

    #update snake body while moving
    for i in range(len(snake_body)-1,-1,-1):
        tile=snake_body[i]
        if(i==0):
            tile.x=snake.x
            tile.y=snake.y
        else:
            prev_title=snake_body[i-1]
            tile.x=prev_title.x
            tile.y=prev_title.y

    snake.x+=velocityX*TILE_SIZE
    snake.y+=velocityY*TILE_SIZE
def draw():
    global snake,food,snake_body,game_over,score#here the score is updated so it is mandatory to declare here.
    move()

    canvas.delete("all")

    #draw food
    canvas.create_rectangle(food.x,food.y,food.x+TILE_SIZE,food.y+TILE_SIZE, fill="red")

    #draw snake
    canvas.create_rectangle(snake.x,snake.y,snake.x+TILE_SIZE,snake.y+TILE_SIZE, fill="lime green")

    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x+TILE_SIZE,tile.y+TILE_SIZE, fill="lime green")
    
    #to print the score
    if(game_over):
        canvas.create_text(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,font="Arial 20",text=f"Game Over:{score}",fill="white")
    else:
        canvas.create_text(30,20,font="Arial 10",text=f"Score:{score}",fill="white")
    
    window.after(100,draw) #100ms i.e for every 1/10 second call the draw function

draw()

window.bind("<KeyRelease>",change_direction)

window.mainloop()