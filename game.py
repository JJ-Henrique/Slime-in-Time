import pygame
import time
import random
import settings

import render
from player import Player
from enemy import Enemy
import game_state


class Game:

    def __init__(self):
        print("Game started")
        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/music.mp3")
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

        pygame.display.set_caption("Survive The Enemy")

        self.clock = pygame.time.Clock()

        # aplica fonte a tdas as classes
        self.font_small = pygame.font.Font(
            "assets/fonts/PressStart2P.ttf", 18)
        self.font_medium = pygame.font.Font(
            "assets/fonts/PressStart2P.ttf", 40)

        self.font_big = pygame.font.Font(
            "assets/fonts/PressStart2P.ttf", 100)

        # parallax layers
        self.layers = [
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_1.png"
                    ).convert_alpha(),
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 5
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_2.png"
                    ).convert_alpha(),
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 4
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_3.png"
                    ).convert_alpha(),
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 3
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_4.png"
                    ).convert_alpha(),
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 2
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_5.png"
                    ).convert_alpha(),
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 1
            },
        ]

        self.spawn_points = [
            (0, 0),
            (settings.SCREEN_WIDTH - settings.ENEMY_SIZE, 0),
            (0, settings.SCREEN_HEIGHT - settings.ENEMY_SIZE),
            (settings.SCREEN_WIDTH - settings.ENEMY_SIZE,
             settings.SCREEN_HEIGHT - settings.ENEMY_SIZE)
        ]

        self.player = Player()

        # CRIA PONTOS ALEATORIOS PARA SPAWN
        self.enemies = []
        self.spawn_enemy()

        self.running = True
        self.state = game_state.GameState.MENU
        print(self.state)
        self.start_time = None
        self.last_spawn_time = 0
        self.score = 0
        self.last_trail_time = 0  # controla a quantidde de trails
        self.trails = []
        self.shake_duration = 0
        self.shake_intensity = 0
        print("GAME STARTED")

        self.background = pygame.image.load(
            "assets/images/background/background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

    def spawn_enemy(self):  # spawn de inimigos em intervalos

        spawn_x, spawn_y = random.choice(self.spawn_points)
        new_enemy = Enemy(spawn_x, spawn_y)
        self.enemies.append(new_enemy)
        print(f"Total enemies: {len(self.enemies)}")

    def update(self):
        if self.state != game_state.GameState.PLAYING:
            return

        self.player.move()
        self.player.update()  # acoplamento de duas classes

        # controle total do paralaxx
        if self.player.direction_x == 1:
            for layer in self.layers:
                layer["x"] -= layer["speed"]

        elif self.player.direction_x == -1:
            for layer in self.layers:
                layer["x"] += layer["speed"]

        for layer in self.layers:
            if layer["x"] <= -settings.SCREEN_WIDTH:
                layer["x"] = 0
            if layer["x"] >= settings.SCREEN_WIDTH:
                layer["x"] = 0

        current_ticks = pygame.time.get_ticks()
        # ATUALIZACAO ONDE posso controlar o delay pelo settings
        if current_ticks - self.last_trail_time > settings.TRAIL_SPAWN_DELAY:

            if self.player.facing_right:
                trail_x = self.player.x
            else:
                trail_x = self.player.x + self.player.width

            trail_y = (
                self.player.y
                + self.player.height // 2
                + random.randint(-3, 3)
            )

            self.trails.append([
                trail_x,
                trail_y,
                # atualizacao onde posso controlar o tempo de vida do rastro pelo settings
                settings.TRAIL_LIFETIME
            ])

            self.last_trail_time = current_ticks

            for trail in self.trails:
                trail[2] -= 1
                self.trails = [
                    trail for trail in self.trails if trail[2] > 0
                ]

        for enemy in self.enemies:
            enemy.chase(self.player)
            enemy.animate()

        self.separate_enemies()

        current_time = time.time() - self.start_time

        if current_time - self.last_spawn_time >= settings.ENEMY_SPAWN_INTERVAL:
            self.spawn_enemy()
            self.last_spawn_time = current_time

        self.score = int(time.time() - self.start_time) * 100

        if self.shake_duration > 0:
            self.shake_duration -= 1

    def check_collision(self):  # colisao entre player e inimigos
        if self.state != game_state.GameState.PLAYING:
            return

        for enemy in self.enemies:
            if self.player.get_rect().colliderect(enemy.get_rect()):
                if self.player.take_damage(1):
                    if self.player.x < enemy.x:
                        self.player.knockback_x = -settings.KNOCKBACK_FORCE
                        enemy.x += settings.KNOCKBACK_FORCE
                    else:
                        self.player.knockback_x = settings.KNOCKBACK_FORCE
                        enemy.x -= settings.KNOCKBACK_FORCE
                    self.shake_duration = 8  # controle do camera shake
                    self.shake_intensity = 2
                    pass

    def separate_enemies(self):
        for enemy in self.enemies:
            for other_enemy in self.enemies:
                if enemy == other_enemy:
                    continue

                if enemy.get_rect().colliderect(other_enemy.get_rect()):
                    if enemy.x < other_enemy.x:
                        enemy.x -= 2
                    else:
                        enemy.x += 2

                    if enemy.y > other_enemy.y:
                        enemy.y -= 2
                    else:
                        enemy.y += 2

    def check_win(self):
        if self.state != game_state.GameState.PLAYING:
            return

        elapsed_time = time.time() - self.start_time
        if elapsed_time >= settings.WIN_TIME:
            self.state = game_state.GameState.VICTORY
            print(self.state)

    def check_game_over(self):
        if self.state != game_state.GameState.PLAYING:
            return

        if self.player.health <= 0:
            self.state = game_state.GameState.GAME_OVER
            print(self.state)

    def draw(self):
        render.draw(self)

    def reset_game(self):
        self.player = Player()
        self.enemies = []
        self.spawn_enemy()
        self.state = game_state.GameState.MENU
        print(self.state)
        self.start_time = None
        self.score = 0
        self.last_spawn_time = 0

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key in (
                        pygame.K_LEFT,
                        pygame.K_RIGHT,
                        pygame.K_UP,
                        pygame.K_DOWN,
                    ):
                        if self.state == game_state.GameState.MENU:
                            self.state = game_state.GameState.PLAYING
                            print(self.state)

                            self.start_time = time.time()

                            print("GAME REALLY STARTED")

                    if event.key == pygame.K_r:

                        if self.state in (
                            game_state.GameState.GAME_OVER,
                            game_state.GameState.VICTORY
                        ):
                            self.reset_game()

            self.update()
            self.check_collision()
            self.check_game_over()
            self.check_win()
            self.draw()
            self.clock.tick(settings.FPS)

    pygame.quit()
