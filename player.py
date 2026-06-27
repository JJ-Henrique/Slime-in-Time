import re

import pygame
from settings import *
from utils import *


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
        self.knockback_x = 0

        self.max_health = 6
        self.health = self.max_health
        self.display_health = self.max_health
        self.invincible = False
        self.last_hit_time = 0

        # Animation
        self.frames = []

        for i in range(1, 7):

            image = pygame.image.load(
                f"assets/images/player/player_{i}.png"
            ).convert_alpha()

            image = pygame.transform.scale(image, (self.width, self.height))

            self.frames.append(image)

        self.current_frame = 0
        self.animation_speed = 0.12
        self.facing_right = True  # direcao
        self.direction_x = 0  # info para a movimentacao dos layers

    def move(self):

        keys = pygame.key.get_pressed()
        self.direction_x = 0
        moving = False

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.facing_right = False
            self.direction_x = -1
            moving = True

        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.facing_right = True
            self.direction_x = 1
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

        self.x += self.knockback_x
        self.knockback_x *= 0.8

    def draw(self, screen):

        current_image = self.frames[int(self.current_frame)]

        if self.facing_right:
            current_image = pygame.transform.flip(current_image, True, False)

        screen.blit(current_image, (self.x, self.y))

    def take_damage(self, amount):

        if self.invincible:
            return False  # ignora o dano
        self.health -= amount
        if self.health < 0:
            self.health = 0

        print(f"Player health: {self.health}")  # debug temporatio

        self.invincible = True
        self.last_hit_time = pygame.time.get_ticks()  # registra ultimo dano
        return True

    def update_invincibility(self):

        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_hit_time >= 1000:  # 1 second of invincibility
                self.invincible = False

    def update_display_health(self):
        self.display_health = lerp(
            self.display_health,
            self.health,
            HEALTH_LERP_SPEED
        )

    def update(self):
        self.update_invincibility()  # para o acoplamento no game.py no def_update
        self.update_display_health()

    def animate(self):
        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)
