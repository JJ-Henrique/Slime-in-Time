import pygame
from settings import *


class Enemy:

    def __init__(self, x, y):

        # Initial position
        self.x = x
        self.y = y

        # Size
        self.width = ENEMY_SIZE
        self.height = ENEMY_SIZE

        # Movement speed
        self.speed = ENEMY_SPEED

        # Sprite
        self.frames = []

        for i in range(1, 4):

            image = pygame.image.load(
                f"assets/images/enemy/enemy_{i}.png"
            ).convert_alpha()

            image = pygame.transform.scale(image, (self.width, self.height))

            self.frames.append(image)

        self.current_frame = 0
        self.animation_speed = 0.10

    def animate(self):

        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def chase(self, player):

        if self.x < player.x:
            self.x += self.speed

        if self.x > player.x:
            self.x -= self.speed

        if self.y < player.y:
            self.y += self.speed

        if self.y > player.y:
            self.y -= self.speed

    def draw(self, screen):
        # CORREÇÃO AQUI: Buscamos o frame correto dentro da lista antes de desenhar
        current_image = self.frames[int(self.current_frame)]

        screen.blit(current_image, (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)
