import pygame
import time

def play_sound(source):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(0.08)

    pygame.mixer.music.stop()
