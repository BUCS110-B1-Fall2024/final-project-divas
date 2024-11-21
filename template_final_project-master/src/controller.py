def __init__(self, screen, image_path, x=100, y=100, speed=5):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
def __init__(self):
"""
docstring
"""
def mainloop(self):
"""
docstring
"""
while(True):
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit() exit()
pygame.display.flip()
