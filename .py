import pygame
import sys

# Initialize pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define vehicle parameters
vehicle_length = 50
vehicle_width = 20
vehicle_color = RED

# Define simulation parameters
dt = 0.1  # Time step (s)
initial_speed = 0.0  # Initial speed (m/s)
initial_position = (100, SCREEN_HEIGHT // 2)  # Initial position (x, y)
initial_heading = 0.0  # Initial heading angle (degrees)

# Define vehicle state variables
speed = initial_speed
position = list(initial_position)
heading = initial_heading

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vehicle Dynamics Simulation")

# Main simulation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Update vehicle position based on speed and heading
    position[0] += speed * dt * pygame.math.cos(pygame.math.radians(heading))    # Positions X, Current speed, time step of the simulation, Horizontal Component   
    position[1] += speed * dt * pygame.math.sin(pygame.math.radians(heading))    # Position y, Current speed,  time step of the simulation, Vertical Component

    # Draw vehicle
    vehicle_rect = pygame.Rect(position[0] - vehicle_length / 2, position[1] - vehicle_width / 2,
                               vehicle_length, vehicle_width)       # Top left corner of rectangle    
    pygame.draw.rect(screen, vehicle_color, vehicle_rect)
    pygame.draw.circle(screen, BLACK, position, 5)              # Draw a point at the center of the vehicle

    # Update the display
    pygame.display.flip()

    # Control the simulation speed
    pygame.time.delay(int(dt * 1000))  # Delay in milliseconds

    # Example: Change the vehicle heading over time (for demonstration purposes)
    heading += 1  # Increment heading angle (degrees)
