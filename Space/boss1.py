import pygame
import math
import time
import constants
import spaceship
import enemybullet
import enemybullet2


class Boss1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.boss1width
        self.height = constants.boss1height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopeboss1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.rect.x >= constants.size[0]:
            self.speedx = -constants.boss1speed
        else:
            self.speedx = constants.boss1speed
        self.timer = time.time()
        self.bullettime = constants.boss1bullettimer
        self.health = constants.boss1health
        self.switch = 0

    def update(self, player, ebullets, enemies):
        if self.switch == 0:
            self.rect.x += constants.boss1speed
        if self.rect.x >= constants.size[0] - self.width:
            self.switch = 1

        if self.switch == 1:
            self.rect.x -= constants.boss1speed
        if self.rect.x <= 0:
            self.switch = 0

        if self.rect.y < 0:
            self.rect.y += constants.boss1speed


        distance = math.sqrt((self.rect.x - player.rect.x)**2 + (self.rect.y - player.rect.y)**2)
        xspeed = constants.enemy1bulletspeed * math.fabs(self.rect.x - player.rect.x)/distance
        yspeed = constants.enemy1bulletspeed * math.fabs(self.rect.y - player.rect.y)/distance


        if time.time() - self.timer + 0.0 > constants.boss1bullettimer:

            bullet1 = enemybullet2.Enemybullet2(self.rect.x + self.width / 2 - constants.ebulletwidth / 2 -10,
                                             self.rect.y + self.height, xspeed, yspeed)
            ebullets.add(bullet1)
            bullet2 = enemybullet2.Enemybullet2(self.rect.x + self.width / 2 - constants.ebulletwidth / 2 + 10,
                                             self.rect.y + self.height, xspeed, yspeed)
            ebullets.add(bullet2)

            count = 0
            while count < 7:
                #create a bullet
                if self.switch == 0:
                    spd = constants.ebullet2speed/2 + 1 * count
                if self.switch == 1:
                    spd = -constants.ebullet2speed/2 - 1 * count
                eb2 = enemybullet.Enemybullet(self.rect.x + self.width/2, self.rect.y + self.height/2, spd, constants.ebullet2speed)
                ebullets.add(eb2)
                count += 1

            self.timer = time.time()
