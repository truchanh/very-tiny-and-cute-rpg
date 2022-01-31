# A small program using pygame and
# spritesheet to produce animation sprite
# this file contains the main game window
# after download this repo you must run
# this file to actually run the game! have fun (@^-^@)

import pygame as pg
from setting import WINW, WINH, FPS, TILESIZE
from player import Player


class Game(pg.sprite.LayeredUpdates):
    def __init__(self):
        pg.init()
        super().__init__()
        self.screen = pg.display.set_mode((WINW, WINH))
        pg.display.set_caption('very tiny & cute rpg')
        self.clock = pg.time.Clock()
        self.done = False
        self.run()

    def run(self):
        self.instantiate()
        self.mainloop()

    def instantiate(self):
        self.player = Player((0, 0), TILESIZE)
        self.add(self.player)

    def debug_msg(self, info):
        font = pg.font.Font(None, 18)
        text_surf = font.render(info, True, pg.Color('white'))
        text_rect = text_surf.get_rect(right=WINW, top=0)
        pg.draw.rect(self.screen, pg.Color('black'), text_rect)
        self.screen.blit(text_surf, text_rect)

    def mainloop(self):
        while not self.done:
            self.clock.tick(FPS)
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.done = True
                    break
            self.screen.fill(pg.Color('white'))

            self.draw(self.screen)
            self.update()

            self.debug_msg(f'direction: {self.player.direction}')
            pg.display.flip()
        pg.quit()


if __name__ == '__main__':
    g = Game()
