# Exodus

This code implements a simple top-down RPG game called **Exodus** using the **Pygame** library. The player controls a character that must navigate through a grid-based environment filled with walls and enemies. The objective is to avoid enemies, but if the player collides with one, the game ends.

---

## Key Components

### 1. **Initialization and Constants**
- **Pygame Initialization:** `pygame.init()` initializes the Pygame library to handle graphics, sound, and events.
- **Constants:**
  - `WIDTH`, `HEIGHT`: Define the size of the game window (640x480 pixels).
  - `TILE_SIZE`: Refers to the size of each tile (32x32 pixels) in the grid.
  - `FPS`: Controls the game’s frame rate (60 frames per second).
  
- **Colors:**
  - `WHITE`: RGB value for white `(255, 255, 255)`.
  - `BLACK`: RGB value for black `(0, 0, 0)`.
  - `RED`: RGB value for red `(200, 0, 0)`.

### 2. **Window Setup**
- `pygame.display.set_mode()` creates the game window with the specified width and height.
- `pygame.display.set_caption("Exodus")` sets the title of the game window to "Exodus."

### 3. **Asset Loading**
- The game loads 32x32 images for the player (`player.png`), enemies (`enemy.png`), and walls (`wall.png`).
- These images are resized to match the `TILE_SIZE` (32x32 pixels).

### 4. **Font for Game Over Message**
- A font is initialized using `pygame.font.Font(None, 48)` to render the "Game Over" message in large text when the player loses.

### 5. **Player Class**
The `Player` class represents the player-controlled character:
- **Attributes:**
  - `rect`: A rectangular hitbox for the player, used for collision detection.
  
- **Methods:**
  - `move(dx, dy, walls)`: Moves the player character by `dx` and `dy` (change in x and y coordinates). It checks for collisions with walls before updating the position.
  - `draw(surface)`: Draws the player on the game screen at the player's current position.

### 6. **Enemy Class**
The `Enemy` class represents the enemy NPCs that move randomly:
- **Attributes:**
  - `rect`: The enemy's hitbox.
  - `speed`: The speed of the enemy's movement.
  - `direction`: The direction the enemy is moving (left, right, up, down).
  - `timer`: A random timer that controls how often the enemy changes direction.
  
- **Methods:**
  - `update(walls)`: Updates the enemy's movement. If the timer reaches 0, the enemy picks a new random direction. The movement is checked for collisions with walls.
  - `draw(surface)`: Draws the enemy on the screen.

### 7. **Wall Class**
The `Wall` class represents obstacles on the map:
- **Attributes:**
  - `rect`: The rectangular hitbox of the wall.
  
- **Methods:**
  - `draw(surface)`: Draws the wall at its current position on the screen.

### 8. **Map Layout**
The map of the game world is defined as a list of strings (`MAP`):
- Each character represents a tile on the map:
  - `"1"`: Wall tile.
  - `"2"`: Enemy spawn tile.
  - `"0"`: Empty floor tile.

The map is converted into `Wall` and `Enemy` objects based on the layout. These objects are used to generate the game world.

### 9. **Game Loop**
The core of the game is the main game loop, which runs continuously until the player quits:
- **Event Handling:** The loop processes any events, like closing the game window.
- **Player Movement:** The player's movement is controlled by the arrow keys or WASD keys. The `move()` method checks for collisions with walls before updating the position.
- **Enemy Movement:** Enemies move randomly. Each enemy updates its position and direction based on its timer.
- **Collision Detection:** If the player collides with any enemy, the game ends. A "Game Over" message is displayed, and the game halts after a 2-second delay.
- **Drawing:** All elements (walls, player, enemies) are drawn on the screen.

### 10. **Game Over Logic**
When the player collides with an enemy, the game displays the "Game Over" message at the center of the screen. After a 2-second delay (`pygame.time.delay(2000)`), the game ends.

### 11. **Frame Rate**
The game is set to run at 60 frames per second using `clock.tick(FPS)`.

### 12. **Exiting the Game**
When the player chooses to quit the game or collides with an enemy, `pygame.quit()` is called to properly close the Pygame window.

---

## Summary

- **Exodus** is a top-down RPG where you control a player character on a grid-based map.
- The player moves around the environment while avoiding enemies and obstacles (walls).
- The game ends when the player collides with an enemy, displaying a "Game Over" message.
- The game uses Pygame for rendering the graphics, handling events, and managing frame rate.


