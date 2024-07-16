---
layout: default
title: Mass-spring System and Time Propagation
parent: ScientificComputing
grand_parent: Science
nav_order: 3
---

# Mass-spring System and Time Propagation

**Simulation Techniques**
- Grid-based Methods
    - Numerical quadrature, fluid dynamics, partial differential equations
- Rigid Body Simulations
    - Furniture, collapse, video games, etc.
- Particle Systems
    - Gases, fluids, molecules, proteins, granular materials (sand), cosmology, etc.
- Mass-spring Systems
    - Deformable objects, elastics (cells, tissues,
bridges, car crashes, etc.)

**Steps of Numerical Modeling**

1. What can I use as input, what would I like to get as output?
    - Cell material properties, initial shape, growth law → cancer shape over time
2. What are the physical equations or laws that govern the system?
    - Diffusion equation, Newton’s second law, etc.
3. Are there symmetries that can be exploited?
    - 3D vs. 2D, Cartesian vs. polar coordinates, etc.
4. What are the degrees of freedom (DOF)?
    - Particle positions, rotation, concentrations, temperature, etc.
5. How many resources are available?
    - Development effort, simulation runtime, computer power
6. Which numerical method is best suited?
    - Continuum vs. particle-based, simple vs. complex
7. Which software tools are available?
    - Existing software vs. own implementation
8. What is the required precision?
    - Error tolerance, grid resolution, particle number etc

## Mass-spring systems & Newtonian dynamics

### A simple way to model elastic objects

### Contact mechanics

### Damping

## Time propagation

### How to evolve a Newtonian system in time

### Euler methods, Heun’s method, Runge–Kutta methods, Verlet methods

### Numerical stability

### Stiffness of an equation

### Explicit vs. implicit integration

### Symplectic integrators