import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """定义单个👽的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并定义初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('image\salien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向右移动外星人"""
        self.x += self.ai_settings.fleet_direction * self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

