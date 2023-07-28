import pygame as pg

pg.init()
tela = pg.display.set_mode((1200, 700))

status = True
while status:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            status = False
pg.quit()