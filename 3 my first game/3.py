import pygame as game

#start the game
game.init()

#Background Color
BG = (0,0,0)
PLAYER = (50,0,0)

#Frame per Second
FPS = 30

#resolution
WIDTH = 800
HEIGHT = 700

#set screen
screen = game.display.set_mode((WIDTH, HEIGHT))
#game name
game.display.set_caption('Cat The Dominator')
#time elapsed
clock = game.time.Clock()
#situation
running = True # True if running, False if not running

class Player(game.sprite.Sprite):
    #main function if running class
    def __init__(self):
        game.sprite.Sprite.__init__(self)
        img = '3 my first game\cat.png'
        self.image = game.image.load(img).convert_alpha()
        #self.image = game.Surface((50,50))
        #self.image.fill(PLAYER)

        #create box
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
    
    def update(self):
        self.rect.y += 5
        if self.rect.bottom > HEIGHT:
            self.rect.y = 0

#Create Sprite Group
all_sprites = game.sprite.Group() # box of charactor
player = Player() #create charactor
all_sprites.add(player) #add charactor to box

while running:
    #update
    clock.tick(FPS)

    #Quit program if trick 'X'
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    all_sprites.update()

    #fill the screen
    screen.fill(BG)

    #draw charactor to screen
    all_sprites.draw(screen)
    
    #display 
    game.display.flip()

#quit game
game.quit()