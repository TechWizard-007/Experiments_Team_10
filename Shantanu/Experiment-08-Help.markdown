# Help Document for Experiment-08.py

## Overview
This Python script, `Experiment-08.py`, uses the Pygame library to create a visual simulation featuring two main elements: a **particle swarm** and a **bubble mass**. The particle swarm consists of particles that are attracted to the mouse cursor, while the bubble mass consists of bubbles that rise from the bottom of the screen with a wobbling motion. This document provides an explanation of the script's functionality, how to run it, and how to interact with the simulation.

## Prerequisites
To run this script, you need:
- **Python 3.x** installed on your system.
- **Pygame library** installed. You can install it using pip:
  ```bash
  pip install pygame
  ```
- A basic understanding of Python and Pygame for modifications (optional).

## How to Run
1. Save the script as `Experiment-08.py`.
2. Ensure Pygame is installed (see Prerequisites).
3. Run the script using Python:
   ```bash
   python Experiment-08.py
   ```
4. A window will open displaying the simulation. Move your mouse to interact with the particle swarm. Close the window or press `Ctrl+C` in the terminal to exit.

## Simulation Components

### 1. Particle Swarm
- **Description**: A group of 300 particles that move towards the mouse cursor with a smooth, damped motion.
- **Behavior**:
  - Each particle is attracted to the mouse position with a small acceleration (`PARTICLE_ACCELERATION = 0.01`).
  - Particle motion is damped (`PARTICLE_DAMPING = 0.97`) to simulate friction or air resistance, preventing excessive speed.
  - If a particle moves off the screen, it resets to a random position with a small random velocity.
- **Visuals**: Particles are small circles (radius 2–4 pixels) with random pastel colors.
- **Interaction**: Move the mouse cursor to guide the swarm. The particles will follow the cursor dynamically.

### 2. Bubble Mass
- **Description**: A collection of 50 bubbles that rise from the bottom of the screen, wobbling as they ascend.
- **Behavior**:
  - Bubbles spawn at the bottom of the screen and move upward with a buoyancy speed (randomly between 0.8 and 2.5 pixels per frame).
  - Each bubble has a wobbling motion, controlled by a sine function with random amplitude (0.3–1.0) and frequency (0.01–0.05).
  - When a bubble moves off the top of the screen, it resets to a new position at the bottom.
  - A new bubble is spawned every 100ms, replacing the oldest bubble to maintain a constant number of bubbles.
- **Visuals**: Bubbles are semi-transparent circles (radius 5–25 pixels) with a light blue color (`BUBBLE_COLOR = (180, 220, 255, 50)`) and a white "shine" effect for a glossy appearance.

## Controls
- **Mouse Movement**: Move the mouse cursor to direct the particle swarm.
- **Quit**: Click the window's close button or press `Ctrl+C` in the terminal to exit the simulation.

## Code Structure
- **Initialization**: Sets up Pygame, the screen (1200x800 pixels), and a clock for 60 FPS.
- **Constants**:
  - `SCREEN_WIDTH`, `SCREEN_HEIGHT`: Window dimensions.
  - `FPS`: Frames per second (60).
  - `NUM_PARTICLES`: Number of particles (300).
  - `NUM_BUBBLES`: Number of bubbles (50).
  - `PARTICLE_ACCELERATION`, `PARTICLE_DAMPING`: Control particle movement.
  - `BUBBLE_SPAWN_EVENT`: Custom Pygame event to spawn new bubbles every 100ms.
- **Classes**:
  - `Particle`: Defines particle properties (position, velocity, radius, color) and behavior (movement towards mouse, damping, boundary reset).
  - `Bubble`: Defines bubble properties (position, radius, buoyancy, wobble parameters) and behavior (upward movement, wobbling, reset).
- **Main Loop**:
  - Handles events (quit, bubble spawn).
  - Updates particle and bubble positions.
  - Draws the background (black), bubbles, and particles.
  - Updates the display and caps the frame rate.

## Customization Ideas
- **Change Particle Count**: Modify `NUM_PARTICLES` to increase or decrease the number of particles.
- **Adjust Particle Behavior**: Tweak `PARTICLE_ACCELERATION` or `PARTICLE_DAMPING` for faster/slower or smoother/sharper movement.
- **Bubble Frequency**: Change the timer for `BUBBLE_SPAWN_EVENT` (e.g., `pygame.time.set_timer(BUBBLE_SPAWN_EVENT, 50)` for faster spawning).
- **Bubble Appearance**: Adjust `BUBBLE_COLOR` or the radius range in the `Bubble` class for different visual effects.
- **Add Interactions**: Introduce collisions between particles and bubbles or add keyboard controls for additional effects.

## Troubleshooting
- **Pygame Not Found**: Ensure Pygame is installed (`pip install pygame`).
- **Window Not Opening**: Check for errors in the terminal. Ensure Python and Pygame are correctly installed.
- **Performance Issues**: Reduce `NUM_PARTICLES` or `NUM_BUBBLES` if the simulation lags on slower systems.
- **No Mouse Interaction**: Verify that the mouse is within the Pygame window, as particles follow the cursor’s position.

## Notes
- The simulation is purely visual and interactive, designed to demonstrate particle and bubble dynamics.
- The script uses RGBA colors for transparency in bubbles, which requires a Pygame surface with `pygame.SRCALPHA`.
- The particle swarm and bubble mass run independently, with particles drawn over bubbles for visual layering.

For further questions or modifications, feel free to experiment with the code or ask for assistance!