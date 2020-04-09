import pygame
import time
import random
from pygame.locals import *



# 飞机类
class HeroPlan(object):
    def __init__(self, screen):
        self.x = 150
        self.y = 580
        self.screen = screen
        self.image = pygame.image.load('./feiji/hero1.png')
        self.bullet_list = []

    # 显示飞机
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # screen.blit(hero, (x, y))
        for bullet in self.bullet_list:
            # 让我方飞机子弹显示
            bullet.display()
            # 让我方飞机子弹移动
            bullet.move()
            if bullet.judge():
                # 让子弹列表里面的元素被删除
                self.bullet_list.remove(bullet)

    # 移动飞机
    def move_left(self):
        # x -= 5
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
            self.bullet_list.append(Bullet(self.screen, self.x, self.y))

# 我方飞机子弹类
class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = x + 30
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load('./feiji/bullet.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


# 敌机类
class EnemyPlan(object):
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image = pygame.image.load('./feiji/enemy0.png')
        self.direction = "right"
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            # 让敌方飞机子弹显示
            bullet.display()
            # 让敌方飞机子弹移动
            bullet.move()
            if bullet.judge():
                # 让子弹列表里面的元素被删除
                self.bullet_list.remove(bullet)


    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 340:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 28 or random_num == 78:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

# 敌机子弹类
class EnemyBullet(object):
    def __init__(self,screen,x,y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('./feiji/bullet1.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 700:
            return True
        else:
            return False


# 键盘控制
def key_contro(hero):
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # x -= 5
                hero.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # x += 5
                hero.move_right()
            elif event.key == K_SPACE:
                print("--space--")
                # 发射子弹
                hero.fire()

# 主函数
def main():
    # 创建窗口
    screen = pygame.display.set_mode((394, 700), 0, 32)
    # 创建背景图片
    background = pygame.image.load('./feiji/background.png')
    # 创建飞机
    hero = HeroPlan(screen)

    # 创建敌方飞机
    enemy = EnemyPlan(screen)

    while True:
        # 设置背景图片
        screen.blit(background, (0, 0))
        # 显示我方飞机
        hero.display()
        # 显示敌方飞机
        enemy.display()
        # 移动敌机
        enemy.move()
        # 敌方飞机发射子弹
        enemy.fire()
        # 键盘控制
        key_contro(hero)

        pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()