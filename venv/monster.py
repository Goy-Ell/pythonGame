import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy/mummy1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000+random.randint(0,300)
        self.rect.y = 540
        self.velocity = (random.randint(1,20))/20

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x=1000+random.randint(0,300)
            self.health=self.max_health

    def update_health_bar(self, surface):
        # couleur bar de vie
        bar_color = (111, 210, 46)
        # arriere plan jauge
        back_bar_color = (60, 63, 60)
        # position arriere plan
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        # position bar de vie
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # dessin bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
