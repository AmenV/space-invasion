import pygame 


class Allien(pygame.sprite.Sprite):
    '''класс 1 пришельца'''
    def __init__(self, screen):
        '''инициализируем и задаём нач. позицию пришельца'''
        super(Allien,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/allien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def draw(self):
        '''вывод пришельца на экран'''
        self.screen.blit(self.image, self.rect)
        
        
        
    def update(self):
        '''перемещает пришельцев'''
        self.y += 0.1
        self.rect.y = self.y