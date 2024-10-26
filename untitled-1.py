import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import scores

def run():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 650))
    pygame.display.set_caption('Game_1')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.createarmy(screen, inos)
    stats = Stats()
    sc = scores(screen, stats)
    
    
    while True:
        controls.events(screen, gun, bullets)
        if stats.rungame == True:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, bullets, gun, inos )
            
run()