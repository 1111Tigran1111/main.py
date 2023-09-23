import pygame as pg

from setting import *

class Bot(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speedx = 0
        self.speedy = 0
        self.image = bot_img
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)

    def update(self):

        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx

        self.speedy = 0
        if keystate[pg.K_w]:
            self.speedy = -8
        if keystate[pg.K_s]:
            self.speedy = 8
        self.rect.y += self.speedy

        if self.rect.right > setting['w']:
            self.rect.right = setting['w']
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > setting['h']:
            self.rect.bottom = setting['h']
        if self.rect.top < 0:
            self.rect.top = 0

