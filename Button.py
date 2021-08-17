import pygame
from SoundsPlayer import play_sound

class Button:
    def __init__(self, before_img, after_img, pos, size):
        self._before_img = before_img
        self._after_img = after_img
        self._pos = pos
        self._size = size
        self._sound = "Sounds/Click2.mp3"
    
    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        self._size = new_size
        
    def draw(self, display):
        img = self._before_img
        if self.check_hover():
            img = self._after_img

        play_image = pygame.image.load(img)
        display.blit(play_image, (self._pos[0], self._pos[1]))
        pygame.display.update()
    
    def check_hover(self):
        pos = pygame.mouse.get_pos()

        if pos[0] >= self._pos[0] and pos[0] <= (self._pos[0] + self._size[0]) and pos[1] >= self._pos[1] and pos[1] <= (self._pos[1] + self._size[1]):
            return True
        return False
    
    def check_click(self):
        click_pos = pygame.mouse.get_pos()

        if click_pos[0] <= self._pos[0] or click_pos[0] >= (self._pos[0] + self._size[0]) or click_pos[1] <= self._pos[1] or click_pos[1] >= (self._pos[1] + self._size[1]):
            return False
        play_sound(self._sound, 0.22)
        return True
