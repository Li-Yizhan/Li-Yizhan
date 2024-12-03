---
layout: default
title: Molecular Dynamics
parent: Scientific Computing
grand_parent: Science
nav_order: 4
---

# Molecular Dynamics

What is Molecular Dynamics?

With MD, one can simulate the dynamic movement, aggregation, reaction, folding, clustering, etc. of atoms, molecules, polymers, proteins, etc

- Represent atoms/particles as (charged or
uncharged) mass points
- Connect the particles with springs representing
chemical bonds ⇒ molecules, polymers
- Arrange them according to the molecular skeletal
structural formula
- Model particle interactions with a potential $U$
- Derive the particle forces $\vec{f_i} = −∇_i U$
- Move the particles through space with a
numerical time integration method (see L3)
- Break/build the bonds between atoms to model
chemical reactions
- Record quantities of interest: vibrations, reaction
rates, temperature, diffusion lengths, etc.

**Statistical Ensembles**

One can fix either volume $V$ or pressure $P$, either energy $E$ or temperature $T$ , either
particle number $N$ or chemical potential $μ$.

<figure>
    <div style="text-align:center;">
    <img src="/Images/StatisticalEnsembles.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.1: Statistical Ensenbles</figcaption>
</figure>

The easiest ensemble to simulate is the microcanonical ensemble (NVE ensemble):
- Use a fixed number of particles, $N$
- Use a fixed simulation box with volume $V = L^d$
I Use a symplectic integrator (semi-implicit Euler, Verlet, Velocity
Verlet, etc.) to move the particles
I Do not use any damping or friction (only conservative forces)
⇒ Energy $E$ is preserved

In experiments, one typically has a canonical ensemble (NVT ensemble):
- Use a fixed number of particles, $N$
- Use a fixed simulation box with volume $V = L^d$
- Integration method does not need to be symplectic
I Mechanism needed to keep the temperature $T$ fixed ⇒ heat bath

**Coarse-graining**

- Atomistic MD represents each atom by a point particle ⇒ very expensive
- Coarse-graining is a technique to reduce computational cost by representing groups of atoms by larger effective beads (“coarse grains”) with averaged properties
- Less particles ⇒ less computational cost (most MD simulations have $O(N)$ or
$O(N log N)$ complexity)
- Larger particles move & oscillate slower ⇒ larger timesteps possible

**Particle Interactions**

The interactions between the atoms/particles are modeled with different potentials

- Unbonded pair interactions
- 2-particle chemical bonds
- 3-particle angle potentials
4-particle torsion potentials (dihedral potentials)
- For large particles: rigid body collisions

**Unbonded particle Interaction**

Lennard-Jones Potential
- Phenomenological
- Models Van de Waals forces
- Attractive at large distance, repulsive at short distances

Potential energy:

$$
U_{LJ}(r) = 4\epsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^{6} \right]
$$

Two material parameters that depend on the two atoms:
- $\epsilon$: depth of the potential well
- $\sigma$: distance where $U_{LJ} = 0$

$r_{min} = 2^{1/6} \sigma ≈ 1.12 \sigma$ is the equilibrium particle distance

Equations for 3D scenario:

Lennard-Jones potential:
$$
U_{LJ}(r_{ij}) = 4\epsilon \left[ \left( \frac{\sigma}{r_{ij}} \right)^{12} - \left( \frac{\sigma}{r_{ij}} \right)^{6} \right]
$$

Resulting force:

$$
f(r_{ij}) = - \frac{dU_{LJ}}{dr_{ij}}(r_{ij}) \cdot dr_{ij} dx \cdot dy \cdot dz= \frac{24\epsilon}{r_{ij}} \left[ 2 \left( \frac{\sigma}{r_{ij}} \right)^{12} - \left( \frac{\sigma}{r_{ij}} \right)^{6} \right]
$$

<figure>
    <div style="text-align:center;">
    <img src="/Images/LennardJonesPotential.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.2: Lennard-Jones Potential</figcaption>
</figure>

**Bond Potentials**

Potential energy:

$$
U_{\text{bond}}(r_{ij}) = \frac{1}{2} k (r_{ij} - r_0)^2 \\
$$

Force:

$$
f(r_{ij}) = - \frac{dU_{\text{bond}}}{dr_{ij}} (r_{ij}) = -k (r_{ij} - r_0)
$$

Two material parameters that depend on the two atoms:
$k$ : bond spring constant
$r_0$: bond rest length

**Angle Potentials**

Potential energy:

$$
U_{\text{angle}}(\theta_{ijk}) = \frac{1}{2} k_{\theta} (\theta_{ijk} - \theta_0)^2
$$

Alternative model:

$$
U'_{\text{angle}}(\theta_{ijk}) = \frac{1}{2} k'_{\theta} (\cos \theta_{ijk} - \cos \theta_0)^2
$$

Two material parameters that depends on the three atoms:

$k_θ$: angle spring constant
$θ_0$: equilibrium angle

To get the force acting on the atoms ijk, one needs to write $\theta_{ijk}$ as a function of the atom positions, $θ_{ijk} (\vec{xi} , \vec{xj} , \vec{xk} )$, and then compute the derivative:

$$
\textcolor{red}{\vec{f}_i} = -\nabla_i U(\theta_{ijk}) = - \frac{d U_{\text{angle}} (\theta_{ijk})}{d \theta_{ijk}} \frac{d \theta_{ijk}}{d \vec{x}_i}
$$

**Dihedral Potentials**

Models torsion of the middle bond, measured by the angle $φ_{ijkl}$, spanned by the two planes going through the points ijk and jkl.

Potential energy:

$$
U_{\text{dih}}(\phi_{ijkl}) = \frac{1}{2} k_{\phi} \begin{cases}
1 + \cos(n \phi_{ijkl} - \phi_0), & n > 0 \\
(\phi_{ijkl} - \phi_0)^2, & n = 0
\end{cases}
$$

Three material parameters that depend on the four atoms:
$k_φ$ : angle spring constant
$φ_0$: phase shift, equilibrium angle
$n$ : number of periodic energy minima on a full turn

Total potential:

$$
U = \sum_{\text{pairs}} U_{LJ}(r_{ij}) + \sum_{\text{bonds}} U_{\text{bond}}(r_{ij}) + \sum_{\text{angles}} U_{\text{angle}}(\theta_{ijk}) + \sum_{\text{dihedra}} U_{\text{dih}}(\phi_{ijkl}) + \dots
$$

**Reduced Unites**

Dimensional Analysis:

All quantities $Q$ in basic classical MD simulations have units: $[Q] = kg^α m^β s^γ$

Examples:

Velocity $[v] = m/s$ ⇒ $\alpha = 0,  \beta = 1, \gamma = -1$

Reduced units:
- Define a reference value for 3 quantities with independent units
- Express all simulation variables in these units
- Choose quantities that make your life as easy as possible
- For Lennard–Jones potential:$ m = 1, \epsilon = 1, σ = 1$

Pros: 
- Simpler and faster code (Example: m = 1 makes acceleration and force equal)
- Sometimes easier to interpret the simulation results (“nice” numbers)
- Reuse one simulation for different conditions: rescale all output according to units

Con:
- Can make the code harder to read

<figure>
    <div style="text-align:center;">
    <img src="/Images/ReducedUnitsLennard.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.2: Reduced Units for Lennard-Jones Potential</figcaption>
</figure>

- Typical simulation timescale: Picoseconds $(10^{−12} s)$
- Typical simulation timestep size for atomistic MD: Femtoseconds $(10^{−15} s)$
- In reduced units, $m = 1, σ = 1, \epsilon = 1$, all these reference quantities are 1

Example: Simulate in reduced units, measure particle velocity. To convert the simulation
output to real velocity, multiply the measured value by 157 $m/s$.

**Boundary Conditions**

One always has to choose a suitable boundary condition (BC). What do you want to do?

Mimic a large volume (gas, liquid, etc.) with a finite (small) box
⇒ Periodic boundary conditions

Simulate bounce-off from walls (pressure)
⇒ Rigid walls (fixed BC)

Simulate open space
⇒ No boundary conditions needed

**Periodic Boundary Conditions**
- Used to model a (infinitely) large system with minimal boundary effects
- Allows to mimic a huge ensemble with just some
- 100–1000 particles
- When a particle leaves the box on one side, it re-enters on the other side
- Check each side ($2d$ times for a box in $d$ dimensions) 
- Calculating distances between particles is a bit more complicated

<figure>
    <div style="text-align:center;">
    <img src="/Images/PeriodicBoundary.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.3: Periodic Boundary</figcaption>
</figure>

Method 1: Restrict particle coodrinates to the simulation box

Minimum image convention:

For the particle distance calculation, use the copy (“image”) of the particle that is the closest

Method 2: Do not restrict the particle coordinates
- No copies of particles needed
- PBCs with the minimum image convention can be implemented in 1 line of code for each dimension

Advantage: measurement of full trajectories (for diffusion length etc.)

Drawback: When visualizing the particles, they need to be placed back in the box anyway

**Fixed Boundary Conditions (Rigit Walls)**
- Used to model a finite container
- Simplest way: penalty method. If the particle flies outside the container, apply a force pushing it back in
- The repulsive force must be perpendicular to the wall
- Repeat for each wall (2d times for box in d dim.)
- Example: If $y_i > L_y$ , apply $\vec{f_i}^{wall} = \begin{bmatrix}
0 \\
-k(y_i - L_y)
\end{bmatrix}$
- Drawback: additional spring parameter $k$
- Large $k$ ⇒ small timestep $h ∝ \sqrt{m/k}$

Alternative: Event-driven time integration
- When a particle leaves the box, partially undo the timestep (for all particles) to when
the one particle is exactly at the wall
- Flip the sign of the y-coordinate of the particle’s velocity ⇒ it bounces off

Fixed boundary conditions (immobile particles)
- Replace smooth walls by immobile particles
- Normal force calculation, just don't move the boundary particles
- Advantage: less artificial / more realistic in some cases
- Drawback: More complicated to set up

**Other Boundary Conditions**

Mixed BCs: walls & periodic

Moving periodic BCs for shear flow

**Initial Condition**

A MD simulation is an initial value problem (IVP) ⇒ initial condition needed

Particles at rest, only potential energy
- Placement of particles: random or regular grid
- All particles at rest (zero initial velocity)
- Control energy by how far apart the particles are
- Problem: particles can be very close ⇒ huge forces, only
dilute systems feasible

Particles perfectly aligned, only kinetic energy
- Placement of particles: triangular grid with $r = r_{min} = 2^{1/6}σ$
- Random initial velocity (magnitude & direction): 

$$
\vec{v}_i = \nu \begin{bmatrix}
\cos \theta \\
\sin \theta
\end{bmatrix} \text{ in 2D} \quad
\vec{v}_i = \nu \begin{bmatrix}
\sqrt{1 - u^2} \cos \theta \\
\sqrt{1 - u^2} \sin \theta \\
u
\end{bmatrix} \text{ in 3D} \\
\theta ∼  U([0, s\pi]), u ∼  U([0,1]), v ∼  \text{Maxwell-Boltzmann}
$$
- Control energy by initial speed

**Particle collisions (soft spheres)**
- Mostly relevant for large particles ($ \geq 100 nm$, macro-molecules, granular materials)
- Meso- or macroscopic steric interaction / volumetric exclusion
- Particles with a radius $R$ (not point-like)
- Penalty method analogous to collision with walls
- Spring constant $k$ and exponent $α$ depend on the material and shape
- For spheres, $α = 1$ (Hertz, 1881)

**Spatial Partitioning**

- Computing all particle pair interactions is an
$O(N^2)$ operation
- By far the most expensive part of the simulation for large $N$
- Everything else is much faster: $O(N)$
- With $O(N2^)$, simulating more that $N ≈ 10^3$ particles becomes unfeasible

How to make MD simulations more efficient?
- Many interaction potentials are short-ranged, i.e., the force is almost zero for two distant particles
- Lennard-Jones potential: $f ≈ 0$ for $r \geq 2.5σ$
- Idea: Restrict particle interaction to the local
neighborhood $(r < 2.5σ)$
- But how to find all nearby particles efficiently?

Spatial Partitioning
- Divide the simulation volume into
boxes (“cells”)
- Each box stores a list of contained
particles
- Optimum box size = interaction
potential cutoff $(2.5σ)$
- All particles interacting with the red one are in the gray boxes
- There are $3^d$ boxes to test in $d$
dimensions
- If the particle density $ρ = N/V$ is constant, each box contains on
average $M = ρ(2.5σ)^d$ particles
- Complexity reduction from $O(N^2)$ to $O(N3^d M) = O(N)$

Efficient Implementation with lined cell lists
- Store in a list first of length $N_{cells}^d$ for each cell the index of the first particle in it
- If no particle is in cell $k$, set first[k] = -1
- In a second list next of length $N$, store for each particle $i$ the index of the next particle
in the same cell.
- For the last particle in a cell, set next[i] = -1

In practice, the cells do not need to store a list of particles! This is important, because:
- The number of particles per cell varies over time
- Clearing and reallocating memory for a list of particles in each cell would be very
expensive (slow)

Updating linked cell lists:
- In each timestep, one needs to either:
    1. rebuild the linked cell lists, or:
    2. update the existing one for each particle that moves from one cell to another
- Advanced method:
    - Use slightly larger cells (size 2.5σ + δ)
    - Rebuild the linked cell lists only when the fastest-moving particle has traveled a cumulative distance of δ/2 since the last rebuild
    - Can be more efficient in practice

Careful with simulation box boundaries:

For wall boundaries with the penalty
method, particles can slightly leave the simulation frame
- add an extra layer of cells around it
- For periodic boundaries, one also needs to check the boxes on the other side(s):

**Spatial Partitioning with Periodic Boundaries**

**Energy and Temperature**
How to measure energy and temperature in a MD simulation?

Potential energy
$$
U = \sum_{\text{pairs}} U_{LJ}(r_{ij}) + \sum_{\text{bonds}} U_{\text{bond}}(r_{ij}) + \sum_{\text{angles}} U_{\text{angle}}(\theta_{ijk}) + \sum_{\text{dihedra}} U_{\text{dih}}(\phi_{ijkl}) + \dots
$$

Kinetic energy:
$$
K = \frac{1}{2} \sum_{i=1}^{N} m_i \| \vec{v}_i \|^2
$$

Equipartition theorem of thermodynamics ⇒ Temperature of a particle system:

$$
T = \frac{2K}{k_B d (N - 1)}
$$

$k_B$: Boltzmann constant (1.380649 × 10−23 J/K)
$d$: Dimensionality of the system (1, 2, 3, ...)

The factor N-1 (instead of N) excludes rigid body movement of the simulation box. 

**Canonical Ensemble**
How to control the temperature?
- Until now we considered constant energy $E = U + K$ (microcanonical ensemble)
- Most experiments are performed at constant temperature $T$ (canonical ensemble)
- ⇒ The system is coupled to a “heat bath” with regulated temperature

Computational methods to simulate this:
- Velocity rescaling
- Nosé–Hoover thermostat
- Constraint method (not discussed here)

**Velocity rescaling**

n each timesteps, scale all particle velocities by the same factor:

$$
\vec{v}_i \gets \sqrt{\frac{T_{\text{target}}}{T_{\text{measured}}}} \vec{v}_i
$$

After this, $T_{target} = T_{measured}$

Pros: Very simple, can be used to initialize the simulation (start with a desired temperature)
Con: Modifies the velocity distribution (Maxwell–Boltzmann for an ideal gas) ⇒ wrong thermodynamic behavior

**Nosé–Hoover thermostat**

Provably the only method with a single “friction” parameter that gives the correct velocity distribution (Hoover, 1985).

Introduce a new degree of freedom, the friction parameter ξ (SI unit: $s^{−1}$).

One then needs to solve a modified ensemble, which is provably canonical:

$$
\ddot{\vec{x}}_i = \frac{1}{m_i} \vec{f}_i - \xi \dot{\vec{x}}_i \quad \text{for} \quad i = 1, \ldots, N
$$

$$
Q \ddot{\xi} = 2K - ((N-1)d + 1) k_B T_{\text{target}} \quad \text{with} \quad K = \frac{1}{2} \sum_{i=1}^{N} m_i \dot{\vec{x}}_i^2
$$

- d:Dimensionality of the system
!: "thermal inertia," needs to be chosen empirically
    - $$ too large ⇒ equilibration to T_{target} is too slow
    - $Q$ too small ⇒ temperature oscillates unrealistically

$Q$ must be found such that $\text{stddev}(T_{\text{measured}}) = \sqrt{\frac{2}{Nd} T_{\text{target}}}$

### Summary:

1. Particle systems are classified into different statistical ensembles
2. Molecular dynamics simulations can be atomistic or coarse-grained
3. The Lennard–Jones potential phenomenologically describes electronically neutral atoms or molecules. The parameters $\epsilon$ and $σ$ depend on the substance.
4. Use a symplectic time integrator to move the particles without energy drift (microcanonical ensemble)
5. With bond and angle constraints, one can model large molecular structures
6. The choice of boundary conditions is important! PBCs mimic an infinite system.
7. Spatial partitioning reduces the computational cost in short-range particle interactions
8. MD simulations at constant temperature require a heat bath (not trivial!)