from pygame import *
import gif_pygame
import pygame
window=display.set_mode((700,500))
display.set_caption('Догонялки')
background=transform.scale(image.load('фон.png'),(700,500))
game= True
clock=time.Clock()
mixer.init()
mixer.music.load('IMUGION - On the base (zaycev.net).mp3')
mixer.music.play()
mixer.music.set_volume(0.5)
kick=mixer.Sound('звук_удара.mp3')
oil=mixer.Sound('шкварчание_масла.mp3')
duck=mixer.Sound('крик_утки.mp3')
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.width=40
        self.rect.height=40
        self.rect.x=player_x
        self.rect.y=player_y
        self.flag_L=True
        self.flag_R= True
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
           self.flag_R=True
           if self.flag_L:
               self.image = pygame.transform.flip(self.image, True, False)
               self.flag_L=False
       if keys[K_d] and self.rect.x < 700 - 80:
           self.rect.x += self.speed
           self.flag_L = True
           if self.flag_R:
               self.image = pygame.transform.flip(self.image, True, False)
               self.flag_R = False
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 500 - 80:
           self.rect.y += self.speed
class Wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y, wall_width,wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((97, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
player=Player('утка1.png',60,450,2)
fire=Player('огонь.png',400,400,0)
#fire = pygame.transform.scale(fire, (40, 60))
eggs=GameSprite('яйца.png',564,300,0)
w1=Wall(150,150,10,350)
w2=Wall(150,150,300,10)
w3=Wall(550,1,10,350)
w4=Wall(260,351,290,10)
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
Winorlose=True
while game:
    if Winorlose:
        window.blit(background,(0,0))
        fire.reset()
        eggs.reset()
        player.reset()
        player.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        if sprite.collide_rect(player, eggs):
            window.blit(win, (200, 200))
            Winorlose = False
        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, fire):
            window.blit(lose, (200, 200))
            Winorlose = False
        display.update()
        clock.tick(244)
    for e in event.get():
        if e.type==QUIT:
            game = False
