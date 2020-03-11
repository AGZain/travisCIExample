from spaceShooter import *
import pygame
from time import sleep
import pytest
 

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(all_sprites,bullets)

def test_lives():
    assert 3 == player.lives,"Failed: Initial Lives is bad!"

def test_Initialpower():
    assert 1 == player.power,"Failed: Power Did not start at 1"

def test_powerUp():
    player.powerup()
    assert 2 == player.power,"Failed: Power Up did not yeild an increase of power by 1"
    player.powerup()
    assert 3 == player.power,"Failed: Power Up did not yeild an increase of power by 1."

def test_shield():
    assert 100 == player.shield, "Failed: Player did not start with 100 shield"
def test_bullets():
    sleep(0.5)
    player.shoot()
    assert 3 == len(player.bullets),"Failed: Number of bullets did not increase with powerup"

def test_powerUpTime():
    sleep(5)
    if (player.power < 2):
        player.powerup()
    curr = player.power
    player.update()
    assert curr - 1 == player.power, "Failed: Power Did not decrease with time"

def test_moveLeft():
    curr = player.rect.x
    pygame.key.get_pressed = keyPress(pygame.K_LEFT)
    player.update()
    assert curr - 5 == player.rect.x,"Failed: Spaceship did not move to the left"

def test_moveRight():
    curr = player.rect.x
    pygame.key.get_pressed = keyPress(pygame.K_RIGHT)
    player.update()
    
    assert curr + 5 == player.rect.x,"Failed: Spaceship did not move to the right"

def test_spaceBarToShoot():
    curr = len(bullets)
    sleep(0.5)
    pygame.key.get_pressed = keyPress(pygame.K_SPACE)
    player.update()
    
    assert curr + player.power == len(bullets), "Failed: New bullets were not shot upon press of space bar"

def test_shootBullet():
    newBullet = Bullet(player.rect.centerx, player.rect.top)
    curr = newBullet.rect.y
    newBullet.update()
    assert curr -10 == newBullet.rect.y, "Failed: Bullet did not move after being shot"

def test_missles():
    newMissle = Missile(player.rect.centerx, player.rect.top)
    curr = newMissle.rect.y
    newMissle.update()
    assert curr -100 == newMissle.rect.y, "Failed: Missle did not move after being shot"

def keyPress(key):
    def press():
        arr = [0] * 1000
        arr[key] = 1
        return arr
    return press


