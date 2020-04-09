import pygame
import time
from pygame.locals import *

# 飞机类
class HeroPlan(object):
    def __init__(self,screen):
        self.x = 150
        self.y = 580
        self.screen = screen
        self.image = pygame.image.load('./feiji/hero1.png')

    # 显示飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        # screen.blit(hero, (x, y))

    # 移动飞机
    def move_left(self):
        # x -= 5
        self.x -= 5
    def move_right(self):
        self.x += 5

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
            

# 主函数
def main():
    # 创建窗口
    screen = pygame.display.set_mode((394,700),0,32)
    # 创建背景图片
    background = pygame.image.load('./feiji/background.png')
    # 创建飞机
    hero = HeroPlan(screen)
    while True:
        # 设置背景图片
        screen.blit(background,(0,0))
        # 显示飞机
        hero.display()
        # 键盘控制
        key_contro(hero)

        pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()