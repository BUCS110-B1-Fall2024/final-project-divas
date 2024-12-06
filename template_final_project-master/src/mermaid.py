class Mermaid:
    """
    Represents the mermaid
    x(int): The mermaid's x-coordinates
    y(int): The mermaid's y-coordinates
    width(int): The width of the mermaid
    height(int): The height of the mermaid
    speed(int): How fast the mermaid moves
    rect(pygame.Rect): The rectangle representing the mermaid's position
    
    """
    def __init__(self, x, y, width, height, speed):
        """
        Initializes the mermaid
        x(int): The mermaid's starting x-coordinate
        y(int): The mermaid's starting y-coordinate
        width(int): The mermaid's width
        height(int): The mermaid's height
        speed(int): The mermaid's speed
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
        
    def move(self,keys):
        """
        Updates the mermaid's on screen position
        keys(dict): Different key states (up, down) from the pygame dictionary
        """
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < screenHeight - self.height:
            self.y += self.speed
        self.rect.update(self.x, self.y, self.width, self.height)

