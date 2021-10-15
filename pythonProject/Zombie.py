import pygame
from pygame.locals import *
from time import clock
from random import *

#feuille de sprites
sprite_sheet = pygame.image.load("assets/zombies.jpg")

#img de face
image_Init = sprite_sheet.subsurface((37, 0, 22, 31))
image_2 = sprite_sheet.subsurface((5, 1, 22, 30))
image_3 = sprite_sheet.subsurface((69, 1, 22, 30))

#img droite
image_4 = sprite_sheet.subsurface((6, 65, 20, 30))
image_5 = sprite_sheet.subsurface((38, 64, 20, 31))
image_6 = sprite_sheet.subsurface((70, 65, 20, 30))

#img gauche
image_7 = sprite_sheet.subsurface((5, 33, 20, 30))
image_8 = sprite_sheet.subsurface((37, 32, 20, 31))
image_9 = sprite_sheet.subsurface((69, 33, 20, 30))

#img dos
image_10 = sprite_sheet.subsurface((5, 97, 22, 30))
image_11 = sprite_sheet.subsurface((37, 96, 22, 31))
image_12 = sprite_sheet.subsurface((69, 97, 22, 30))

#list d'img
Face_list_zb = [image_Init, image_2, image_3]
Back_list_zb = [image_4, image_5, image_6]
LeftSide_list_zb = [image_7, image_8, image_9]
RightSide_list_zb = [image_10, image_11, image_12]

class Zombie(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.health = 150
        self.max_health = 150
        self.velocity = 2
        self.image = image_Init
        self.rect = self.image.get_rect()
        self.spawnsx = [517, 1283]
        self.rect.x = self.spawnsx[randint(0, 1)]
        self.rect.y = 564
        self.nextFrame = clock()
        self.frame = 0
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y

    def next_frame(self):
        if(self.nextFrame < clock()):
            self.frame = self.frame +1

    def anim_down_zb(self):
        self.image = Face_list_zb[self.frame % 3]

    def anim_up_zb(self):
        self.image = Back_list_zb[self.frame % 3]

    def anim_right_zb(self):
        self.image = RightSide_list_zb[self.frame % 3]

    def anim_left_zb(self):
        self.image = LeftSide_list_zb[self.frame % 3]

    def damage(self):
        self.health -= 50

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            if abs(self.game.player.rect.x - self.rect.x) > abs(self.game.player.rect.y - self.rect.y):
                if self.game.player.rect.x > self.rect.x:
                    self.move_right()
                else:
                    self.move_left()
            else:
                if self.game.player.rect.y > self.rect.y:
                    self.move_down()
                else:
                    self.move_up()

    def move_right(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.x += self.velocity
        if not self.game.check_collision(self, self.game.all_obstacles):
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
        if not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.x -= self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y

    def move_down(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.y += self.velocity
        if not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.y += self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y

    def move_up(self):
        self.save_position_x = self.rect.x
        self.save_position_y = self.rect.y
        self.rect.y -= self.velocity
        if not self.game.check_collision(self, self.game.all_obstacles):
            self.save_position_x = self.rect.x
            self.save_position_y = self.rect.y
            self.rect.y -= self.velocity
        else:
            self.rect.x = self.save_position_x
            self.rect.y = self.save_position_y












