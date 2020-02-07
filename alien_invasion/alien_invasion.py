import sys

import pygame
from pygame.sprite import Group

from Button import Button
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions


def run_game():
    # 初始化游戏并创建一个屏幕对象

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创造一个用于储存子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建第一行外星人
    game_functions.creat_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建 play 按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 开始游戏的主循环
    while True:

        # 监听用户的事件
        game_functions.check_events(ai_settings, screen, stats, ship, aliens,
                                    bullets, play_button,scoreboard=sb)

        # 如果飞船还有命
        if stats.game_active:
            # 更新飞船的位置
            ship.updata()

            # 更新Group中的每一个bullet
            game_functions.update_bullets(ai_settings, screen, stats, ship, aliens, bullets, sb)

            # 更新外星人的位置
            game_functions.update_aliens(ai_settings, stats, screen, ship, bullets, aliens, scoreboard=sb)

        # 更新整个屏幕
        game_functions.updata_screen(setting=ai_settings, screen=screen, stats=stats, ship=ship,
                                     bullets=bullets, aliens=aliens, play_button=play_button, scoreboard = sb)


run_game()
