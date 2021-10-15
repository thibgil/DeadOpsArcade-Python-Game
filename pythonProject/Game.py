import pygame
from Player import Player
from Zombie import Zombie
from Obstacle import Obstacle
from Tile import Tile

class Game:

    def __init__(self):
        self.player = Player(self)
        self.zombie = Zombie(self)
        self.all_players = pygame.sprite.Group(self.player)
        self.all_obstacles = pygame.sprite.Group()
        self.all_vides = pygame.sprite.Group()
        self.all_tiles = pygame.sprite.Group()
        self.all_zombies = pygame.sprite.Group()
        self.all_collided_zombies = pygame.sprite.Group()
        self.all_collided_bullets = pygame.sprite.Group()
        self.pressed = {}

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_zombie(self):
        zb = Zombie(self)
        self.all_zombies.add(zb)

    def collided_zombies_detection(self):
        for zombie in self.all_zombies:
            if self.check_collision(zombie, self.player.all_left_bullets) or self.check_collision(zombie, self.player.all_right_bullets) or self.check_collision(zombie, self.player.all_front_bullets) or self.check_collision(zombie, self.player.all_back_bullets):
                self.all_collided_zombies.add(zombie)

    def collided_bullets_detection(self):
        for bullet in self.player.all_left_bullets:
            if self.check_collision(bullet, self.all_zombies):
                self.all_collided_bullets.add(bullet)
        for bullet in self.player.all_right_bullets:
            if self.check_collision(bullet, self.all_zombies):
                self.all_collided_bullets.add(bullet)
        for bullet in self.player.all_front_bullets:
            if self.check_collision(bullet, self.all_zombies):
                self.all_collided_bullets.add(bullet)
        for bullet in self.player.all_back_bullets:
            if self.check_collision(bullet, self.all_zombies):
                self.all_collided_bullets.add(bullet)

    def spawn_obstacle(self, image, x, y):
        obs = Obstacle(image, x, y)
        self.all_obstacles.add(obs)

    def spawn_vide(self, image, x, y):
        vide = Obstacle(image, x, y)
        self.all_vides.add(vide)

    def spawn_tile(self, image, x, y):
        tile = Tile(image, x, y)
        self.all_tiles.add(tile)
