class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # 设置最高分
        self.high_score = 0

    def reset_stats(self):
        """重置游戏数据"""
        self.ships_left = self.ai_settings.ship_limit
        self.game_score = 0
        self.level = 1