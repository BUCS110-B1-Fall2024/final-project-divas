import random
import pygame


pygame.init()


#what the screen will look like
screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Mermaid Fish Collector Game")
clock = pygame.time.Clock()
FPS = 60

red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
blue = (0, 0, 255)


#mermaid settings
mermaid_x, mermaid_y = screenWidth // 2, screenHeight // 2
mermaidSpeed = 5
mermaid_width, mermaid_height = 100, 50

running = True
gameState = "start"

score = 0 # the score begins at 0
current_round_color = red # update so this changes as the rounds progress
required_fish = 10
collected_fish = 0


#fishie settings
fish_group = pygame.sprite.Group()


class Fish(pygame.sprite.Sprite):
   def __init__(self, x, y, color):
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


def spawnFish():
    target_fish_count = 0
    for _ in range(10):  # begins with 10 fish on the screen
        x = random.randint(screenWidth, screenWidth + 200)
        y = random.randint(0, screenHeight - 30)
        if target_fish_count < 5:
            color = current_round_color
            target_fish_count += 1
        else:
            color = random.choice([red, green])
        fish = Fish(x, y, color)
        fish_group.add(fish)
spawnFish()


def drawScreen():
    screen.fill(blue)
    font = pygame.font.Font(None, 74)
    text = font.render("Press SPACE To Begin:", True, white)
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - 50))


def pauseScreen():
    screen.fill(blue)
    font = pygame.font.Font(None, 74)
    text = font.render("Game Paused", True, white)
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - 50))


def gameOver_screen():
    screen.fill(blue)
    font = pygame.font.Font(None, 74)
    text = font.render(f"Final Score: {score}", True, white)
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - 50))
    text_restart = pygame.font.Font(None, 50).render("Press R to Restart", True, white)
    screen.blit(text_restart, (screenWidth // 2 - text_restart.get_width() // 2, screenHeight // 2 + 50))


def drawGame():
    screen.fill(blue)
    pygame.draw.rect(screen, white, (mermaid_x, mermaid_y, mermaid_width, mermaid_height)) 
    fish_group.draw(screen)
    font = pygame.font.Font(None, 36)
    color_name = "Red" if current_round_color == red else "Green"
    text = font.render(f"Current score: {score} | You have {collected_fish}/{required_fish} fish | Round: {color_name}", True, white)
    screen.blit(text, (10, 10))


#main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if gameState == "start" and event.key == pygame.K_SPACE:
                gameState = "active"
            if gameState == "pause" and event.key == pygame.K_p:
                gameState = "active"
            elif gameState == "active" and event.key == pygame.K_p:
                gameState = "pause"
            if gameState == "game_over" and event.key == pygame.K_r:
                gameState = "start"
                score = 0
                collected_fish = 0
                fish_group.empty()
                spawnFish()


#mermaid movement on the keyboard
    keys = pygame.key.get_pressed()
    if gameState == "active":
        if keys[pygame.K_UP] and mermaid_y > 0:
            mermaid_y -= mermaidSpeed
        if keys[pygame.K_DOWN] and mermaid_y < screenHeight - mermaid_height:
            mermaid_y += mermaidSpeed
        if keys[pygame.K_LEFT] and mermaid_x > 0:
            mermaid_x -= mermaidSpeed
        if keys[pygame.K_RIGHT] and mermaid_x < screenWidth - mermaid_width:
            mermaid_x += mermaidSpeed
        fish_group.update()
        for fish in fish_group:
            if pygame.Rect(mermaid_x, mermaid_y, mermaid_width, mermaid_height).colliderect(fish.rect):
                if fish.color == current_round_color:
                    score += 1
                    collected_fish += 1
                    fish.kill()
                    print(f"Fish collected: {collected_fish}/{required_fish}")
                else:
                    print("Wrong color!")

                #respawn fish if there are not enough
                if len(fish_group) < 10:
                    spawnFish()

   #keeping track of the users actions/if they are collecting the correct fish
    if gameState == "active":
        fish_group.update()
        for fish in fish_group:
            if pygame.Rect(mermaid_x, mermaid_y, mermaid_width, mermaid_height).colliderect(fish.rect):
                if fish.color == current_round_color:
                    score += 1
                    collected_fish += 1
                    fish.kill()
                else:
                    print("Wrong color!")
        #checks round completion
        if collected_fish >= required_fish:
            collected_fish = 0
            current_round_color = random.choice([red, green]) #gives new target color
            fish_group.empty()
            spawnFish()
            print("New round started!")


    if gameState == "start":
        drawScreen()
    elif gameState == "active":
        drawGame()
    elif gameState == "pause":
        pauseScreen()
    elif gameState == "game_over":
        gameOver_screen()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
