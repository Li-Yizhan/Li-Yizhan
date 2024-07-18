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



