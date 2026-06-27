from enum import Enum
from settings import *
import pygame
from utils import *
import math
from enemy import *
from player import *


class ShieldState(Enum):
    INACTIVE = 0
    EXPANDING = 1
    ACTIVE = 2
    SHRINKING = 3
    COOLDOWN = 4


class Shield:

    def __init__(self):  # sschield states
        self.state = ShieldState.INACTIVE
        self.radius = 0
        self.display_radius = 0
        self.active_start_time = 0
        self.pulse_offset = 0

    def activate(self):

        if self.state != ShieldState.INACTIVE:
            return
        self.state = ShieldState.EXPANDING
        self.radius = SHIELD_MAX_RADIUS

    def is_active(self):  # controla a invencibilidade
        return self.state == ShieldState.ACTIVE

    def collides_with(self, enemy, player):  # controla colisao do shield
        enemy_center_x = enemy.x + (enemy.width // 2)
        enemy_center_y = enemy.y + (enemy.height // 2)
        center_x = player.x + (player.width // 2)
        center_y = player.y + (player.height // 2)
        delta_x = enemy_center_x - center_x
        delta_y = enemy_center_y - center_y
        distance = math.hypot(delta_x, delta_y)

        if distance <= self.display_radius:
            return True

        return False

    def update_display_radius(self):
        self.display_radius = lerp(
            self.display_radius,
            self.radius,
            SHIELD_LERP_SPEED
        )

    def update_state(self):
        # EXPANDING

        if self.state == ShieldState.EXPANDING:
            if abs(self.radius - self.display_radius) < SHIELD_RADIUS_TOLERANCE:
                self.state = ShieldState.ACTIVE
                self.active_start_time = pygame.time.get_ticks()
                print(self.state)
                print(self.active_start_time)

        # ACTIVE

        if self.state == ShieldState.ACTIVE:
            tempo_passado = pygame.time.get_ticks() - self.active_start_time
            if tempo_passado > SHIELD_ACTIVE_DURATION:
                self.state = ShieldState.SHRINKING
                self.radius = 0

        if self.state == ShieldState.SHRINKING:
            if abs(self.radius - self.display_radius) < SHIELD_RADIUS_TOLERANCE:
                self.state = ShieldState.INACTIVE

    def update_pulse(self):
        if self.state != ShieldState.ACTIVE:
            return

        current_time = pygame.time.get_ticks()
        pulse = math.sin(current_time / 500) * 3
        self.pulse_offset = pulse

    def update(self):
        self.update_display_radius()
        self.update_state()
        self.update_pulse()

    def draw(self, screen, player):

        if self.state == ShieldState.INACTIVE:
            return

        center_x = player.x + (player.width // 2)
        center_y = player.y + (player.height // 2)

        diameter = (self.display_radius + SHIELD_GLOW_SIZE) * 2

        shield_surface = pygame.Surface(
            (diameter, diameter),
            pygame.SRCALPHA
        )

        center = (diameter // 2, diameter // 2)
        render_radius = int(self.display_radius + self.pulse_offset)

        pygame.draw.circle(  # glow da borda
            shield_surface,
            SHIELD_GLOW_COLOR,
            center,
            render_radius + SHIELD_GLOW_SIZE, 6
        )
        pygame.draw.circle(  # preenchimento
            shield_surface,
            SHIELD_FILL_COLOR,
            center,
            render_radius - 3, 0
        )
        pygame.draw.circle(  # borda principal
            shield_surface,
            SHIELD_BORDER_COLOR,
            center,
            render_radius, 3
        )

        screen.blit(shield_surface, ((center_x - diameter // 2,
                                      center_y - diameter // 2)))
