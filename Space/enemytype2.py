import pygame
import time
import constants
import spaceship
import enemybullet2

class Enemytype2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.enemytype2width
        self.height = constants.enemytype2height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopeenemy2.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.rect.x >= constants.size[0]:
            self.speedx = -constants.enemytype2speed
        else:
            self.speedx = constants.enemytype2speed
        self.timer = time.time()
        self.bullettime = constants.enemytype2bullettimer
        self.health = constants.enemy2health


    def update(self, player, bullets, enemies):
        self.rect.x += self.speedx
        if self.speedx < 0 and self.rect.x + self.width < 0:
            enemies.remove(self)
        if self.speedx > 0 and self.rect.x > constants.size[0]:
            enemies.remove(self)
        if time.time() - self.timer > constants.enemytype2bullettimer:
            bullet = enemybullet2.Enemybullet2(self.rect.x + self.width/2 - constants.ebulletwidth/2,
                                             self.rect.y + self.height, 0, constants.enemy2bulletspeed)
            bullets.add(bullet)
            self.timer = time.time()
