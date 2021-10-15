import pygame
from pygame.locals import *
from time import clock
from Bullets import *

sprite_sheet = pygame.image.load("assets/GameSprites8.png")
imageInit = sprite_sheet.subsurface((0, 8, 31, 37))

# Image de face
image1 = imageInit
image2 = sprite_sheet.subsurface((32, 10, 31, 37))
image3 = sprite_sheet.subsurface((64, 8, 31, 37))
image4 = sprite_sheet.subsurface((96, 10, 31, 37))

# Image de dos
image5 = sprite_sheet.subsurface((0, 152, 31, 37))
image6 = sprite_sheet.subsurface((32, 152, 31, 37))
image7 = sprite_sheet.subsurface((64, 152, 31, 37))
image8 = sprite_sheet.subsurface((96, 152, 31, 37))

# Image de droite
image9 = sprite_sheet.subsurface((2, 56, 27, 37))
image10 = sprite_sheet.subsurface((34, 56, 27, 37))
image11 = sprite_sheet.subsurface((66, 56, 27, 37))
image12 = sprite_sheet.subsurface((98, 56, 27, 37))

# Image de gauche
image13 = sprite_sheet.subsurface((2, 104, 27, 37))
image14 = sprite_sheet.subsurface((34, 104, 27, 37))
image15 = sprite_sheet.subsurface((66, 104, 27, 37))
image16 = sprite_sheet.subsurface((98, 104, 27, 37))

# Liste des images en fonction des directions
Face_list = [image1, image2, image3, image4]
Back_list = [image5, image6, image7, image8]
LeftSide_list = [image9, image10, image11, image12]
RightSide_list = [image13, image14, image15, image16]

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.velocity = 5
        self.image = imageInit
        self.rect = self.image.get_rect()
        self.rect.x = 893
        self.rect.y = 611
        self.health = 200
        self.isAlive = True
        self.max_health = 200
        self.ammo = 100
        self.max_ammo = 200
        self.cool_down = 0
        self.nextFrame = clock()
        self.frame = 0
        self.all_bullets = pygame.sprite.Group()
        self.all_left_bullets = pygame.sprite.Group()
        self.all_right_bullets = pygame.sprite.Group()
        self.all_front_bullets = pygame.sprite.Group()
        self.all_back_bullets = pygame.sprite.Group()
        self.save_position_x = 0
        self.save_position_y = 0

    def next_frame(self):
        if(self.nextFrame < clock()):
            self.frame = self.frame +1

    def move_right(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.x += self.velocity
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.x += self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y

    def move_left(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.x -= self.velocity
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.x -= self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y

    def move_up(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.y -= self.velocity
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.y -= self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y

    def move_down(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.y += self.velocity
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.y += self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y

    def anim_down(self):
        self.image = Face_list[self.frame % 4]

    def anim_up(self):
        self.image = Back_list[self.frame % 4]

    def anim_right(self):
        self.image = RightSide_list[self.frame % 4]

    def anim_left(self):
        self.image = LeftSide_list[self.frame % 4]

    def cooldown(self):
        if self.cool_down >= 10:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def shoot_left_bullet(self):
        if self.ammo > 0 and self.cool_down == 0:
            self.all_left_bullets.add(Bullets(self, self.game))
            self.ammo -= 1
            self.cool_down = 1

    def shoot_right_bullet(self):
        if self.ammo > 0 and self.cool_down == 0:
            self.all_right_bullets.add(Bullets(self, self.game))
            self.ammo -= 1
            self.cool_down = 1

    def shoot_front_bullet(self):
        if self.ammo > 0 and self.cool_down == 0:
            self.all_front_bullets.add(Bullets(self, self.game))
            self.ammo -= 1
            self.cool_down = 1

    def shoot_back_bullet(self):
        if self.ammo > 0 and self.cool_down == 0:
            self.all_back_bullets.add(Bullets(self, self.game))
            self.ammo -= 1
            self.cool_down = 1

    def alive(self):
        if self.health <= 0:
            self.isAlive = False

    def damaged(self):
        if self.game.check_collision(self, self.game.all_zombies):
            self.health -= 5