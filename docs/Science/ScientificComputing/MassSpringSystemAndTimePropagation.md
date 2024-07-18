---
layout: default
title: Mass-spring System and Time Propagation
parent: Scientific Computing
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

**Mass-Point System**
- Systems with inherently localized masses
    - gases, galaxies, sand, ...
- Discretization of an object into a collection of mass points
    - elastic objects, inelastic objects
- Interaction between pairs of mass points $i \neq j$ based on internal forces $\vec{f}_{ij}^{int}$
- All other forces acting on point $i$ are external forces $\vec{f}_{i}^{ext}$
    - Gravity, external fields, contact with walls, etc
- Total force acting on point $i$: $\vec{f_i} = \vec{f}_{i}^{ext} + \sum_{j\neq i} \vec{f}_{ij}^{int}$
- Internal forces are symmetric: $\vec{f}_{ij}^{int} = -\vec{f}_{ij}^{int}$, therefore: $\sum_i \sum_j \vec{f}_{ij}^{int} = \vec{0}$

**Mass-Spring Systems**
- Representation of internal forces with springs
    - elastic forces, inelastic forces, internal contact forces, ...
- Typically only between nearby mass point pairs (short-range forces)

**Elastic Spring Force**
- Spring constant: $k$ (stiffness)
- Initial spring length: $L$ (rest length)
- Current spring length: $l$ (deformed length)

Hooke's Law (linear force):

$$
f = -k(l-L)
$$

>**Definition: Elasticity**
The ability of an object to resist an applied force $(k > 0)$ and to return to its original size and shape when it is removed again $(l → L$ when $f → 0)$.

- A simple mechanism to model internal forces $\vec{f_{ij}^{int}}$
- Springs can also be non-linear (Example: $f = −k(l/L − 1)β $)

**Elastic Spring Force**

Elastic springs can also be formulated via their potential energy:
$$
U = \frac{1}{2} k (l - L)^2
$$

The force is the negative derivative w.r.t. the DOF $I$:

$$
f = -\frac{dU}{dl} = -k(l - L)
$$

The elastic energy is the negative integrated force:

$$
U = -\int_{L}^{l} f \, dl = \frac{1}{2} k (l - L)^2
$$

In vector form (in any dimension, 2D, 3D, etc):
$$
\vec{f} = -k(l - L) \vec{n} \quad \text{where} \quad \vec{n} = \frac{\vec{x}_i - \vec{x}_j}{\|\vec{x}_i - \vec{x}_j\|}
$$

**Elastic Spring Force Networks**

How to assemble forces on mass points?

Total internal force $\vec{f}_0^{int}$ on a mass point is the sum of all
incident spring forces:

$$
\vec{f}^{\text{int}}_0 = - \sum_{j=1,2,3} k_j (l_j - L_j) \frac{\vec{x}_0 - \vec{x}_j}{l_j}, \quad l_j = \|\vec{x}_0 - \vec{x}_j\|
$$

External forces $\vec{f}^ext$:
- Gravity
- Contact forces
- External fields (magnetic, electric, etc.)
- Drag (air resistance, fluid advection etc.)
- Anything not represented by internal springs

Total force on mass point $i$: $\vec{f_i} = \vec{f}_i^{int} + \vec{f}_i^{ext}$ 
Total internal energy = sum of all spring energies

### Damping

**Viscous Forces and Damping**

Elastic spring forces are conservative forces:
- They are the negative derivative of a potential energy: 
$$
\vec{f}^{\text{int}}_i = - \nabla_i U = - 
\begin{bmatrix}
\partial U/\partial x_i \\
\partial U/\partial y_i \\
\partial U/\partial z_i
\end{bmatrix}
$$
- They can only depend on positions $\vec{x_i}(t)$, not on velocities $\vec{v_i}(t) = \frac{d \vec{x_i}}{dt}(t)$

With only conservative forces, spring networks would never stop oscillating. 

Examples of non-conservative forces:
- Viscous damping: $\vec{f}^{\text{ext}}_i(t) = -\gamma \cdot \vec{v}_i(t)$ with viscous damping coefficient $γ ≥ 0$
- Dynamic friction: $\vec{f}^{\text{ext}}_i(t) \propto -\frac{\vec{v}_i(t)}{\|\vec{v}_i(t)\|}$ (opposite to velocity, but independent of speed)
- Drag (e.g., air resistance): $\vec{f}^{\text{ext}}_i(t) \propto -\|\vec{v}_i(t)\| \cdot \vec{v}_i(t)$ (proportional to $−v^2$)

**Equations of motion**

Newton's 2nd law for one mass point (3 equations):

$$
m_i \frac{d^2 \vec{x}_i}{dt^2}(t) = \vec{f}_i, \quad \vec{x}_i = 
\begin{bmatrix}
x_i \\
y_i \\
z_i
\end{bmatrix}, \quad \vec{f}_i = 
\begin{bmatrix}
f_{x,i} \\
f_{y,i} \\
f_{z,i}
\end{bmatrix}
$$

Newton's 2nd law for $N$ mass points (3N equations)

$$
\mathbf{M} \frac{d^2 \vec{X}}{dt^2}(t) = \vec{F}, \quad \mathbf{M} = 
\begin{bmatrix}
m_1 & & & \\
& m_1 & & \\
& & \ddots & \\
& & & m_N
\end{bmatrix}, \quad \vec{X} = 
\begin{bmatrix}
x_1 \\
y_1 \\
z_1 \\
\vdots \\
x_N \\
y_N \\
z_N
\end{bmatrix}, \quad \vec{F} = 
\begin{bmatrix}
f_{x,1} \\
f_{y,1} \\
f_{z,1} \\
\vdots \\
f_{x,N} \\
f_{y,N} \\
f_{z,N}
\end{bmatrix}
$$

$M$ is called the mass matrix

**Equations of Motion with Damping**

Newton's 2nd law for $N$ mass points with viscous damping

$$
\mathbf{M} \frac{d^2 \vec{X}}{dt^2}(t) + \mathbf{D} \frac{d \vec{X}}{dt}(t) = \vec{F}
$$

$D$ is called the damping matrix. 

Simplest form: $D = γ I$ where $γ \geq 0$ is the viscous damping coefficient

$$
\mathbf{D} = 
\begin{bmatrix}
\gamma & & & \\
& \gamma & & \\
& & \ddots & \\
& & & \gamma
\end{bmatrix}
$$

There are more advanved ways of building $D$. 

### Implementation

There are two ways of representing mass-spring networks in program code:

**Method 1: Object-oriented way (grouped by points and springs)**

<figure>
    <div style="text-align:center;">
    <img src="/Images/ObjectOrientMassSpringNetwork.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.1: Object-oriented Method</figcaption>
</figure>

Computation of Forces:
<figure>
    <div style="text-align:center;">
    <img src="/Images/ForceComputationMethod1.png" alt="Trapezoidal Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.2: Object-oriented Method Force Computation</figcaption>
</figure>

**Array-oriented way (grouped by variables)**

<figure>
    <div style="text-align:center;">
    <img src="/Images/ArrayOrientMassSpringNetwork.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.3: Array-oriented Method</figcaption>
</figure>

<figure>
    <div style="text-align:center;">
    <img src="/Images/ForceComputationMethod2.png" alt="Trapezoidal Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.4: Array-oriented Method Force Computation</figcaption>
</figure>

Both methods have their advantages and disadvantages

**Solution of mass-spring system**

General form of the equations of motion:

$$
\mathbf{M} \frac{d^2 \vec{X}}{dt^2}(t) + \mathbf{D} \frac{d \vec{X}}{dt}(t) = \vec{F} \left( t, \vec{X}(t), \frac{d \vec{X}}{dt} \right)
$$

- $M$ is the mass matrix
- $X(t)$ is the position vector as a function of time
- $\frac{d \vec{X}}{dt}$ is the velocity vector as a function of time
- $\frac{d^2 \vec{X}}{dt^2}(t)$ is the acceleration vector as a function of time
- $D$ is the damping matrix
- $\vec{F} \left( t, \vec{X}(t), \frac{d \vec{X}}{dt} \right)$ is the external force vector as a function of time, position, and velocity. 

Simple form for one mass point:

$$
m \frac{d^2 \vec{x}}{dt^2}(t) + \gamma \frac{d \vec{x}}{dt}(t) = \vec{f} \left( t, \vec{x}(t), \frac{d \vec{x}}{dt} \right)
$$

We have $\vec{x}(t_0), \vec{v}(t_0)$, we want: $\vec{x}(t)$ and $\vec{v}(t) = \frac{d \vec{x}}{dt}(t)$

$$
\frac{d^2 \vec{X}}{dt^2}(t) = \mathbf{M}^{-1} \left( \vec{F} \left( t, \vec{X}(t), \frac{d \vec{X}}{dt} \right) - \mathbf{D} \frac{d \vec{X}}{dt}(t) \right)
$$

$$
\frac{d^2 \vec{x}}{dt^2}(t) = \frac{1}{m} \left( \vec{f} \left( t, \vec{x}(t), \frac{d \vec{x}}{dt} \right) - \frac{\gamma}{m} \frac{d \vec{x}}{dt}(t) \right)
$$

Remember from Lecture 1: Computers are finite state machines, but the sought function $x(t)$ is infinite-dimensional!

Solution: Discretize time into finite timesteps $h$:

| \( t \)  | \( t_0 \)        | \( t_1 = t_0 + h \) | \( t_2 = t_0 + 2h \) | \( t_3 = t_0 + 3h \) |
|----------|------------------|---------------------|----------------------|----------------------|
| \( x(t) \) | \( x_0 = x(t_0) \) | \( x_1 \approx x(t_1) \) | \( x_2 \approx x(t_2) \) | \( x_3 \approx x(t_3) \) |

- The time series $x_n, n = 0,, 1, \ldots, N$ is a finite-dimensional approximation to $x(t)$
- There are numerous different methods to find the new position $x_{n+1}$ from the previous ones $x_n, x_{n−1}$ etc., the velocities $v_n, v_{n−1}$ etc., and forces f_n, f_{n−1} etc.
- Many names: “Time propagation methods”, “ODE integration methods”, “ODE
solvers”, “IVP (Initial Value Problem) solvers” ...

**Method 1: Forward Euler Method**


The simplest possible method. Idea: Taylo-expand the solution

$$
\begin{align*}
x(t_0 + h) &= x(t_0) + h \cdot x'(t_0) + \frac{h^2}{2} x''(t_0) + \dots \\
           &= x(t_0) + h \cdot x'(t_0) + \mathcal{O}(h^2) \\
           &\approx x(t_0) + h \cdot x'(t_0)
\end{align*}
$$

Forward Euler method: $x_{n+1} = x_n + h \cdot v_n$

- Error in each step: $O(h^2)$ ("local error")
- To integrate over a time period $T$, $N = T/h$ steps are required. 
- Endpoint after $N$ steps: $x(T) = x_N + O(Nh^2) = x_N + O(h)$
- The "global error" is $O(h)$
- The forward Euler method is therefore called a 1st-order method. 

<figure>
    <div style="text-align:center;">
    <img src="/Images/ForwardEulerMethodVisualInterpretation.png" alt="Trapezoidal Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.5: Forward Euler Method Visual Interpretation</figcaption>
</figure>

- Make a straight step forward in direction of the current derivative
- Compute the new derivative, and make another straight step in that direction
- The smaller h, the better the approximation

Problem: We still need the velocity $v_n$. From Newton’s equation of motion, we only have the acceleration $a_n = f_n/m$.

$$
\begin{align*}
a_n &= \frac{f(x_n, v_n, t_n)}{m} \\
x_{n+1} &= x_n + h \cdot v_n \\
v_{n+1} &= v_n + h \cdot a_n \\
t_{n+1} &= t_n + h
\end{align*}
$$

<figure>
    <div style="text-align:center;">
    <img src="/Images/ForwardEulerAlgorithm.png" alt="Trapezoidal Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.5: Forward Euler Method Algorithmn</figcaption>
</figure>

All forces are first calculated, before the positions and velocities are updated, such that all
forces use the same information ⇒ 2 loops over all mass points in step 3!

**Mass-spring models (A simple example)**

An Oscillating Point Mass ("Harmonic Oscillator")

- Point-like mass $m$
- Hookean spring (stiffness $k$, rest length $L$)
- Gravitational acceleration $g$

Modeling steps:
- Input: $m, k, L, g,$ initial position $z(0)$, initial velocity $v (0)$
- Output: Oscillation $z(t)$
- Physical laws: 
    - Newton’s 2nd law of motion: $f (t) = m · a(t)$
    - Hooke’s law for springs $f_s(t) = −k · (z(t) + L)$
    - Gravity $f_g(t) = −m · g$
- Symmetries/simplifications: Only vertical translation
- Degrees of freedom: $z$

Putting all forces together:

$$
m \cdot a(t) = \sum_i f_i = f_s + f_g = -k \cdot (z(t) + L) - m \cdot g
$$

That's a 2nd-order ordinary differential equation (ODE)
- Vertical acceleration: 
$a(t) = \frac{dv}{dt}(t) = \frac{d^2 z}{dt^2}(t)$
- Vertical velocity
$v(t) = \frac{dz}{dt}(t)$

For each order of the ODE, we need one initial condition (here: 2)

$$
z(0) = z_0 \quad v(0) = v_0
$$

Such a problem is called an initial-value problem (IVP)

<figure>
    <div style="text-align:center;">
    <img src="/Images/ForwardEulerDisad.png" alt="Trapezoidal Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.5: Forward Euler Method Inaccuracy</figcaption>
</figure>

$$
\begin{align*}
z(t + h) &= z(t) + h \cdot v(t) + \mathcal{O}(h^2) \\
v(t + h) &= v(t) + h \cdot a(t) + \mathcal{O}(h^2)
\end{align*}
$$

- Numerical IVP solvers are inaccurate
- Inaccuracy can lead to instability
- With forward Euler integration, very small timesteps are needed for stability

**Method 2: Midpoint method (Runge-Kutta 2, RK2)**

<figure>
    <div style="text-align:center;">
    <img src="/Images/MidpointMethod.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.6: Midpoint Method</figcaption>
</figure>

- Make a forward Euler step with half length $h/2$ to the midpoint
- Compute the derivative at the midpoint
- From the starting point, make a full step forward with the derivative at the midpoint

Properties of the midpoint method:

Pros:
- Local error is $O(h^3)$, global error is $O(h^2)$ (it is a 2nd-order method)
- More stable than forward Euler, larger timesteps possible
Con:
- Two evaluations of the derivative needed per step

Midpoint Method for a 1st-order ODE:

$$
\begin{align*}
&\frac{dx}{dt}(t) = g(x(t), t) \\
&k_1 = g(x_n, t_n) \\
&x_{n+1/2} = x_n + h/2 \cdot k_1 \\
&t_{n+1/2} = t_n + h/2 \\
&k_2 = g(x_{n+1/2}, t_{n+1/2}) \\
&x_{n+1} = x_n + h \cdot k_2 \\
&t_{n+1} = t_n + h
\end{align*}
$$

For Newton's equation of motion:
$$
\begin{align*}
&a_n = \frac{f(x_n, v_n, t_n)}{m} \\
&x_{n+1/2} = x_n + h/2 \cdot v_n \\
&v_{n+1/2} = v_n + h/2 \cdot a_n \\
&t_{n+1/2} = t_n + h/2 \\
&a_{n+1/2} = \frac{f(x_{n+1/2}, v_{n+1/2}, t_{n+1/2})}{m} \\
&x_{n+1} = x_n + h \cdot v_{n+1/2} \\
&v_{n+1} = v_n + h \cdot a_{n+1/2} \\
&t_{n+1} = t_n + h
\end{align*}
$$

**Heun's Method**

<figure>
    <div style="text-align:center;">
    <img src="/Images/HeunMethod.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.7: Heun's Method</figcaption>
</figure>

- Make a full forward Euler step
- Compute the derivative at the endpoint
- From the starting point, make a full step forward with the average derivative

Properties of the Heun's method:

Pros:
- Local error is $O(h^3)$, global error is $O(h^2)$ (it is a 2nd-order method)
- Very similar to the midpoint method (RK2)
Con:
- Two evaluations of the derivative needed per step

$$
\begin{align*}
\frac{dx}{dt}(t) &= g(x(t), t) \\
k_1 &= g(x_n, t_n) \\
\tilde{x}_{n+1} &= x_n + h \cdot k_1 \\
k_2 &= g(\tilde{x}_{n+1}, t_{n+1}) \\
x_{n+1} &= x_n + \frac{h}{2}(k_1 + k_2)
\end{align*}
$$

**Method 4: 4th-order Runge-Kutta Method (Runge-Kutta Method, RK4)**

<figure>
    <div style="text-align:center;">
    <img src="/Images/RungeKuttaMethod.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.8: Runge-Kutta Method</figcaption>
</figure>

RK4 for a 1st-order ODE:

$$
\begin{align*}
\frac{dx}{dt}(t) &= g(x(t), t) \\
\textcolor{red}{k_1} &= g(x_n, t_n) \\
\textcolor{red}{k_2} &= g(x_n + \frac{h}{2} \cdot \textcolor{red}{k_1}, t_n + \frac{h}{2}) \\
\textcolor{red}{k_3} &= g(x_n + \frac{h}{2} \cdot \textcolor{red}{k_2}, t_n + \frac{h}{2}) \\
\textcolor{red}{k_4} &= g(x_n + h \cdot \textcolor{red}{k_3}, t_n + h) \\
x_{n+1} &= x_n + \frac{h}{6} (\textcolor{red}{k_1} + 2\textcolor{red}{k_2} + 2\textcolor{red}{k_3} + \textcolor{red}{k_4})
\end{align*}
$$

- The derivative is computed at the beginning, in two different ways in the middle, and again at the end
- The solution at the end is a full forward step with weighted derivatives
- The two derivatives in the middle have twice the weight of the endpoint derivatives

**Properties of Runge–Kutta 4**

Pros:
- Local error is O(h5), global error is O(h4) (it is a 4th-order method)
- Very precise, even larger timesteps possible

Cons:
- Four evaluations of the derivative (the force) needed per step

$$
\begin{align*}
\textcolor{magenta}{w_1} &= v_n \\
\textcolor{blue}{a_1} &= a(x_n, v_n, t_n) \\
\textcolor{magenta}{w_2} &= v_n + \frac{h}{2} \cdot \textcolor{blue}{a_1} \\
\textcolor{blue}{a_2} &= a \left( x_n + \frac{h}{2} \cdot \textcolor{magenta}{w_1}, v_2, t_n + \frac{h}{2} \right) \\
\textcolor{magenta}{w_3} &= v_n + \frac{h}{2} \cdot \textcolor{blue}{a_2} \\
\textcolor{blue}{a_3} &= a \left( x_n + \frac{h}{2} \cdot \textcolor{magenta}{w_3}, v_3, t_n + \frac{h}{2} \right) \\
\textcolor{magenta}{w_4} &= v_n + h \cdot \textcolor{blue}{a_3} \\
\textcolor{blue}{a_4} &= a (x_n + h \cdot \textcolor{magenta}{w_4}, v_4, t_n + h) \\
x_{n+1} &= x_n + \frac{h}{6} \left( \textcolor{magenta}{w_1} + 2\textcolor{magenta}{w_2} + 2\textcolor{magenta}{w_3} + \textcolor{magenta}{w_4} \right) \\
v_{n+1} &= v_n + \frac{h}{6} \left( \textcolor{blue}{a_1} + 2\textcolor{blue}{a_2} + 2\textcolor{blue}{a_3} + \textcolor{blue}{a_4} \right)
\end{align*}
$$

**Method Comparison**

<figure>
    <div style="text-align:center;">
    <img src="/Images/MethodComparison.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.9: Method Comparison</figcaption>
</figure>

- With equal timesteps h, higher order typically implies higher accuracy
- Higher accuracy leads to more stability
- Even RK4 and other high-order methods can loose stability

**Numerical Stability**

There is no simple and universal definition of numerical stability in general.

Loosely speaking: If the true solution $x(t)$ is bounded for all times,

$$
a \leq x(t) \leq b
$$

with constants $a$ and $b$, and the numerical solution $\~{x}(t)$ also remains bounded,

$$
a \leq \~{x}(t) \leq b
$$

for all times, a numerical method is said to be stable.

Stability depends on:
- The numerical method
- The step size $h$
- The problem/ODE solved (forces, stiffness, damping, ...)
- The initial conditions

**Numerical Stability Example**

Single spring with the forward Euler method:

<figure>
    <div style="text-align:center;">
    <img src="/Images/NumericalStabilityExample.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.10: Numerical Stability Example: Single Spring with the forward Euler method</figcaption>
</figure>

- Initial position $x_0 = A$
- Initial velocity $v_0 = 0$
- Spring rest length $L = 0$
- Force: $f = -k \cdot x$
- Solution: $x(t) = A \cos{(\sqrt{k/m} \cdot t) \in [-A, A']}$

The forward Euler method makes the first two steps with maximal force $f = -k \cdot A$, but the true force would be smaller. 

$$
\begin{align*}
x_{n+1} &= x_n + h \cdot v_n \\
v_{n+1} &= v_n + h \cdot \frac{f}{m} \\
&\Rightarrow x_0 = A \\
&\quad \quad v_0 = 0 \\
&\Rightarrow x_1 = A \\
&\quad \quad v_1 = -hkA/m \\
&\Rightarrow x_2 = A - h^2 kA/m \\
&\quad \quad v_2 = -2hkA/m
\end{align*}
$$

The numerical solution overshoots already in the second step $(x1 → x2)$ if $h > √2m/k$!

**Avoiding Instability**

How to avoid numerical instability?

Numerical instability is a consequence of the finite step size $h$.
- There is no universal solution to avoid numerical instability
- Smaller timesteps increase the chance for stability (⇒ slower simulation)
- Higher-order methods tend to be more stable (⇒ more complicated program)
- Increasing damping can help, but does not always (⇒ sometimes not desired)

How to predict numerical stability?
- Stability depends on many factors: The step size, the order, the ODE, initial conditions, ...
- This makes stability nearly impossible to predict in practice
- The stiffer the ODE you solve, the harder it is to remain stable
- Toy problems are usually used to quantify & compare the stability of different methods

**Stiffness**

Stiffness of a differential equation is itself difficult to define in general. 

Loosely speaking: A stiff problem is one for which the solution changes quickly. 

<figure>
    <div style="text-align:center;">
    <img src="/Images/StiffProblem1.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.11: Stiffness for Oscillation</figcaption>
</figure>

$$
\begin{align*}
m \frac{d^2 x}{dt^2}(t) &= -k \cdot x(t) \\
x(t) &= A \cos \left( \sqrt{\frac{k}{m}} \cdot t \right)
\end{align*}
$$

Here, the ratio $k/m$ determines the oscillation frequency, and therefore the “stiffness”

The concept of stiffness is more general than just oscillations of mass-spring systems.

Example: Degradation of a morphogen concentration C:

<figure>
    <div style="text-align:center;">
    <img src="/Images/StiffProblem2.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.12: Stiffness for Degeneration</figcaption>
</figure>

- Here, the morphogen turnover rate $k$ determines the “stiffness”
- But: The equation becomes less stiff over time, even though $k$ is constant!

**Size of the timestep**

$$
\begin{align*}
m \frac{d^2 x}{dt^2}(t) &= -k \cdot x(t) &\Rightarrow &\quad x(t) = A \cos(\omega t) &\quad \omega = \sqrt{\frac{k}{m}}
\end{align*}
$$

- For dynamic mass-spring systems, the oscillation frequency $ω$ sets  the timescale
- The timestep must be small enough to be able to track each oscillation: $ωh \ll 2π$
- ⇒ Choose $h \ll 2π√m/k$ (In practice: $h \leq \frac{1}{2}√m/k$ )
- Large mass-spring systems with different m’s and k’s: pick the smallest $m/k$ ratio
- 4× heavier masses allow for a doubling of the timestep $h$
- 4× stiffer springs require a twice smaller timestep $h$
- ⇒ Heavy & soft mass-spring systems are faster to solve than light & stiff ones

**Method 5: Backward Euler Method**


How to improve stability?

1st-order ODE:

$$
\frac{dx}{dt}(t) = g(x(t), t) 
$$

Newton's equation of motion:

$$
\frac{d^2 x}{dt^2}(t) = \frac{1}{m} f \left( x(t), \frac{dx}{dt}(t), t \right)
$$

Forward Euler:

$$
\begin{align*}
x_{n+1} &= x_n + h \cdot g(x_n) \\
x_{n+1} &= x_n + h \cdot v_n \\
v_{n+1} &= v_n + h/m \cdot f(x_n, v_n, t_n)
\end{align*}
$$

Backward Euler:

$$
\begin{align*}
x_{n+1} &= x_n + h \cdot g(\textcolor{red}{x_{n+1}}) \\
x_{n+1} &= x_n + h \cdot \textcolor{red}{v_{n+1}} \\
v_{n+1} &= v_n + h/m \cdot f(\textcolor{red}{x_{n+1}}, \textcolor{red}{v_{n+1}}, t_n+1)
\end{align*}
$$

- The backward Euler method is an implicit method; it is stable also for stiff problems
- The error order is the same as for forward Euler: Locally $O(h^2)$, globally $O(h)$
- Solve $x_n − x_{n+1} + h · g(x_{n+1}) = 0$ in each step
- Use Newton’s method to find the root xn+1
- For complex systems, this makes the algorithm much more complicated

**Trapezoidal Method**

$$
\begin{align*}
x_{n+1} &= x_n + h \frac{g(x_n, t_n) + g(\textcolor{red}{x_{n+1}}, t_{n+1})}{2} \\
\\
x_{n+1} &= x_n + h \frac{v_n + \textcolor{red}{v_{n+1}}}{2} \\
v_{n+1} &= v_n + h \frac{f(x_n, v_n, t_n) + f(x_{n+1}, \textcolor{red}{v_{n+1}}, t_{n+1})}{2m}
\end{align*}
$$
- The trapezoidal method is also an implicit method
- 2nd-order: Local error is $O(h^3)$, global error is $O(h^2)$
- Similarly complicated to implement as the backward Euler method

**Comparison of Methods**

<figure>
    <div style="text-align:center;">
    <img src="/Images/ComparisonOfSixMethods.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.13: Comparison of Methods</figcaption>
</figure>

### Symplectic Integrators

**Method 7: Semi-implicit Euler Method**

Simplest symplectic integrator: Semi-implicit Euler method:

$$
\begin{align*}
v_{n+1} &= v_n + h/m \cdot f(x_n, v_n, t_n) \\
x_{n+1} &= x_n + h \cdot \textcolor{red}{v_{n+1}}
\end{align*}
$$

This is just the forward Euler method with switched order

- Semi-implicit Euler is just as simple as the forward Euler
- Only 1st order, like the forward Euler
- For undamped systems ($f$ does not depend on $v$), it is 2nd order!

**Method 8: Velocity Verlet Method (Leapfrog Method)**

Very similar to the semi-implicit Euler method, when the force is velocity-independent:

- Only one force evaluation per timestep (reuse $a_{n+1}$ in the next step as an)
- 2nd-order method (global error is $O(h^2)$)
- This only applies to undamped systems where the force does not depend on velocity!
- In damped systems (where $f$ depends on $v$), the error is $O(h)$ (1st-order)

**Verlet Method (Störmer–Verlet method)**

Idea: Taylor Expansion:

$$
\begin{align*}
x(t + h) &= x(t) + \colorbox{gray}{$hv(t)$} + \frac{h^2}{2}a(t) + \frac{h^3}{6}x'''(t) + \mathcal{O}(h^4) \\
x(t - h) &= x(t) - \colorbox{gray}{$hv(t)$} + \frac{h^2}{2}a(t) - \frac{h^3}{6}x'''(t) + \mathcal{O}(h^4) \\
\hline
x(t + h) + x(t - h) &= 2x(t) + h^2 a(t) + \mathcal{O}(h^4)
\end{align*}
$$

Verlet Method:

$$
\begin{align*}
x_{n+1} &= 2x_n - x_{n-1} + \frac{h^2}{m} \cdot f(x_n, t_n)
\end{align*}
$$ddfdydghjkl

Only one force evaluation per timestep
- Multi-step method, requires storing two positions: $x_n$ and $x_{n−1}$
- Local error is $O(h^4)$ but global error is only $O(h^2)$ ⇒ 2nd-order method
- This only applies to undamped systems where the force does not depend on velocity!
- In damped systems (where f depends on v ), the error is O(h) (1st-order)

For umdamped systems, $f \neq f(v)$:

<figure>
    <div style="text-align:center;">
    <img src="/Images/ComparisonOfSymplecticIntegrators.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.13: Comparison of Symplectic Methods</figcaption>
</figure>

But: For all of these methods, adding damping forces increases the global error to $O(h)$
⇒ They all become 1st-order methods when $f = f (v )$

**Different types of ODE Integration Methods**

<ins>Explicit methods</ins>
$x_{n+1} = g(x_n, v_n, f_n, ...) , g$ is independent of $x_{n+1}, v_{n+1}$ and $f_{n+1}$

Pros:
- Easy to implement
-  Simple often means efficient (low memory requirement)

Con:
− Typically less stable than implicit methods ⇒ smaller timestep h required

Examples: Forward Euler, Midpoint, Heun, Verlet, Velocity Verlet, Runge–Kutta 4, etc.

<ins>Implicit methods</ins>
$x_{n+1} = g(x_{n+1}, v_{n+1}, f_{n+1}, x_n, v_n, f_n, ...) , g$ depends on x_{n+1} and/or v_{n+1} and/or f_{n+1}

Pro:
- Often more stable ⇒ larger timestep h possible

Cons:
− More complicated to implement
− More memory intensive
− Requires solution of an implicit equation (typically a system of linear equations)

Examples: Backward Euler, Trapezoidal, etc.
There are also hybrid methods (semi-implicit methods, predictor-corrector methods)

---

<ins>Single-step methods</ins>
$x_{n+1} = g(xn, vn, fn)$, only one previous step is required to compute the next

Pros:
- Easy to implement
- Simple often means efficient (low memory requirement)

Con:
- Low order ⇒ smaller timestep h required

Examples: Forward Euler, Velocity Verlet

<ins>Multi-step methods</ins>
$x_{n+1} = g(x_n, v_n, f_n, x_{n−1}, v{n−1}, f_{n−1}, x_{n+1/2}, v_{n+1/2}, f_{n+1/2}, ...)$, multiple previous steps or intermediate steps required to compute the next

Pro:
-  Higher order possible ⇒ larger timestep h possible

Cons
- More complicated to implement (keep track of older steps)
- Higher memory requirement
Example: Verlet, midpoint, Heun, Runge–Kutta 4

**Which Method to use?**

- Start with something simple (Semi-implicit Euler, Velocity Verlet)
- Increase $h$ until the error becomes unacceptable
- If performance still too low, try higher order or implicit methods

But:
- For damped systems for which only the final state in static equilibrium x(tend) is of
interest, simple low-order methods often suffice
- When the precise trajectory x(t) is needed, high-order methods should be used (e.g.,
4th-order Runge–Kutta)
- There are special methods that conserve the energy (symplectic methods).
Examples: Semi-implicit Euler, Verlet, Velocity Verlet

**Grid and Shear Stiffness**

Cubic grids without diagonal springs have no shear stiffness:

<figure>
    <div style="text-align:center;">
    <img src="/Images/NoSpringDeformation.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.14: Shear Stiffness</figcaption>
</figure>

For mass-spring systems, this must be avoided!

Triangular grids or random grids have no such zero-energy deformation modes:

<figure>
    <div style="text-align:center;">
    <img src="/Images/2DTriGrid.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.15: Traingular Grids</figcaption>
</figure>

In 3D, use tetrahedral grids!

**Contact Mechanics**

How to model contact with walls and obstacles?

<figure>
    <div style="text-align:center;">
    <img src="/Images/ContactMechanics.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.16: Contact Mechanics</figcaption>
</figure>

Penalty method: Apply a repulsive force in case of overlap of mass points with the obstacle.

Pros:
Very simple to implement
+ Additional $\vec{f_i}^ext(\vec{x_i}) $, works with all time integrators
+ Easy to formulate for many shapes: walls, spheres, cylinders, boxes, ...

Con:
− Requires strong force and relatively small timestep

Model the repulsive force with a spring with rest length $L = 0$:

$$
\begin{align*}
\textcolor{red}{\vec{f}^{\text{ext}}_i} (\vec{x}_i) &= \begin{bmatrix}
0 \\
0 \\
-k_{\text{wall}} (z_i - z_{\text{wall}})
\end{bmatrix} \quad \text{if} \quad z_i < z_{\text{wall}}
\end{align*}
$$

Corresponding elastic contact energy $C$:

$$
\begin{align*}
C &= \frac{1}{2} \sum_{i=1}^{N} k_{\text{wall}} (z_i - z_{\text{wall}})^2 \delta_{z_i < z_{\text{wall}}} \\
\text{where} \quad \delta_{z_i < z_{\text{wall}}} &= \begin{cases} 
1 & \text{if } z_i < z_{\text{wall}} \\
0 & \text{else}
\end{cases}
\end{align*}
$$

Choose a large enough $k_{wall}$ ⇒ Timestep $h ∝ √m/k_{wall}$ must be quite small.

**Critical Damping**

How to choose the damping coefficient?

<figure>
    <div style="text-align:center;">
    <img src="/Images/Damping.png" alt="Trapezoidal Rule" 
    style="width:100%; height:auto;">
    </div>
    <figcaption>Fig.17: Damping</figcaption>
</figure>

$$
\begin{equation}
m \frac{d^2 x}{dt^2}(t) - \gamma \frac{dx}{dt}(t) + kx(t) = 0
\end{equation}
$$

- Critical damping: $γ_{crit} = 2√mk$
- Damping ratio: $ζ = γ/γ_{crit}$
- ζ = 1: critical damping
- ζ < 1: subcritical damping
- ζ > 1: supercritical damping

### Summary

1. Mass-spring models are a simple way to model elastic deformations
2. There are many different time integrators of different order
3. Time integration methods are classified as explicit vs. implicit, and single-step vs.
multi-step
4. Explicit methods are much easier to implement — implicit methods require iterative
solvers in each timestep
5. Symplectic integrators conserve the total energy of Hamiltonian (undamped) systems
6. A stiff ODE is one whose solution changes rapidly. The stiffer an ODE, the harder it is
to solve numerically in a stable way.
7. Use a timestep $h \leq √m/k$ for explicit single-step methods
8. Use subcritical damping: $γ \ll 2√mk$
9. Careful about the spring arrangement: Use triangular grids to avoid zero-energy
modes.
10. The penalty method is a simple way to model contact with other objects (walls,
obstacles, ...)