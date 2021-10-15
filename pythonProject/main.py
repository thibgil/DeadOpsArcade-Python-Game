import pygame
from pygame.locals import *
from Game import *
from Player import *
from Zombie import *
from Music import *

# Init + création de fenetre + chargement img
pygame.init()
screen = pygame.display.set_mode((1800, 900), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Projet Prepa "Dead Ops Arcade" ')

game = Game()

save_player_rect_x = game.player.rect.x
save_player_rect_y = game.player.rect.y

mainClock = pygame.time.Clock()

#image jeu
image_ammo = pygame.image.load("assets/ammo_img.png")
image_ammo = pygame.transform.scale(image_ammo, (60, 60))
image_heart = pygame.image.load("assets/health.png")
image_heart = pygame.transform.scale(image_heart, (60, 60))

#image pour le menu
image_menu = pygame.image.load("assets/deadops.png")
image_circle = pygame.image.load("assets/redcircle.png")

#image de mort
image_skull = pygame.image.load("assets/skull.png")
image_died = pygame.image.load("assets/dead_img.png")

# Création du mixer pour apport de sons
pygame.mixer.init()

# importation des spritesheet + decoupe des prites
sprite_sheet1 = pygame.image.load("assets/GameTiles.png")
sprite_sheet2 = pygame.image.load("assets/Houses2.png")
sprite_sheet3 = pygame.image.load("assets/GameTiles1.png")
sprite_sheet4 = pygame.image.load("assets/GameTiles8.png")

house_antenne = sprite_sheet2.subsurface((26, 12, 146, 126))
house_pokemon = sprite_sheet2.subsurface((191, 25, 115, 115))

arbre = sprite_sheet1.subsurface((58, 87, 25, 32))
arbre = pygame.transform.scale(arbre, (47, 94))

eau = pygame.image.load("assets/water.png")
eau = eau.subsurface((26, 12, 100, 100))
eau =  pygame.transform.scale(eau, (47, 47))

gris = pygame.image.load("assets/gris.jpg")
gris = pygame.transform.scale(gris, (47, 47))

grass = sprite_sheet4.subsurface((80, 320, 47, 47))
dirt = sprite_sheet4.subsurface((80, 112, 47, 47))

house_1 = sprite_sheet1.subsurface((227, 186, 47, 56))
house_1 = pygame.transform.scale(house_1, (94, 103))

house_2 = sprite_sheet1.subsurface((275, 186, 47, 56))
house_2 = pygame.transform.scale(house_2, (94, 103))

house_3 = sprite_sheet1.subsurface((322, 186, 47, 56))
house_3 = pygame.transform.scale(house_3, (94, 103))

house_4 = sprite_sheet1.subsurface((370, 186, 47, 56))
house_4 = pygame.transform.scale(house_4, (94, 103))

house_5 = sprite_sheet1.subsurface((417, 186, 47, 56))
house_5 = pygame.transform.scale(house_5, (94, 103))

house_6 = sprite_sheet1.subsurface((465, 186, 47, 56))
house_6 = pygame.transform.scale(house_6, (94, 103))

#image du vide
vide = pygame.image.load("assets/vide.png")
vide = pygame.transform.scale(vide, (94, 103))

#matrices tiles + obstacles
Map = [[grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
       [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
       [grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
       [grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
       [grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt],
       [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
       [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass],
       [grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass]]

obstacle_Map_1 = [[house_1, house_2, house_3, house_4, house_5, house_6, house_1, house_2, house_3, house_4, house_5, house_6, house_1, house_2, house_3, house_4, house_5, house_6, house_1, house_2],
                  [house_1, house_2, house_3, house_4, vide, house_6, house_1, house_2, house_3, house_4, house_5, house_6, house_1, house_2, vide, house_4, house_5, house_6, house_1, house_2],
                  [house_1, house_2, house_3, house_4, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, house_4, house_5, house_6, house_1, house_2],
                  [house_1, house_2, house_3, house_4, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, house_4, house_5, house_6, house_1, house_2]]

obstacle_Map_2 = [[arbre, arbre, arbre, arbre, arbre, arbre, arbre, arbre, vide, vide, arbre, arbre, arbre, arbre, arbre, arbre, arbre, arbre],
                  [arbre, arbre, arbre, arbre, arbre, arbre, arbre, arbre, vide, vide, arbre, arbre, arbre, arbre, arbre, arbre, arbre, arbre],
                  [arbre, arbre, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, arbre, arbre],
                  [vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide],
                  [vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide],
                  [vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide],
                  [arbre, arbre, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, arbre, arbre],
                  [arbre, arbre, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, vide, arbre, arbre]]

obstacle_Map_3 = [[eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, gris, gris, gris, gris, gris, gris, gris, gris, gris, gris],
                  [eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, gris, gris, gris, gris, gris, gris, gris, gris, gris, gris],
                  [eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, eau, gris, gris, gris, gris, gris, gris, gris, gris, gris, gris]]

#dimensions tiles
height = 47
width = 47

#dimensiosn obstacle maison 1
d = 94
h = 47*4

#génération des maps
# tiles
for i in range(0, 38):
    for j in range(0, 19):
        pos_x = i * height
        pos_y = j * width
        game.spawn_tile(Map[j][i], pos_x, pos_y)

# obstacles : maisons
for i in range(0, 19):
    for j in range(0, 4):
        pos1_x = i * d
        pos1_y = j * h
        if obstacle_Map_1[j][i] == vide:
            game.spawn_vide(obstacle_Map_1[j][i], pos1_x, pos1_y)
        else:
            game.spawn_obstacle(obstacle_Map_1[j][i], pos1_x, pos1_y)

# obstacles : arbres
for i in range(0, 18):
    for j in range(0, 8):
        pos1_x = i * width + 10*47
        pos1_y = j * height + 7*47
        if obstacle_Map_2[j][i] == vide:
            game.spawn_vide(obstacle_Map_2[j][i], pos1_x, pos1_y)
        else:
            game.spawn_obstacle(obstacle_Map_2[j][i], pos1_x, pos1_y)

# obstacles : eau
for i in range(0, 38):
    for j in range(0, 3):
        pos1_x = i * width
        pos1_y = j * height + 16*47
        game.spawn_obstacle(obstacle_Map_3[j][i], pos1_x, pos1_y)

#initialisation de l'etat de jeu
running = False

#creation d'un modele de bouton
def button(screen, position, text):
    font = pygame.font.SysFont("Chiller", 50)
    text_render = font.render(text, 1, (0, 255, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.rect(screen, (50, 50, 50), (x, y, w, h))
    return screen.blit(text_render, (x, y))

#menu avant jeu
while not running:
    game.all_tiles.draw(screen)
    game.all_obstacles.draw(screen)
    screen.blit(image_circle, (550, 100))
    screen.blit(image_menu, (655, 300))
    b1 = button(screen, (860, 600), "Jouer")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):
                running = True

    pygame.display.update()
    mainClock.tick(30)

#Paylist
musique = Music()
musique.play()

#boucle du jeu
while running and game.player.isAlive:

    #changement de musique
    if pygame.mixer.music.get_busy() == False :
        musique.change_music()
        musique.play()

    game.player.next_frame()

    #Affichage des sprites et images
    game.all_tiles.draw(screen)
    game.all_obstacles.draw(screen)
    game.all_players.draw(screen)

    # dessiner les balles
    game.player.all_left_bullets.draw(screen)
    game.player.all_right_bullets.draw(screen)
    game.player.all_front_bullets.draw(screen)
    game.player.all_back_bullets.draw(screen)

    #verif si le joueur est en vie
    game.player.alive()

    #joueur subit les degats de collision
    game.player.damaged()

    #temps entre 2 tirs
    game.player.cooldown()

    #affichage de la vie du joueur
    pygame.draw.rect(screen, (105, 48, 58), [1550, 850, game.player.max_health, 20])
    pygame.draw.rect(screen, (14, 186, 7), [1550, 850, game.player.health, 20])

    #affichage des munitions du joueur
    pygame.draw.rect(screen, (108, 107, 106), [1550, 770, game.player.max_ammo, 20])
    pygame.draw.rect(screen, (246, 247, 36), [1550, 770, game.player.ammo, 20])

    #symboles de munition et vie du joueur
    screen.blit(image_ammo, (1500, 750))
    screen.blit(image_heart, (1500, 820))

    #affichage vie du zombie
    #pygame.draw.rect(screen, (105, 48, 58), [game.zombie.rect.x, game.zombie.rect.y + 10, (game.zombie.max_health)*0.31415, 4])
    #pygame.draw.rect(screen, (14, 186, 7), [game.zombie.rect.x, game.zombie.rect.y + 10, (game.zombie.health)*0.31415, 4])

    # dessiner les zombies
    game.all_zombies.draw(screen)
    for zombie in game.all_zombies:
        zombie.move()
        zombie.next_frame()

    #orientation des balles
    for bullet in game.player.all_left_bullets:
        bullet.shoot_left()

    for bullet in game.player.all_right_bullets:
        bullet.shoot_right()

    for bullet in game.player.all_front_bullets:
        bullet.shoot_front()

    for bullet in game.player.all_back_bullets:
        bullet.shoot_back()

    #gestion des collisions detectees entre bullets et zombies et inversement
    game.collided_bullets_detection()
    game.collided_zombies_detection()

    #destruction des zombies et bullets qui ont été en collision
    for bullet in game.all_collided_bullets:
        bullet.kill()

    for zombie in game.all_collided_zombies:
        zombie.kill()

    else:
        # sauvegarde la position
        save_player_rect_x = game.player.rect.x
        save_player_rect_y = game.player.rect.y

        if game.pressed.get(pygame.K_RIGHT):
            game.player.move_right()
            game.player.anim_right()

        elif game.pressed.get(pygame.K_LEFT):
            game.player.move_left()
            game.player.anim_left()

        elif game.pressed.get(pygame.K_UP):
            game.player.move_up()
            game.player.anim_up()

        elif game.pressed.get(pygame.K_DOWN):
            game.player.move_down()
            game.player.anim_down()

    #Rafraichissement du jeu
    pygame.display.flip()

    #vérif : touche enfoncée ou levée
    for event in pygame.event.get():

        if game.pressed.get(pygame.K_SPACE):
            if game.player.image in LeftSide_list:
                game.player.shoot_left_bullet()
            elif game.player.image in RightSide_list:
                game.player.shoot_right_bullet()
            elif game.player.image in Face_list:
                game.player.shoot_front_bullet()
            elif game.player.image in Back_list:
                game.player.shoot_back_bullet()
            musique.sound()

        if game.pressed.get(pygame.K_1):
            game.spawn_zombie()

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == QUIT:
            pygame.quit()

    mainClock.tick(30)

#menu quand le joueur est mort
while running and not game.player.isAlive:
    game.all_tiles.draw(screen)
    game.all_obstacles.draw(screen)
    game.all_players.draw(screen)

    pygame.Surface.fill(screen, (0, 0, 0, 50))

    if musique.playlist == ["assets/afternoon_adventure.ogg", "assets/domestic_na_kanojo.ogg", "assets/final_countdown.ogg", "assets/damned.ogg", "assets/Yaosobi.ogg", "assets/Tainted-Love.ogg", "assets/Lovers_on_the_sun.ogg", "assets/chop_suey.ogg", "assets/you_spin_me_round.ogg"]:
        musique.playlist_end()
        pygame.mixer.music.play(-1)

    screen.blit(image_died, (300, 0))
    screen.blit(image_skull, (100, 300))
    screen.blit(image_skull, (1400, 300))
    b = button(screen, (1200, 800), "Quitter le jeu")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()

    pygame.display.update()
    mainClock.tick(30)