import pygame
from random import *

class Music():
    def __init__(self):
        self.playlist = ["assets/afternoon_adventure.ogg", "assets/domestic_na_kanojo.ogg", "assets/final_countdown.ogg", "assets/damned.ogg", "assets/Yaosobi.ogg", "assets/Tainted-Love.ogg", "assets/Lovers_on_the_sun.ogg", "assets/chop_suey.ogg", "assets/you_spin_me_round.ogg"]
        self.music_init = pygame.mixer.music.load(self.playlist[randint(0, 8)])
        self.sound_bullet = pygame.mixer.Sound("assets/sound_weapon.wav")
        self.channel0 = pygame.mixer.Channel(0)

    def sound(self):
        self.channel0.play(self.sound_bullet)

    def play(self):
        self.musique_play = pygame.mixer.music.play(1, 0.0)

    def change_music(self):
        self.music_unload = pygame.mixer.music.unload()
        self.music_reload = pygame.mixer.music.load(self.playlist[randint(0, 8)])

    def playlist_end(self):
        self.music_stop = pygame.mixer.music.stop()
        self.music_unload = pygame.mixer.music.unload()
        self.music_reload = pygame.mixer.music.load("assets/game_over.ogg")
        del self.playlist[0: 8]


