import pygame as pg
from player import Player
from bot import Bot
from setting import *

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])
run = True
score = 0

all_sprite = pg.sprite.Group()
player = Player()
bot = Bot()
bot_group = pg.sprite.Group()
bot_group.add(bot)
all_sprite.add(player)
all_sprite.add(bot)

while run:

    clock.tick(setting['fps'])
    pg.display.flip()
    screen.blit(obstacle_img, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if pg.sprite.spritecollide(player, bot_group, False,  pg.sprite.collide_circle):
    if pg.sprite.spritecollide(player, bot_group, False,  pg.sprite.collide_circle):
        run = False

    all_sprite.draw(screen)
    all_sprite.update()
    pg.display.flip()

pg.quit()