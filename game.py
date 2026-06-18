import pygame
import time
import random

from settings import *
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):
        print("Game started")
        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/music.mp3")
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 5
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_2.png"
                    ).convert_alpha(),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 4
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_3.png"
                    ).convert_alpha(),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 3
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_4.png"
                    ).convert_alpha(),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 2
            },
            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        "assets/images/background/layer_5.png"
                    ).convert_alpha(),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
                "x": 0,
                "speed": 1
            },
        ]

        self.spawn_points = [
            (0, 0),
            (SCREEN_WIDTH - ENEMY_SIZE, 0),
            (0, SCREEN_HEIGHT - ENEMY_SIZE),
            (SCREEN_WIDTH - ENEMY_SIZE, SCREEN_HEIGHT - ENEMY_SIZE)
        ]

        self.player = Player()

        # CRIA PONTOS ALEATORIOS PARA SPAWN
        self.enemies = []
        self.spawn_enemy()

        self.running = True
        self.game_over = False
        self.victory = False
        self.game_started = False
        self.start_time = None
        self.last_spawn_time = 0
        self.score = 0
        self.last_trail_time = 0  # controla a quantidde de trails
        self.trails = []
        print("GAME STARTED")

        self.background = pygame.image.load(
            "assets/images/background/background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background, (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

    def spawn_enemy(self):  # spawn de inimigos em intervalos

        spawn_x, spawn_y = random.choice(self.spawn_points)
        new_enemy = Enemy(spawn_x, spawn_y)
        self.enemies.append(new_enemy)
        print(f"Total enemies: {len(self.enemies)}")

    def update(self):

        if not self.game_started:
            return

        if self.game_over or self.victory:
            return

        self.player.move()

        # controle total do paralaxx
        if self.player.direction_x == 1:
            for layer in self.layers:
                layer["x"] -= layer["speed"]

        elif self.player.direction_x == -1:
            for layer in self.layers:
                layer["x"] += layer["speed"]

        for layer in self.layers:
            if layer["x"] <= -SCREEN_WIDTH:
                layer["x"] = 0
            if layer["x"] >= SCREEN_WIDTH:
                layer["x"] = 0

        current_ticks = pygame.time.get_ticks()
        # ATUALIZACAO ONDE posso controlar o delay pelo settings
        if current_ticks - self.last_trail_time > TRAIL_SPAWN_DELAY:

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
                TRAIL_LIFETIME  # atualizacao onde posso controlar o tempo de vida do rastro pelo settings
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

        if current_time - self.last_spawn_time >= ENEMY_SPAWN_INTERVAL:
            self.spawn_enemy()
            self.last_spawn_time = current_time

        self.score = int(time.time() - self.start_time) * 100

    def check_collision(self):  # colisao entre player e inimigos
        for enemy in self.enemies:
            if self.player.get_rect().colliderect(enemy.get_rect()):
                self.game_over = True

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
        if not self.game_started:
            return
        if self.game_over or self.victory:
            return
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= WIN_TIME:
            self.victory = True

    def draw(self):
        self.screen.fill((50, 50, 50))

        for layer in reversed(self.layers):
            self.screen.blit(layer["image"], (layer["x"], 0))
            self.screen.blit(
                layer["image"], (layer["x"] - SCREEN_WIDTH, 0))

            self.screen.blit(
                layer["image"],
                (layer["x"], 0)
            )
            self.screen.blit(
                layer["image"],
                (layer["x"] + SCREEN_WIDTH, 0)
            )

        for trail in self.trails:
            # TAMANHO DAS PARTICULAS DO RASTRO
            # Aumente ou diminua o divisor para alterar a velocidade com que as particulas encolhem.
            # trail[2] // 2 = particulas maiores
            # trail[2] // 4 = tamanho medio
            # trail[2] // 6 = particulas menores
            # < MODIFICADO NO SETTING PARA MELHORAR EM PROJETOS FUTUROS
            radius = max(1, trail[2] // TRAIL_SIZE)

            pygame.draw.circle(
                self.screen,
                (91, 198, 184),
                (int(trail[0]), int(trail[1])),
                radius
            )

        if not self.game_started:
            text = self.font_medium.render("Press an Arrow Key to Start",
                                           True, (255, 255, 255))
            text_rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            )
            self.screen.blit(text, text_rect)

        elif not self.game_over and not self.victory:

            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

        elif self.game_over:

            text = self.font_big.render("GAME OVER", True, (255, 0, 0))
            text_rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            )
            self.screen.blit(text, text_rect)

        elif self.victory:
            text = self.font_big.render("YOU WIN!", True, (0, 255, 0))
            text_rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            )
            self.screen.blit(text, text_rect)

        if self.game_started and not self.game_over and not self.victory:  # TIMER#

            font = self.font_small

            remaining_time = max(
                0, WIN_TIME - int(time.time() - self.start_time))

            timer_text = font.render(
                f"Time Left: {remaining_time}", True, (255, 255, 255)
            )

            self.screen.blit(timer_text, (10, 10))

            score_text = font.render(
                f"Score: {self.score}", True, (255, 255, 255)
            )

            self.screen.blit(score_text, (10, 50))

            enemy_text = font.render(  # contadr de inimigos
                f"Enemies: {len(self.enemies)}", True, (255, 255, 255))
            self.screen.blit(enemy_text, (10, 90))

        fps_text = self.font_small.render(
            f"FPS: {int(self.clock.get_fps())}",
            True,
            (255, 255, 255)
        )

        self.screen.blit(fps_text, (10, 130))

        pygame.display.update()

    def reset_game(self):
        self.player = Player()
        self.enemies = []
        self.spawn_enemy()
        self.game_over = False
        self.victory = False
        self.game_started = False
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
                        if not self.game_started:

                            self.game_started = True

                            self.start_time = time.time()

                            print("GAME REALLY STARTED")

                    if event.key == pygame.K_r:

                        if self.game_over or self.victory:

                            self.reset_game()

            self.update()
            self.check_collision()
            self.check_win()
            self.draw()
            self.clock.tick(FPS)

    pygame.quit()
