import os
import pygame as pg

setting = {
    'w': 541,
    'h': 504,
    'title': '?????????????',
    'fps': 60,
}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')
font_folder = os.path.join(game_folder, 'font')

player_img = pg.image.load(os.path.join(media_folder, 'player.png'))
bot_img = pg.image.load(os.path.join(media_folder, 'pacsus.png'))


obstacle_img = pg.image.load(os.path.join(media_folder, 'лабиринт.png'))


decrypted = os.path.join(font_folder, '??????.????')
clock = pg.time.Clock()