import pygame
import random
import math

# --- Initialization ---
pygame.init()

# Using namespace std equivalent in Python by importing functions directly
from random import randint, uniform
from math import sin, cos, atan2, degrees, radians

# --- Constants and Configuration ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUBBLE_COLOR = (180, 220, 255, 50) # RGBA for transparency

# Particle Swarm Settings
NUM_PARTICLES = 300
PARTICLE_ACCELERATION = 0.01  # How strongly they are attracted to the mouse
PARTICLE_DAMPING = 0.97       # Friction/air resistance

# Bubble Mass Settings
NUM_BUBBLES = 50
BUBBLE_SPAWN_EVENT = pygame.USEREVENT + 1


# --- Screen Setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("nParticle Swarms and Bubble Masses")
clock = pygame.time.Clock()
pygame.time.set_timer(BUBBLE_SPAWN_EVENT, 100) # Spawn a new bubble every 100ms

# --- Particle Class for the Swarm ---
class Particle:
    def __init__(self):
        self.x = uniform(0, SCREEN_WIDTH)
        self.y = uniform(0, SCREEN_HEIGHT)
        self.vx = uniform(-1, 1)
        self.vy = uniform(-1, 1)
        self.radius = randint(2, 4)
        self.color = (randint(200, 255), randint(100, 200), randint(200, 255))

    def update(self, mouse_pos):
        """Expression for swarm behavior"""
        mouse_x, mouse_y = mouse_pos
        
        # Calculate direction towards the mouse
        dir_x = mouse_x - self.x
        dir_y = mouse_y - self.y
        
        # Update velocity with acceleration and damping
        self.vx = (self.vx * PARTICLE_DAMPING) + (dir_x * PARTICLE_ACCELERATION)
        self.vy = (self.vy * PARTICLE_DAMPING) + (dir_y * PARTICLE_ACCELERATION)
        
        # Update position
        self.x += self.vx
        self.y += self.vy

        # Simple boundary check to keep particles on screen
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            self.reset()
            
    def reset(self):
        """Reset particle to a random position"""
        self.x = uniform(0, SCREEN_WIDTH)
        self.y = uniform(0, SCREEN_HEIGHT)
        self.vx = uniform(-1, 1)
        self.vy = uniform(-1, 1)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# --- Bubble Class for the Bubble Mass ---
class Bubble:
    def __init__(self):
        self.x = uniform(0, SCREEN_WIDTH)
        self.y = uniform(SCREEN_HEIGHT, SCREEN_HEIGHT + 100) # Start below the screen
        self.radius = randint(5, 25)
        
        # Expression parameters
        self.buoyancy = uniform(0.8, 2.5) # Upward speed
        self.wobble_amplitude = uniform(0.3, 1.0)
        self.wobble_frequency = uniform(0.01, 0.05)
        self.wobble_counter = 0

    def update(self):
        """Expression for bubble behavior"""
        self.wobble_counter += self.wobble_frequency
        
        # Update position with buoyancy and wobble
        self.y -= self.buoyancy
        wobble_x = sin(self.wobble_counter) * self.wobble_amplitude
        self.x += wobble_x
        
        # Reset bubble if it goes off the top of the screen
        if self.y < -self.radius * 2:
            self.reset()
            
    def reset(self):
        self.x = uniform(0, SCREEN_WIDTH)
        self.y = SCREEN_HEIGHT + self.radius
        
    def draw(self, surface):
        # Create a transparent surface for the bubble
        bubble_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(bubble_surface, BUBBLE_COLOR, (self.radius, self.radius), self.radius)
        # Add a "shine" effect
        pygame.draw.circle(bubble_surface, (255, 255, 255, 80), (self.radius*0.7, self.radius*0.7), self.radius//4)
        surface.blit(bubble_surface, (int(self.x - self.radius), int(self.y - self.radius)))


# --- Main Game Loop ---
def main():
    # Create lists to hold our objects
    particle_swarm = [Particle() for _ in range(NUM_PARTICLES)]
    bubble_mass = [Bubble() for _ in range(NUM_BUBBLES)]
    
    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == BUBBLE_SPAWN_EVENT:
                # Add a new bubble periodically, replacing an old one
                if bubble_mass:
                   bubble_mass.pop(0)
                bubble_mass.append(Bubble())

        # Get mouse position for swarm logic
        mouse_pos = pygame.mouse.get_pos()

        # --- Update all objects ---
        for particle in particle_swarm:
            particle.update(mouse_pos)
            
        for bubble in bubble_mass:
            bubble.update()

        # --- Drawing ---
        screen.fill(BLACK) # Background
        
        # Draw Bubbles (drawn first, so they are in the background)
        for bubble in bubble_mass:
            bubble.draw(screen)
            
        # Draw Particles
        for particle in particle_swarm:
            particle.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()