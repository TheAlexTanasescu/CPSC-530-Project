import pygame

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 3
CIRCLE_SIZE = 50

# Define colors
WHITE = (255, 255, 255)
GREENS = [(204, 255, 204), (153, 255, 153), (0, 204, 0), (0, 153, 0)]

# Define intensity levels (from 1 to 20)
intensity_levels = [[4, 2, 3],
                    [4, 3, 3],
                    [4, 1, 4]]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Android Visualizer")

# Draw the grid
grid_color = WHITE
line_width = 5
cell_size = SCREEN_WIDTH // GRID_SIZE
for i in range(1, GRID_SIZE):
    # Draw horizontal line
    pygame.draw.line(screen, grid_color, (0, i * cell_size), (SCREEN_WIDTH, i * cell_size), line_width)
    # Draw vertical line
    pygame.draw.line(screen, grid_color, (i * cell_size, 0), (i * cell_size, SCREEN_HEIGHT), line_width)

# Draw the circles with different shades of green based on intensity levels
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        intensity = intensity_levels[row][col]
        circle_color = GREENS[intensity - 1]
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2
        pygame.draw.circle(screen, circle_color, (x, y), CIRCLE_SIZE // 2)

# Update the display
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
