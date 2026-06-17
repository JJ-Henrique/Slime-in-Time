import pygame
from settings import *


class Player:

    def __init__(self):

        # Initial position
        self.x = 400
        self.y = 300

        # Size
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE

        # Speed
        self.speed = PLAYER_SPEED

        # Animation
        self.frames = []

        for i in range(1, 4):

            image = pygame.image.load(
                f"assets/images/player/player_{i}.png"
            ).convert_alpha()

            image = pygame.transform.scale(image, (self.width, self.height))

            self.frames.append(image)

        self.current_frame = 0
        self.animation_speed = 0.09

    def animate(self):

        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def move(self):

        keys = pygame.key.get_pressed()

        moving = False

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            moving = True

        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            moving = True

        if keys[pygame.K_UP]:
            self.y -= self.speed
            moving = True

        if keys[pygame.K_DOWN]:
            self.y += self.speed
            moving = True

        if moving:
            self.animate()

        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))

        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))

    def draw(self, screen):

        screen.blit(self.frames[int(self.current_frame)], (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)
