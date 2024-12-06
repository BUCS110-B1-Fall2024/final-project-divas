import random
import pygame
import os
from fish import Fish
from mermaid import Mermaid

pygame.init()

#what the screen will look like
screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Mermaid Fish Collector Game")
clock = pygame.time.Clock()
FPS = 60

#constants of different colors
Red = (255, 0, 0)
Green = (0, 255, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Lightblue = (173, 216, 230)

mermaid = Mermaid(screenWidth//2, screenHeight//2, 70, 50, 5)

running = True
gameState = "start"

seashells = 0 # the score begins at 0
high_score = 0
current_round_color = Red # update so this changes as the rounds progress
required_fish = 10
collected_fish = 0
rounds_played = 0
max_rounds = 10

#fishie settings
fish_group = pygame.sprite.Group()

#this stores the high score
high_score_file = "high_score.txt"

if os.path.exists(high_score_file):
    with open(high_score_file, "r") as file:
        high_score = int(file.read().strip())
else:
    high_score = 0

def spawnFish():
    """
    Spawns fish on the right side of the screen. There will be a variety of the three possible color fish.
    """
    target_fish_count = 0
    for _ in range(10):  # begins with 10 fish on the screen
        x = random.randint(screenWidth, screenWidth + 200)
        y = random.randint(0, screenHeight - 30)
        if target_fish_count < 5:
            color = current_round_color
            target_fish_count += 1
        else:
            color = random.choice([Red, Green])
            
        if random.random() < 0.2: #20% chance a light blue fish/ azure fish will spawn
            color = Lightblue
            
        fish = Fish(x, y, color)
        fish_group.add(fish)
spawnFish()

def drawScreen():
    """
    Draws the game's starting screen. The user must press SPACE to begin.
    """
    screen.fill(Blue)
    font = pygame.font.Font(None, 74)
    text = font.render("Press SPACE To Begin:", True, White)
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - 50))


def pauseScreen():
    """
    Draws the pause screen
    """
    screen.fill(Blue)
    font = pygame.font.Font(None, 74)
    text = font.render("Game Paused", True, White)
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - 50))


def gameOver_screen():
    """
    Draws the game over screen after 10 rounds. The user's final score and high score are displayed. Their high score carries across different game sessions
    """
    screen.fill(Blue)
    font = pygame.font.Font(None, 74)
    text = font.render(f"Final Score: {seashells} Seashells", True, White)
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - 50))
    
    high_score_text = pygame.font.Font(None, 50).render(f"High Score: {high_score} Seashells", True, White)
    screen.blit(high_score_text, (screenWidth // 2 - high_score_text.get_width() // 2, screenHeight // 2 + 50))

    text_restart = pygame.font.Font(None, 50).render("Press R to Restart", True, White)
    screen.blit(text_restart, (screenWidth // 2 - text_restart.get_width() // 2, screenHeight // 2 + 100))
    
def drawGame():
    """
    Draws the game screen, fish, mermaid, and displays the user's score
    """
    screen.fill(Blue)
    pygame.draw.rect(screen, White, mermaid.rect) 
    fish_group.draw(screen)
    font = pygame.font.Font(None, 30)
    color_name = "Red" if current_round_color == Red else "Green"
    text = font.render(f"Current score: {seashells} | Your target is: {collected_fish}/{required_fish} | Round: {color_name} | Round #: {rounds_played}/{max_rounds}", True, White)
    screen.blit(text, (10, 10))

#high score
def update_high_score():
    """
    Updates the user's high score if they beat it. This is then saved to file
    """
    global high_score
    if seashells > high_score:
        high_score = seashells
        with open(high_score_file, "w") as file:
            file.write(str(high_score))
        
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
                seashells = 0
                collected_fish = 0
                rounds_played = 0
                fish_group.empty()
                spawnFish()

#mermaid movement on the keyboard
    keys = pygame.key.get_pressed()
    if gameState == "active":
        mermaid.move(keys)
        fish_group.update()
        
        for fish in fish_group:
            if mermaid.rect.colliderect(fish.rect):
                if fish.color == Lightblue:
                    seashells -= 2
                    print(f"Wrong fish! You lost 2 seashells! Now you only have {seashells} seashells.")
                    fish.kill()
                elif fish.color == current_round_color:
                    seashells += 1
                    collected_fish += 1
                    fish.kill()
                    print(f"Fish collected: {collected_fish}/{required_fish}")
                else:
                    seashells -= 1
                    print("Wrong color!")
                    fish.kill()

                # Respawn fish if needed
                if len(fish_group) < 10:
                    spawnFish()

   #keeping track of the users actions
    if gameState == "active":
        fish_group.update()
        for fish in fish_group:
            if mermaid.rect.colliderect(fish.rect):
                if fish.color == current_round_color:
                    seashells += 1
                    collected_fish += 1
                    fish.kill()
                else:
                    print("Wrong color!")
                    
        #checking round completion
        if collected_fish >= required_fish:
            collected_fish = 0
            current_round_color = random.choice([Red, Green]) #gives new target color
            fish_group.empty()
            spawnFish()
            print("New round started!")
            rounds_played += 1
            if rounds_played >= max_rounds:
                gameState = "game_over"
                update_high_score()

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
pygame.display.flip()
clock.tick(FPS)

pygame.quit()
