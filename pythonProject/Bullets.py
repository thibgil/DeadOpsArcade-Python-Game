import pygame
from pygame.locals import *

class Bullets(pygame.sprite.Sprite):

    def __init__(self, player, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.velocity = 30
        self.image = pygame.image.load("assets/orb.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def shoot_left(self):
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.rect.x = self.rect.x - self.velocity
        else:
            self.kill()

    def shoot_right(self):
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.rect.x = self.rect.x + self.velocity
        else:
            self.kill()

    def shoot_front(self):
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.rect.y = self.rect.y + self.velocity
        else:
            self.kill()

    def shoot_back(self):
        if not self.game.check_collision(self, self.game.all_zombies) and not self.game.check_collision(self, self.game.all_obstacles):
            self.rect.y = self.rect.y - self.velocity
        else:
            self.kill()


