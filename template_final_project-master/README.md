
# Mermaid Fish Collector Game
## CS110 B1 Final Project Fall 2024

## Team Members

Stephania Calin, Ava Attina

***

## Project Description

This game is about a mermaid who is attempting to catch fish with a specified color. On the top of the screen, there is be a counter displaying the number of fish that the player has caught. The player must avoid colliding with light blue fish, as the game will end.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. start menu
2. game over menu
3. timer
4. fish counter
5. obstacle collisions

### Classes

### Mermaid Class: Represents the mermaid
Represents the mermaid
- x(int): The mermaid's x-coordinates
- y(int): The mermaid's y-coordinates
- width(int): The width of the mermaid
- height(int): The height of the mermaid
- speed(int): How fast the mermaid moves
- rect(pygame.Rect): The rectangle representing the mermaid's position

#### Fish Class: Represents each fish on the screen
- self.image: The 30x30 rectangle which represents the fish
- self.rect: The rectangular boundary of the fish. When the mermaid collides with this boundary, it is detected and the mermaid will either gain or lose points.
- self.color: The color of the fish (either red, green, or light blue)
- update(self): The fish moves left across the screen. It will then respawn on the right if not caught.

## ATP

---

### Program: Mermaid Fish Collector Game 

---

### Test Case 1: Mermaid Movement  

| Step |              Procedure              |                Expected Results                 |
|------|:-----------------------------------:|-----------------------------------------------:|
|  1   | Start the game.                       | The game starts with the mermaid visible.       |
|  2   | Press the **Up** arrow key.           | The mermaid moves upward.                       |
|  3   | Press the **Down** arrow key.         | The mermaid moves downward.                     |
|  4   | Press the **Left** arrow key.         | The mermaid moves left.                         |
|  5   | Press the **Right** arrow key.        | The mermaid moves right.                        |

---

### **Test Case 2: Fish Color Collection**  

| Step |              Procedure              |                Expected Results                 |
|------|:-----------------------------------:|-----------------------------------------------:|
|  1   | Start the game.                      | The game starts with the mermaid visible.       |
|  2   | Either "red" or "green" is specified.    | This determines the type of fish the player must collect.             |
|  3   | Use the mermaid to collide with a fish of the specified color. | That fish is collected, and the score increases. |
|  4   | Attempt to collide with a fish of a different color. | The fish is not collected.           |

---

### **Test Case 3: Round Transition**  

| Step |              Procedure              |                Expected Results                 |
|------|:-----------------------------------:|-----------------------------------------------:|
|  1   | Collect the required number of fishes in the current round (e.g., 10 red fishes). | The required fish count is reached.             |
|  2   | Wait for the game to transition to the next round. | The game transitions smoothly to the next round. |
|  3   | Verify that a new color is specified for the round. | The round indicator displays a new color (e.g., Green). |

---

### **Test Case 4: Score and Seashell Reward**  

| Step |              Procedure              |                Expected Results                 |
|------|:-----------------------------------:|-----------------------------------------------:|
|  1   | Collect a set number of fishes in a round (e.g., 8 fishes). | The fish collection progresses.                 |
|  2   | Complete the round by reaching the target fish count. | The round ends, and the seashell reward is displayed. |
|  3   | Verify that the seashell reward corresponds to the number of fishes collected. | The seashell reward accurately reflects the number of fishes collected. |

---

### **Test Case 5: Graphical Display and Animation**  

| Step |              Procedure              |                Expected Results                 |
|------|:-----------------------------------:|-----------------------------------------------:|
|  1   | Start the game.                      | The game starts with the mermaid and fishes visible on the screen. |
|  2   | Observe the animations of the fishes moving across the screen. | Fishes move smoothly across the screen.         |
|  3   | Verify that the mermaid sprite moves smoothly in response to controls. | The mermaid moves smoothly in the specified direction. |
|  4   | Check that collected fishes disappear from the screen. | Collected fishes disappear instantly from the game view. |
|  5   | Observe the transition animations between rounds. | Smooth transition animations occur between rounds. | 
