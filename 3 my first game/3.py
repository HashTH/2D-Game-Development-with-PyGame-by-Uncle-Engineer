import pygame as game

#start the game
game.init()

#Background Color
BG = (0,0,0)

#Frame per Second
FPS = 60

#resolution
WIDTH = 800
HEIGHT = 700

#set screen
screen = game.display.set_mode((WIDTH, HEIGHT))
#game name
game.display.set_caption('Zero to Draw')
#time elapsed
clock = game.time.Clock()
#situation
running = True # True if running, False if not running
while running:
    #update
    clock.tick(FPS)

    #Quit program if trick 'X'
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    #fill the screen
    screen.fill(BG)
    
    #display 
    game.display.flip()

#quit game
game.quit()