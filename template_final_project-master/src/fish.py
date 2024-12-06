
class Fish(pygame.sprite.Sprite):
    """
    Represents the fish
    image(pygame.Surface): The red, green, and light blue rectangles which represent the fish
    rect(pygame.Rect): The rectangle representing the fish
    color(tuple): The color (Red/Green/Light Blue) of the fish
    """
    def __init__(self, x, y, color):
       """
       Initializes the fish
       x(int): The starting x-coordinate of the fish
       y(int): The starting y-coordinate of the fish
       color(tuple): The color of the fish
       """
       super().__init__()
       self.image = pygame.Surface((30, 30))
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.color = color


    def update(self):
       self.rect.x -= 2  # Move fish left
       if self.rect.x < -30:  # Reset fish if it goes off-screen
           self.rect.x = screenWidth + random.randint(0, 200)
           self.rect.y = random.randint(0, screenHeight - 30)

