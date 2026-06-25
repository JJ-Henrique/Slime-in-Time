import pygame
import random
from settings import *
from game_state import GameState
import time


# layers/backgrounds
def draw_background(game):
    shake_x = 0
    shake_y = 0
    if game.shake_duration > 0:
        shake_x = random.randint(
            -game.shake_intensity,
            game.shake_intensity
        )

        shake_y = random.randint(
            -game.shake_intensity,
            game.shake_intensity
        )

    for layer in reversed(game.layers):
        game.screen.blit(layer["image"], (layer["x"] + shake_x, shake_y))
        game.screen.blit(
            layer["image"], (layer["x"] - SCREEN_WIDTH, 0))

        game.screen.blit(
            layer["image"],
            (layer["x"] + shake_x, shake_y)
        )
        game.screen.blit(
            layer["image"],
            (layer["x"] + SCREEN_WIDTH + shake_x, shake_y)
        )

# desenha personagens e inimigos alem de controlar o state


def draw_game_state(game):
    if game.state == GameState.MENU:  # controla o draw de player e enemies
        text = game.font_medium.render(
            "Press an Arrow Key to Start", True, WHITE)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        game.screen.blit(text, text_rect)

    elif game.state == GameState.PLAYING:
        game.player.draw(game.screen)
        for enemy in game.enemies:
            enemy.draw(game.screen)

    elif game.state == GameState.GAME_OVER:
        text = game.font_big.render("GAME OVER", True, RED)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        game.screen.blit(text, text_rect)

    elif game.state == GameState.VICTORY:
        text = game.font_big.render("YOU WIN!", True, GREEN)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        game.screen.blit(text, text_rect)

# desenha a hud


def draw_hud(game):
    if game.state == GameState.PLAYING:  # TIMER#
        font = game.font_small

        remaining_time = max(
            0, WIN_TIME - int(time.time() - game.start_time))
        enemy_text = font.render(  # contadr de inimigos
            f"Enemies: {len(game.enemies)}", True, WHITE)
        game.screen.blit(enemy_text, (10, 90))

        fps_text = game.font_small.render(
            f"FPS: {int(game.clock.get_fps())}", True, WHITE)
        game.screen.blit(fps_text, (1150, 700))

        timer_text = font.render(
            f"Time Left: {remaining_time}", True, WHITE)
        game.screen.blit(timer_text, (10, 10))

        score_text = font.render(
            f"Score: {game.score}", True, WHITE)
        game.screen.blit(score_text, (10, 50))

        health_text = font.render(  # vida
            f"Health: {game.player.health}/{game.player.max_health}", True, WHITE)
        game.screen.blit(health_text, (10, 130))

        health_percent = (
            game.player.health / game.player.max_health
        )

       # a partir daqui sera feita a implementacao da barra de vida fill_width = HEALTH_BAR_WIDTH * health_percent

# desenha trails


def draw_trails(game):

    for trail in game.trails:

        radius = max(1, trail[2] // TRAIL_SIZE)

        pygame.draw.circle(
            game.screen,
            (91, 198, 184),
            (int(trail[0]), int(trail[1])),
            radius
        )


# controla todo o draw


def draw(game):
    game.screen.fill((50, 50, 50))
    draw_background(game)
    draw_trails(game)
    draw_game_state(game)
    draw_hud(game)

    pygame.display.update()
