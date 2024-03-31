from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_right(GameSprite):
    def update_right(self):
        kays_pressed = key.get_pressed()
        if kays_pressed[K_UP] and  self.rect.y < win_height:
            self.rect.y -= 5
        if kays_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.x += 5
        
    def update_left(self):
        kays_ = key.get_pressed()
        if kays_pressed[K_UP] and  self.rect.y < win_height:
            self.rect.y -= 5
        if kays_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.x += 5



class Bulet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


lost = 0
life = 3
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

win_width = 700
win_height = 500

img_racket = "rocket.png"
racket_1 = Player(img_hero, 5, win_height - 100, 4, 50, 10)
img_ball = "ufo.png"

run = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
fires = 10
n = 10

font.init()
font1 = font.SysFont("Arial", 80)
win = font1.render("YOU WIN", True, (255, 255, 255))
lose = font1.render("YOU LOSE", True, (180, 0, 0))
font2 = font.SysFont("Arial", 36)

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

while run:
    for e in event.get():
        if e.type == QUIT:
            game = False  
    
    if finish != True:
        window.blit(background,(0, 0))
        rocket_1.update_left()
        rocket_2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        display.update()
        time.delay(50)

    #https://docs.google.com/document/d/1ikWy1_LOgevjmaQupC4PR_zFoSbMOFX7rHNZ05YVpqU/edit
