# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint as rd
from player import Player
from enemy import Enemy

# РАЗМЕРЫ ОКОШКА
WIDTH = 500
HEIGHT = 300

FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


player = Player("./capibara.png",100,120, 200,200)

enemyGroup = pygame.sprite.Group()
def spawnEnemy():
    enemy = Enemy("./zombie.png",width=rd(20,50),height=rd(20,50),x=rd(0,WIDTH),y=rd(0,200))
    enemyGroup.add(enemy)

for i in range (5):
    spawnEnemy()






x = 0



bullets = []
countHit = 0
running = True
while running:
    


    



    screen.fill(WHITE)
    for enemy in enemyGroup:
        enemy.draw(screen)
        enemy.follow(player,1)
    pygame.draw.rect(screen, GREEN,(x,200,50,20))
    player.draw(screen)
    player.movement()
    if x >= WIDTH+20:
        x = -70
    # Держим цикл на правильной скорости

    for bullet in bullets:
        bullet.draw(screen)
        bullet.move()



        colliderSprite = pygame.sprite.spritecollideany(bullet,enemyGroup)
        if colliderSprite:
            bullets.remove(bullet)
            enemyGroup.remove(colliderSprite)
            countHit += 1

    clock.tick(FPS)

    

    if pygame.sprite.spritecollideany(player,enemyGroup):
        print("СТОЛКНОВЕНИЕ")
        player.hp -= 1
        if player.hp <= 0:
            print('смерть')
            running = False
    pygame.display.update()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = player.shoot(mouse_x,mouse_y)
                if bullet:
                    bullets.append(bullet)
                
    
pygame.quit()


# домашка 21.12.2024
# TODO Сделать движение вверх-вниз через клавиши, сделать проверки на пересечение верхней границы, нижней, и левой границ