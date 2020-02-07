import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def updata_screen(setting, screen, stats, ship, bullets, aliens, play_button, scoreboard):
    # 每次循环时都重绘屏幕
    screen.fill(setting.bg_color)
    # 在外星人和飞船后绘制所有的子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 如果游戏处于非活动状态，就绘制 Play 按钮
    if not stats.game_active:
        play_button.draw_button()

    # 显示得分
    scoreboard.show_scoreboard()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def check_high_score(stats, scoreboard):
    """检查是否诞生了最高分"""
    if stats.game_score > stats.high_score:
        stats.high_score = stats.game_score
        scoreboard.prep_high_score()


# ship
def check_events(ai_settings, screen, stats, ship, aliens,
                 bullets, play_button, scoreboard):
    """监听事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, ship, aliens,
                              bullets, play_button, scoreboard, mouse_x, mouse_y)




def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard):
    """被外星人撞到的飞船"""
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # 更新记分牌
        scoreboard.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创造一批新的外星人，并把飞船居中
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)

    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False


# bullets
def update_bullets(ai_settings, screen, stats, ship, aliens, bullets, scoreboard):
    """更新屏幕中所有的bullets"""
    # 更新子弹的位置
    bullets.update()

    # 删除屏幕中已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullets_alien_collisions(ai_settings, screen, stats, ship, bullets, aliens, scoreboard)


def check_bullets_alien_collisions(ai_settings, screen, stats, ship, bullets, aliens, scoreboard):
    # 检查是否有子弹击中了外星人
    # 如果击中就删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for aliens in collisions.values():
            stats.game_score += ai_settings.alien_point * len(aliens)
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    start_new_level(ai_settings, screen, stats, ship, bullets, aliens, scoreboard)


def start_new_level(ai_settings, screen, stats, ship, bullets, aliens, scoreboard):
    if len(aliens) == 0:
        # 删除现有所有的子弹并新建一批外星人
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)

        # 提升等级
        stats.level += 1
        scoreboard.prep_level()

        # 加快游戏节奏
        ai_settings.increase_speed()


def fire_bullet(ai_settings, screen, ship, bullets):
    """发射子弹"""
    # 创建以可子弹，并加入到编组中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# alien
# calculate
def get_number_aliens(ai_settings, alien):
    alien_width = alien.rect.width
    available_width = ai_settings.screen_width - 2 * alien_width
    number_alien = int(available_width / (2 * alien_width))
    return number_alien - 1


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# create
def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算外星人之间的合理宽度
    alien = Alien(ai_settings, screen)
    number_alien = get_number_aliens(ai_settings, alien)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人
    for row_number in range(number_rows):
        creat_alien(ai_settings, screen, number_alien, aliens, row_number)


def creat_alien(ai_settings, screen, number_alien, aliens, number_rows):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 创建第一行外星人
    for alien_number in range(number_alien):
        # 创建一个外星人并加入当前行
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_rows
        aliens.add(alien)


def update_aliens(ai_settings, stats, screen, ship, bullets, aliens, scoreboard):
    """更新外星人的位置"""
    # 查看是否有外星人在屏幕的边缘
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard)

    # 检查有没有外星人越过底部
    check_alines_bottom(ai_settings, stats, screen, ship, aliens, bullets, scoreboard)


def check_fleet_edges(ai_settings, aliens):
    """若外星人到达屏幕边缘 采取的措施"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def check_alines_bottom(ai_settings, stats, screen, ship, aliens, bullets, scoreboard):
    """检查是否有外星人达到了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 与飞船被外星人撞击相同
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, scoreboard)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移 并改变运动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



# button
def check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, scoreboard, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.game_active = True

        # 隐藏鼠标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()

        # 重置计分板
        scoreboard.prep_scoreboard()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一批外星人，并让飞船居中
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 重置游戏速度
        ai_settings.initialize_dynamic_settings()

