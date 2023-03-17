import pygame

# Grid lock pattern constants
GRID_SIZE = 100
GRID_WIDTH = 3
GRID_HEIGHT = 3

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * GRID_WIDTH, GRID_SIZE * GRID_HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Grid lock pattern state
pattern = []
current_position = None

# Draw the grid lock pattern
def draw_grid():
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, GRAY, (i * GRID_SIZE, j * GRID_SIZE, GRID_SIZE, GRID_SIZE), 3)

# Check if a point is inside a grid cell
def is_point_inside_cell(point, cell):
    cell_x, cell_y = cell
    cell_rect = pygame.Rect(cell_x * GRID_SIZE, cell_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    return cell_rect.collidepoint(point)

# Get the grid cell coordinates for a point
def get_cell_for_point(point):
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            if is_point_inside_cell(point, (i, j)):
                return (i, j)
    return None

# Draw the current pattern state
def draw_pattern():
    for i in range(len(pattern)):
        if i == 0:
            pygame.draw.circle(screen, WHITE, pattern[i], GRID_SIZE // 6)
        else:
            pygame.draw.line(screen, WHITE, pattern[i - 1], pattern[i], GRID_SIZE // 10)
    if current_position is not None:
        pygame.draw.line(screen, WHITE, pattern[-1], current_position, GRID_SIZE // 10)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start drawing the pattern
            cell = get_cell_for_point(event.pos)
            if cell is not None:
                current_position = (cell[0] * GRID_SIZE + GRID_SIZE // 2, cell[1] * GRID_SIZE + GRID_SIZE // 2)
                pattern.append(current_position)
        elif event.type == pygame.MOUSEMOTION:
            # Continue drawing the pattern
            if current_position is not None:
                current_position = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            # End drawing the pattern
            current_position = None
    # Draw the screen
    screen.fill(BLACK)
    draw_grid()
    draw_pattern()
    pygame.display.flip()

# Output the pattern coordinates
print(pattern)