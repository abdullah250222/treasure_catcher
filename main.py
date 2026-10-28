import pygame
import sys
import random
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, WHITE, BLUE, GOLD, RED, GREEN, CYAN, PURPLE, ORANGE, GRAY, ICE_BLUE
from player import Player
from item import Item

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Treasure Catcher")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 60)

player = Player()
items = []

spawn_timer = 0
spawn_delay = 30

score = 0
lives = 3
missed_coins = 0
game_over = False
game_started = False
difficulty = "medium"

next_powerup_score = 100
powerup_msg_timer = 0

event_timer = random.randint(300, 500)
active_event = None
event_duration = 0

life_spawn_timer = random.randint(600, 1200)
magnet_timer = 0

has_shield = False
bonus_msg_timer = 0

fever_timer = 0
next_fever_score = 250

smoke_timer = 0
slowmo_timer = 0

def reset_game():
    global player, items, spawn_timer, score, lives, missed_coins, game_over, game_started
    global next_powerup_score, powerup_msg_timer, event_timer
    global active_event, event_duration, life_spawn_timer, magnet_timer
    global has_shield, bonus_msg_timer, fever_timer, next_fever_score
    global smoke_timer, slowmo_timer

    player = Player()
    items = []
    spawn_timer = 0
    score = 0
    lives = 3
    missed_coins = 0
    game_over = False
    game_started = False
    next_powerup_score = 100
    powerup_msg_timer = 0
    event_timer = random.randint(300, 500)
    active_event = None
    event_duration = 0
    life_spawn_timer = random.randint(600, 1200)
    magnet_timer = 0
    has_shield = False
    bonus_msg_timer = 0
    fever_timer = 0
    next_fever_score = 250
    smoke_timer = 0
    slowmo_timer = 0

def draw_start_screen():
    screen.fill(BLACK)
    
    title_text = title_font.render("TREASURE CATCHER", True, GOLD)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 210, 150))

    sub_text = font.render("Select Difficulty to Start:", True, WHITE)
    screen.blit(sub_text, (SCREEN_WIDTH // 2 - 140, 260))

    easy_text = font.render("Press 1 : EASY", True, GREEN)
    med_text = font.render("Press 2 : MEDIUM", True, CYAN)
    hard_text = font.render("Press 3 : HARD", True, RED)

    screen.blit(easy_text, (SCREEN_WIDTH // 2 - 100, 330))
    screen.blit(med_text, (SCREEN_WIDTH // 2 - 100, 380))
    screen.blit(hard_text, (SCREEN_WIDTH // 2 - 100, 430))

def draw_hud():
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (SCREEN_WIDTH - 120, 10))

    if difficulty == "hard":
        missed_text = font.render(f"Missed: {missed_coins}/5", True, RED if missed_coins >= 3 else WHITE)
        screen.blit(missed_text, (10, 45))

    if powerup_msg_timer > 0:
        p_text = font.render("POWER UP: BIG BASKET!", True, GOLD)
        screen.blit(p_text, (SCREEN_WIDTH // 2 - 140, 10))

    if magnet_timer > 0:
        m_text = font.render("MAGNET ACTIVE!", True, CYAN)
        screen.blit(m_text, (10, 80))

    if slowmo_timer > 0:
        sl_text = font.render("SLOW-MO ACTIVE!", True, ICE_BLUE)
        screen.blit(sl_text, (10, 115))

    if has_shield:
        s_text = font.render("SHIELD ACTIVE!", True, PURPLE)
        screen.blit(s_text, (10, 150))

    if bonus_msg_timer > 0:
        b_text = font.render("SUPER BONUS +50!", True, GOLD)
        screen.blit(b_text, (SCREEN_WIDTH // 2 - 110, 80))

    if fever_timer > 0:
        f_text = font.render("FEVER MODE: COIN RAIN!", True, GOLD)
        screen.blit(f_text, (SCREEN_WIDTH // 2 - 150, 45))
    elif active_event == "fast":
        e_text = font.render("WARNING: FAST FALL!", True, RED)
        screen.blit(e_text, (SCREEN_WIDTH // 2 - 130, 45))
    elif active_event == "bombs":
        e_text = font.render("WARNING: BOMB STORM!", True, RED)
        screen.blit(e_text, (SCREEN_WIDTH // 2 - 140, 45))

def run_game():
    global spawn_timer, score, lives, missed_coins, game_over, game_started, difficulty
    global next_powerup_score, powerup_msg_timer, event_timer, active_event, event_duration
    global spawn_delay, life_spawn_timer, magnet_timer, has_shield, bonus_msg_timer, fever_timer, next_fever_score
    global smoke_timer, slowmo_timer

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not game_started:
                    if event.key == pygame.K_1:
                        difficulty = "easy"
                        game_started = True
                    elif event.key == pygame.K_2:
                        difficulty = "medium"
                        game_started = True
                    elif event.key == pygame.K_3:
                        difficulty = "hard"
                        game_started = True
                elif game_over and event.key == pygame.K_r:
                    reset_game()

        if game_started and not game_over:
            keys = pygame.key.get_pressed()
            player.move(keys)

            if powerup_msg_timer > 0:
                powerup_msg_timer -= 1

            if bonus_msg_timer > 0:
                bonus_msg_timer -= 1

            if magnet_timer > 0:
                magnet_timer -= 1

            if slowmo_timer > 0:
                slowmo_timer -= 1

            if smoke_timer > 0:
                smoke_timer -= 1

            if fever_timer > 0:
                fever_timer -= 1

            if fever_timer <= 0:
                event_timer -= 1
                if event_timer <= 0 and active_event is None:
                    active_event = random.choice(["fast", "bombs"])
                    event_duration = 240
                    event_timer = random.randint(350, 600)

                if active_event:
                    event_duration -= 1
                    if event_duration <= 0:
                        active_event = None

            if life_spawn_timer > 0:
                life_spawn_timer -= 1

            if difficulty == "easy":
                difficulty_speed = 1.0
                spawn_delay_val = 35
            elif difficulty == "medium":
                difficulty_speed = 1.0 + (score / 600.0)
                spawn_delay_val = 30
            else:
                difficulty_speed = 1.2 + (score / 300.0)
                spawn_delay_val = 25

            current_delay = max(8, int((10 if active_event == "bombs" else spawn_delay_val) / difficulty_speed))

            spawn_timer += 1
            if spawn_timer >= current_delay:
                speed_mult = (1.8 if active_event == "fast" else 1.0) * difficulty_speed
                if slowmo_timer > 0:
                    speed_mult *= 0.4
                
                has_green_on_screen = any(item.type == "life" for item in items)
                has_cyan_on_screen = any(item.type == "magnet" for item in items)
                has_purple_on_screen = any(item.type == "shield" for item in items)
                
                forced_type = None

                if fever_timer > 0:
                    forced_type = "coin"
                else:
                    if lives < 3 and not has_green_on_screen:
                        life_chance = 0.08 if difficulty == "easy" else 0.04
                        if life_spawn_timer <= 0 or random.random() < life_chance:
                            forced_type = "life"
                            life_spawn_timer = random.randint(600, 1200)

                    if forced_type is None and not has_cyan_on_screen and random.random() < 0.05:
                        forced_type = "magnet"

                    if forced_type is None and not has_purple_on_screen and not has_shield and random.random() < 0.04:
                        forced_type = "shield"

                    if forced_type is None and random.random() < 0.04:
                        forced_type = "slowmo"

                    if forced_type is None and random.random() < 0.05:
                        forced_type = "zigzag"

                    if forced_type is None and random.random() < 0.04:
                        forced_type = "gem"

                    if forced_type is None and random.random() < 0.06:
                        forced_type = "smoke"

                    if difficulty == "easy":
                        bomb_chance = 0.2
                    elif difficulty == "medium":
                        bomb_chance = 0.35
                    else:
                        bomb_chance = 0.5 + min(0.3, score / 1000.0)

                    if active_event == "bombs":
                        bomb_chance = 0.85

                    if forced_type is None and random.random() < bomb_chance:
                        forced_type = "bomb"

                items.append(Item(speed_multiplier=speed_mult, forced_type=forced_type))
                spawn_timer = 0

            for item in items[:]:
                if magnet_timer > 0 and (item.type == "coin" or item.type == "gem" or item.type == "zigzag"):
                    if item.x < player.rect.centerx:
                        item.x += 6
                    elif item.x > player.rect.centerx:
                        item.x -= 6
                    item.rect.x = item.x

                item.update()

                if player.rect.colliderect(item.rect):
                    if item.type == "coin":
                        score += 10
                    elif item.type == "zigzag":
                        score += 30
                    elif item.type == "gem":
                        score += 50
                        bonus_msg_timer = 120
                    elif item.type == "smoke":
                        smoke_timer = 180
                    elif item.type == "slowmo":
                        slowmo_timer = 300
                    elif item.type == "bomb":
                        if has_shield:
                            has_shield = False
                        else:
                            lives -= 1
                            if lives <= 0:
                                game_over = True
                    elif item.type == "life":
                        lives += 1
                    elif item.type == "magnet":
                        magnet_timer = 300
                    elif item.type == "shield":
                        has_shield = True

                    if score >= next_powerup_score:
                        player.activate_powerup()
                        next_powerup_score += 100
                        powerup_msg_timer = 120

                    if score >= next_fever_score:
                        fever_timer = 240
                        active_event = None
                        next_fever_score += 250

                    items.remove(item)
                elif item.y > SCREEN_HEIGHT:
                    if difficulty == "hard" and (item.type == "coin" or item.type == "gem" or item.type == "zigzag"):
                        missed_coins += 1
                        if missed_coins >= 5:
                            lives -= 1
                            missed_coins = 0
                            if lives <= 0:
                                game_over = True
                    items.remove(item)

        if not game_started:
            draw_start_screen()
        else:
            screen.fill(BLACK)
            player.draw(screen)

            for item in items:
                item.draw(screen)

            draw_hud()

            if smoke_timer > 0:
                fog_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                fog_surface.set_alpha(200)
                fog_surface.fill((50, 50, 50))
                screen.blit(fog_surface, (0, 0))

            if game_over:
                over_text = font.render("GAME OVER", True, BLUE)
                restart_text = font.render("Press R to Restart", True, WHITE)
                screen.blit(over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
                screen.blit(restart_text, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 20))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run_game()