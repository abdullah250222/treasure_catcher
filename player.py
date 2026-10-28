import pygame
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED

class Player:
    def __init__(self):
        self.base_width = PLAYER_WIDTH
        self.width = self.base_width
        self.height = PLAYER_HEIGHT
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = PLAYER_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.powerup_timer = 0

    def activate_powerup(self):
        self.width = self.base_width * 2
        self.powerup_timer = 420
        self.rect.width = self.width

    def move(self, keys):
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
            if self.powerup_timer == 0:
                self.width = self.base_width
                self.rect.width = self.width

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed

        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)