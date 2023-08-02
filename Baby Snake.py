from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 20
VELOCITY = 20
DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = 0
    player = canvas.create_rectangle(start_x, start_y,
                                     SQUARE_SIZE, start_y + SQUARE_SIZE, 'blue')
    goal = canvas.create_rectangle(start_x + 360, start_y + 360,
                                   SQUARE_SIZE + 360, SQUARE_SIZE + 360, 'salmon')

    direction = "right" # Start moving right initially
    points = 0

    while True:
        # Handle key press
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = "left"
        elif key == 'ArrowRight':
            direction = "right"
        elif key == 'ArrowUp':
            direction = "up"
        elif key == 'ArrowDown':
            direction = "down"

        # Update the player's position based on the direction
        if direction == "left":
            start_x -= VELOCITY
        elif direction == "right":
            start_x += VELOCITY
        elif direction == "up":
            start_y -= VELOCITY
        elif direction == "down":
            start_y += VELOCITY

        canvas.moveto(player, start_x, start_y)

        # Detecting collisions
        x = canvas.get_left_x(player)
        y = canvas.get_top_y(player)

        if (x < start_x) or (x >= CANVAS_WIDTH) or (y < start_y) or (y >= CANVAS_HEIGHT):
            break

        # Check collision with goal
        player_x1, player_y1 = x, y
        player_x2, player_y2 = x + SQUARE_SIZE, y + SQUARE_SIZE

        goal_x1, goal_y1 = canvas.get_left_x(goal), canvas.get_top_y(goal)
        goal_x2, goal_y2 = goal_x1 + SQUARE_SIZE, goal_y1 + SQUARE_SIZE

        if player_x1 < goal_x2 and player_x2 > goal_x1 and player_y1 < goal_y2 and player_y2 > goal_y1:
            points += 1
            print(f"Score: {points}")

            # Move the goal to a new random location
            new_x = random.randint(0, CANVAS_WIDTH - SQUARE_SIZE)
            new_y = random.randint(0, CANVAS_HEIGHT - SQUARE_SIZE)
            canvas.moveto(goal, new_x, new_y)

        # Sleep
        time.sleep(DELAY)

if __name__ == '__main__':
    main()
