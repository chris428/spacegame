import pygame
import constants
import spaceship
import spaceshipbullet
import enemytype1
import enemytype2
import enemytype3
import enemytype4
import time
import random
import powerup
import boss1


pygame.init()
screen = pygame.display.set_mode(constants.size)
playing = True
player = spaceship.Spaceship()
playerbullets = pygame.sprite.Group()
enemies= pygame.sprite.Group()
ebullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

#clock
enemy1spawn = time.time()
enemy2spawn = time.time()
powerupspawn = time.time()
gametimer = time.time()
enemyspawn = [[1, 4], [1, 6], [3, 7], [3, 9], [1, 12.5], [2, 13], [1, 16], [1, 18], [2, 20], [3, 20], [1, 22], [2, 24], [1, 27], [1, 28],
              [1, 28.75], [3, 29], [3, 29.5], [2, 37], [2, 37], [2, 37], [3, 37], [3, 37], [3, 37], [1, 40], [1, 42], [3, 42], [3, 44], [1, 45], [1, 48],
              [1, 51], [2, 54], [4, 60],

              [1, 85], [1, 86], [1, 87], [1, 88], [1, 88], [2, 88], [3, 88.5], [3, 89], [3, 89.5], [3, 90], [1, 90], [1, 90],
              [2, 90], [1, 90.5], [3, 92], [3, 92], [3, 92.5], [3, 93], [1, 100], [1, 100.5], [2, 101], [2, 101.2], [3, 102], [1, 102], [3, 102.5],
              [2, 107], [2, 107], [2, 107], [2, 107], [3, 107], [3, 107], [3, 107], [3, 107], [4, 107], [3, 108], [2, 109], [2, 110], [3, 111], [2, 112]
              ,[2, 113], [2, 114], [3, 114], [3, 115], [2, 116], [2, 118], [2, 118], [1, 119], [1, 119], [2, 122], [2, 122], [3, 123], [3, 123], [5, 125],

              [5, 150], [5, 151], [5, 151.5], [5, 152], [2, 152], [2, 152], [3, 152.5], [3, 152.5], [3, 156.6], [3, 157], [3, 158], [5, 159],
              [1, 160], [1, 160.25], [1, 160.5], [1, 160.75], [1, 161], [2, 161], [3, 161], [2, 162], [3, 162], [3, 163], [1, 163], [3, 164],
              [3, 167], [3, 167], [3, 167], [3, 167], [3, 167], [5, 167.5], [5, 167.5], [5, 167.5], [4, 170], [4, 190],

              [3, 219], [2, 221], [2, 221], [3, 222], [2, 222], [5, 230], [3, 231], [3, 231.2],
              [2, 232], [2, 232.5], [1, 232.75], [1, 232.75], [5, 234], [2, 234], [2, 234], [5, 235], [5, 236], [5, 237.5]]

#tracker
score = 0
lives = constants.lives


#background
image = pygame.image.load("background.jpeg")
image = pygame.transform.scale(image, (constants.size[0], constants.size[1]))
        #Music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

while playing:
    screen.blit(image, (0,0))
    for event in pygame.event.get():

        #quit
        if event.type == pygame.QUIT:
            playing = False

        #keydowns
        if event.type == pygame.KEYDOWN:

            #to move
            if event.key == pygame.K_RIGHT:
                player.speedx = constants.spaceshipspeed
            if event.key == pygame.K_LEFT:
                player.speedx = -constants.spaceshipspeed
            if event.key == pygame.K_UP:
                player.speedy = -constants.spaceshipspeed
            if event.key == pygame.K_DOWN:
                player.speedy = constants.spaceshipspeed

            #to shoot
            if event.key == pygame.K_SPACE:
                if player.powerlevel == 1:
                    bullet1 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth)
                    bullet2 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth)
                    playerbullets.add(bullet1)
                    playerbullets.add(bullet2)

                elif player.powerlevel == 2:
                    bullet1 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth)
                    bullet2 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth)

                    bullet3 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 5, constants.bulletwidth)
                    bullet4 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, -5, constants.bulletwidth)

                    playerbullets.add(bullet1)
                    playerbullets.add(bullet2)
                    playerbullets.add(bullet3)
                    playerbullets.add(bullet4)

                elif player.powerlevel == 3:
                    bullet1 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth * 2)
                    bullet2 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth * 2)

                    bullet3 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 2, constants.bulletwidth * 2)
                    bullet4 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, -2, constants.bulletwidth * 2)

                    playerbullets.add(bullet1)
                    playerbullets.add(bullet2)
                    playerbullets.add(bullet3)
                    playerbullets.add(bullet4)

                elif player.powerlevel == 4:
                    bullet1 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth * 3)
                    bullet2 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth * 3)

                    bullet3 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2,
                              player.rect.y + player.height/2 - constants.bulletheight/2, 1, constants.bulletwidth * 3)
                    bullet4 = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth,
                              player.rect.y + player.height/2 - constants.bulletheight/2, -1, constants.bulletwidth * 3)

                    playerbullets.add(bullet1)
                    playerbullets.add(bullet2)
                    playerbullets.add(bullet3)
                    playerbullets.add(bullet4)
                elif player.powerlevel in range(5, 8):
                    c = 0
                    while c < player.powerlevel:
                        bullet = spaceshipbullet.Spaceshipbullet(
                            player.rect.x + player.width / 2 - constants.bulletwidth,
                            player.rect.y + player.height / 2 - constants.bulletheight / 2, -player.powerlevel/2 + 1 * c,
                            constants.bulletwidth * 3)
                        playerbullets.add(bullet)
                        c+=1
                elif player.powerlevel >= 8:
                    c = 0
                    while c < 5:
                        bullet = spaceshipbullet.Spaceshipbullet(
                            player.rect.x + player.width / 2 - constants.bulletwidth,
                            player.rect.y + player.height / 2 - constants.bulletheight / 2, -2 + 1 * c,
                            constants.bulletwidth * 8)
                        playerbullets.add(bullet)
                        playerbullets.add(bullet)
                        playerbullets.add(bullet)
                        c+=1

                elif player.powerlevel == 0:
                    bullet = spaceshipbullet.Spaceshipbullet(player.rect.x + player.width/2 - constants.bulletwidth/2,
                             player.rect.y + player.height/2 - constants.bulletheight/2, 0, constants.bulletwidth)
                    playerbullets.add(bullet)

        #keyups
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.speedx = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                player.speedy = 0

    #create enemies

    for e in enemyspawn:

        if e[1] < time.time() - gametimer:
            if e[0] == 1:
                xpos = random.randint(0, constants.size[0])
                ypos = -50
                enemy1 = enemytype1.Enemytype1(xpos, ypos)
                enemies.add(enemy1)

            if e[0] == 2:
                ypos = random.randint(0, constants.size[1] / 2)
                flip = random.randint(0, 1)
                if flip == 0:
                    xpos = 0 - constants.enemytype2width
                else:
                    xpos = constants.size[0]
                enemy2 = enemytype2.Enemytype2(xpos, ypos)
                enemies.add(enemy2)

            if e[0] == 3:
                xpos = random.randint(0, constants.size[0])
                ypos = -constants.enemytype3height
                enemy3 = enemytype3.Enemytype3(xpos, ypos)
                flip = random.randint(0, 1)
                if xpos in range(0, constants.size[0]/2):
                    enemy3.speedx = constants.enemytype3speed/4
                else:
                    enemy3.speedx = -constants.enemytype3speed/4
                enemies.add(enemy3)

            if e[0] == 4:
                xpos = random.randint(constants.size[0]/2 - constants.boss1width, constants.size[0]/2 + constants.boss1width)
                ypos = -140
                boss = boss1.Boss1(xpos, ypos)
                enemies.add(boss)

            if e[0] == 5:
                xpos = random.randint(0, constants.size[0])
                ypos = -50
                enemy4 = enemytype4.Enemytype4(xpos, ypos)
                enemies.add(enemy4)

            enemyspawn.remove(e)


    if time.time() - powerupspawn > constants.poweruptimer:
        p = powerup.Powerup()
        powerups.add(p)
        powerupspawn = time.time()

    if score % 10 == 0 and score > 0 and constants.enemytype1timer - 0.25 > 2:
        constants.enemytype1timer -= 0.25
        constants.enemytype1speed += 0.25

    player.update()
    for bullet in playerbullets:
        if bullet.rect.y + bullet.height < 0:
            playerbullets.remove(bullet)
        screen.blit(bullet.image, bullet.rect)
        bullet.update()
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
        enemy.update(player, ebullets, enemies)
    for bullet in ebullets:
        if bullet.rect.y > constants.size[1] or bullet.rect.y < 0:
            ebullets.remove(bullet)
        screen.blit(bullet.image, bullet.rect)
        bullet.update()
    for p in powerups:
        screen.blit(p.image, p.rect)
        p.update()


    enemyshot = pygame.sprite.groupcollide(enemies, playerbullets, False, True)

    for e in enemies:
        if e in enemyshot:
            e.health -= len(enemyshot[e])
            score += 1
        if e.health <= 0:
            enemies.remove(e)



    ebulletscollided = pygame.sprite.spritecollide(player, ebullets, True)



    if len(ebulletscollided) > 0:
        screen.fill((255, 0, 0))
        lives -= 1
        if player.powerlevel > 0:
            player.powerlevel -= 1

    powerupscollided = pygame.sprite.spritecollide(player, powerups, True)

    if len(powerupscollided) > 0:
        player.powerlevel += 1

    if lives == 0:
        playing = False

    screen.blit(player.image, player.rect)
    pygame.display.update()

print score