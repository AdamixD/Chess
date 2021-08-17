import pygame
import time

def play_sound(source, stime=0.08):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(stime)

    pygame.mixer.music.stop()
