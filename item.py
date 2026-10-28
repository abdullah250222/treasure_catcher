import pygame
import random
import math
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, GOLD, RED, GREEN, CYAN, PURPLE, ORANGE, GRAY, ICE_BLUE

class Item:
    def __init__(self, speed_multiplier=1.0, forced_type=None):
        self.width = 25
        self.height = 25
        self.x = random.randint(40, SCREEN_WIDTH - self.width - 40)
        self.y = -self.height
        
        if forced_type:
            self.type = forced_type
        else:
            self.type = random.choice(["coin", "coin", "coin", "bomb", "bomb"])

        if self.type == "gem":
            self.width = 30
            self.height = 30

        if self.type == "coin":
            self.color = GOLD
        elif self.type == "gem":
            self.color = GOLD
        elif self.type == "zigzag":
            self.color = ORANGE
        elif self.type == "bomb":
            self.color = RED
        elif self.type == "smoke":
            self.color = GRAY
        elif self.type == "life":
            self.color = GREEN
        elif self.type == "magnet":
            self.color = CYAN
        elif self.type == "shield":
            self.color = PURPLE
        elif self.type == "slowmo":
            self.color = ICE_BLUE

        base_speed = random.randint(3, 6)
        self.speed = base_speed * speed_multiplier
        self.zigzag_angle = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed

        if self.type == "zigzag":
            self.zigzag_angle += 0.1
            self.x += math.sin(self.zigzag_angle) * 4
            if self.x < 0:
                self.x = 0
            elif self.x > SCREEN_WIDTH - self.width:
                self.x = SCREEN_WIDTH - self.width

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)