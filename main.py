import pygame
from game import Game

pygame.init()

# generer  la fentre de notre jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer le background
background = pygame.image.load('assets/bg.jpg')
# charger joueur
game = Game()
running = True

# boucle tant que cette condition est vrai
while running:
    # appliquer l'arreier plan
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)


    game.player.all_projectiles.draw(screen)

    game.all_monsters.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
        game.player.move_left()

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():  # pour chaque eveneement effectué dans le jeux
        if event.type == pygame.QUIT:  # si le type d'event est un quit
            running = False
            pygame.quit()
            print("fermeture du jeux")

        # detecter lache bouton
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
