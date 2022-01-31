import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, bounds, size):
        pg.init()
        super().__init__()
        self.x, self.y = bounds
        self.size = size
        self.display_surf = pg.display.get_surface()
        self.direction = pg.math.Vector2()
        self.speed = 6
        self.move = {  # spritesheet dictionary
            'down': pg.image.load(
                        './gfx/ACharDown.png'
                    ).convert_alpha(self.display_surf),
            'up': pg.image.load(
                        './gfx/ACharUp.png'
                    ).convert_alpha(self.display_surf),
            'right': pg.image.load(
                        './gfx/ACharRight.png'
                    ).convert_alpha(self.display_surf),
            'left': pg.image.load(
                        './gfx/ACharLeft.png'
                    ).convert_alpha(self.display_surf)
        }
        self.raw_image = self.move['down']  # default image
        self.img_ls = []  # a list contains pg.Rect data
        self.index = 0  # default index of each individual image in the img_ls
        img_width = self.raw_image.get_width()//2
        img_height = self.raw_image.get_height()//2
        for j in range(0, self.raw_image.get_height(), img_height):
            for i in range(0, self.raw_image.get_width(), img_width):
                # using a nested for loop with specific step
                # to iterate through the entire spritesheet and then
                # add pg.Rec spec to the img_ls has defined above
                self.img_ls.append(pg.Rect(i, j, img_width, img_height))

        self.image = self.raw_image.subsurface(self.img_ls[self.index])
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(
            x=self.x, y=self.y
        )

    def update(self):
        self.keyin()
        self.movement()

    def animated(self):
        self.image = self.raw_image.subsurface(
            self.img_ls[self.index]
        )
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        pg.time.delay(200)  # slow down the player's movement
        self.index += 1
        if self.index >= len(self.img_ls):
            self.index = 0

    def keyin(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            #  create the animation for the player moving right the screen
            self.raw_image = self.move['right']
            self.animated()
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.raw_image = self.move['left']
            self.animated()
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.raw_image = self.move['down']
            self.animated()
        elif keys[pg.K_UP]:
            self.direction.y = -1
            self.raw_image = self.move['up']
            self.animated()
        else:
            self.direction.y = 0
            self.direction.x = 0
            self.image = self.raw_image.subsurface(
                self.img_ls[self.index]
            )
            self.image = pg.transform.scale(self.image, (self.size, self.size))
            pg.time.delay(200)  # slow down the player's movement
            self.index = 0  # static status

    def movement(self):
        self.rect.center += self.direction*self.speed
