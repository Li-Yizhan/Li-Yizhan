---
layout: default
title: Numerical Integration and Root Finding
parent: ScientificComputing
grand_parent: Science
nav_order: 2
---

# Numerical Integration and Root Finding

## Numerical Integration

Why would I need to compute $∫_a^b f (x) \mathrm{d}x$ numerically?
- Many systems can be described by differential equations
- The mean value of a continuous function $f(x)$ is defined as $\bar{f} = \frac{1}{b-1} ∫_a^b f (x) \mathrm{d}x$ 
- Many processes in nature follow the principle of energy minimization. <ins>Energies can
typically be written as integrals</ins>.
- When the integrand $f (x)$ is known only point-wise $(f_1 = f (x_1), f2 = f (x_2), ...)$, numerical methods are needed.
- Often $f (x)$ cannot be expressed analytically or it is stochastic (noise)

### How to compute definite integrals $∫_a^b f (x) \mathrm{d}x$

**Method 1: Trapezoidal rule:**

Approximate $f(x)$ by a straight line between the endpoints, for which the integral is known:

<figure>
    <div style="text-align:center;">
    <img src="/Images/TrapezoidalRule.png" alt="Trapezoidal Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.1: Trapezoidal Rule</figcaption>
</figure>

- Only 2 function values are needed: $f(a)$ and $f(b)$. 
- $f(x)≈p(x)$ only if $f$ doesn't fluctuate much between $a$ and $b$, so this works <ins>only for very short integration intervals</ins>. 

**Trapezoidal Rule: h-refinement**

For long integrals, divide it into $n$ subintervals of length $h$ and sum up the integrals. 

<figure>
    <div style="text-align:center;">
    <img src="/Images/hRefinement.png" alt="Trapezoidal Rule: h-refinement" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.2: Trapezoidal Rule: h-refinement</figcaption>
</figure>

For $h = \frac{b-a}{n}$ and $x_i=a + i \cdot h$:

$$
∫_a^b f(x)d(x) ≈ h\left(\frac{f(x_0)}{2}+\sum_{i=1}^{n-1} f(x_i) + \frac{f(x_n)}{2}\right)
$$

Complexity: $O(N)$ ($N = n+1$ function evaluations needed to compute a 1D integral)

**Method 2: Simpson's Rule**

Approximate $f(x)$ by a parabola defined by 3 points, for which the integral is known:

<figure>
    <div style="text-align:center;">
    <img src="/Images/SimpsonRule.png" alt="Simpson's Rule" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.3: Simpson's Rule</figcaption>
</figure>

- 3 function values are needed: $f(a), f(b),$ and $f(\frac{a+b}{2})$.
- $f(x) ≈ p(x)$ only if $a$ and $b$ are near each other, so this also works well only for very short integrals. 

Derivation of Simpson's Rule:
- Simpson's Rule approximate $f(x)$ using a quadratic polynomial $p(x)$ that passes through the points $(a, f(a)), (b, f(b))$, and the midpoint $(\frac{a+b}{2}, f(\frac{a+b}{2}))$

- A quadratic polynomial can be written as $p(x) = Ax^2 + Bx + C$

- To determine $A, B,$ and $C$, we can set up the system of equations:

$$
\begin{cases}
    A a^2 + B a + C = f(a) \\
    A b^2 + B b + C = f(b) \\
    A \left( \frac{a + b}{2} \right)^2 + B \left( \frac{a + b}{2} \right) + C = f\left( \frac{a + b}{2} \right)
\end{cases}
$$

- Integral of the quadratic polynomial over [a,b] can be found using basic calculus:

$$
\int_{a}^{b} p(x) \, dx = \int_{a}^{b} (A x^2 + B x + C) \, dx
$$

- This evaluate to:

$$
A \left[ \frac{x^3}{3} \right]_{a}^{b} + B \left[ \frac{x^2}{2} \right]_{a}^{b} + C \left[ x \right]_{a}^{b}
$$

By solving the system of equations and integrating, the integral of the polynomial can be approximated in the form:

$$
\int_{a}^{b} f(x) \, dx \approx \frac{b - a}{6} \left[ f(a) + 4 f\left( \frac{a + b}{2} \right) + f(b) \right]
$$

**Simpson's Rule: h-refinement, p-refinement**

<figure>
    <div style="text-align:center;">
    <img src="/Images/SimpsonHPRefinement.png" alt="Simpson's Rule: h-refinement, p-refinement" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.4: Simpson's Rule: h-refinement, p-refinement</figcaption>
</figure>

- Complexity: $O(N)$
- 2nd refinement technique: Increase the degree of the polynomial (1: linear, 2: quadratic, 3: cubic eetc.). This is called <ins>p-refinement</ins>
- These polynomials are also called basis functions or shape functions.

**Practical Issues**
- Non-Uniform Grid Spacing
    - E.g., if the values are coming from expensive experiments or simulation output
    - Apply an integration formula for one interval to each subinterval
- Noisy Data
    - What if the function values $f_1. f_2, \ldots$ are stochastic/unreliable?
        - Fit a model function to the data first, then integrate that function
        - Aggregate the data into bins, and use the bin averages to integrate 

**Convergence Order**

$$
∫_a^b f(x)d(x) = \sum_{i=1}^n p(x) dx + e(f, p, a, b, h), \quad h = x_i - x_{i-1}
$$

- How big is the error $e$ made with these approximations?
- How to compare different numerical integration methods?

>**Definition: Convergence order of an integration method**
The exponent $\alpha$ of the resolution $h$ with which the error $e$ asymptotically decreases according to $\lvert e \rvert ∼ h^{\alpha}$

- Trapezoidal rule: $e = O(h^2)$ (2nd-order h-convergence)
- Simpson's rule: $e = O(h^4)$ (4th-order h-convergence)

These two methods are examples of composite Newton-Cotes rules. There are many more such integration methods that use other types of polynomials. 

**Convergence Plot**
- Higher convergence order is generally better.
- Like the Landau notation for algorithmic complexity, it says nothing about the absolute error, only how the error scales if $h$ is reduced. 

<figure>
    <div style="text-align:center;">
    <img src="/Images/ConvergencePlot.png" alt="Convergence Plot" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.5: Convergence Plot for Trapezoidal rule and Simpson's rule</figcaption>
</figure>

When the relative error approaches the limit of double precision (around $10^{-16}$), numerical fluctuation and deviation emerges. 

**Newton-Cotes formulas**

- The Newton-Cotes rules use polynomials with degree $k: p(x) = a_k x^k + \ldots + a_1x + a_0$
- They integrate polynomials with degree $k+1$ exactly if $k$ is even, degree $k$ if $k$ is odd. 
- They are therefore said to have precision order $k+1$ or $k$ (not to be confused with the h-convergence order!)
- The precision order of these formulas is $k+1$ for even $k$ and $k$ for odd $k$. This means the rule exactly integrates polynomials up to this degree. 

<figure>
    <div style="text-align:center;">
    <img src="/Images/NewtonCotesExample.png" alt="Newton-Cotes Example" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.6: Newton-Cotes Example with k = 0 (Midpoint Rule)</figcaption>
</figure>

- Two classes of Newton-Cotes formulas: Open and closed
- Closed formulas use endpoints $x_0 = a$ and $x_k = b$ as integration points
- Open formulas use only points in the interior of the interval

**Maximizing Efficiency of Numerical Integration**

Numerical integration is also called numerical quadrature or just quadrature
- Quadratures are often selected based on precision per computational cost
- To measure cost, the number of function evaluations is usually taken
- With N function values, what’s the maximal precision order a quadrature can have?
- Or: If we want a quadrature of a specific order, how many function evaluations are
needed at minimum?
- This question will be crucial later, e.g., for the finite element method

**Method 3: Gaussian Quadrature**

It can be proven that Gaussian quadrature has the largest possible precision order: $2N-1$ for $N$ function evaluations in $1D$.
- It means that Gaussian quadrature can exactly integrate any polynomial of degree up to $2N - 1$. 

$$
∫_{-1}^1 f(x) dx ≈ \sum_{i=1}^N w_i f(x_i)
$$

For a desired $N$, the question is then only how to choose the nodes $x_i$ and integration weights $w_i$. These are called the Gauss points and Gauss weights. 

Gaussian quadrature is optimal in the sense that it is exact for the polynomial with highest possible degree:

$f (x) = a_{2N−1}x^{2N−1} + ... + a_1x + a_0$

Gauss points are usually defined on the interval [-1, 1]. For any integration bounds $a, b$ transform the problem according to:

$$
∫_{-1}^1 f(x) dx = \frac{b-a}{2}∫_{-1}^1f(\frac{b-a}{2}ξ + \frac{a+b}{2}) dξ
$$

The normalized variable $ξ \in [-1,1]$ is also called barycentric coordinate. 

Gauss points and corresponding weights for integration with maximal order can be defined also in higher dimensions. 

### Multidimensional integrals: $∫_{a_N}^{b_N} \ldots ∫_{a_2}^{b_2} ∫_{a_1}^{b_1} f(x_1, x_2, \ldots, x_N) \mathrm{d}x_1, \mathrm{d}x_2 \ldots \mathrm{d}x_N$

How to integrate multidimensional integrals?
- As long as the integration bounds are constant (independent from each other), i.e., the integration domain is a box, one can use the tensor product rule:

Curse of dimensionality: Number of quadrature points $N ~ n^d$ explodes exponentially with the dimension $d$. 

**Method 4: Monte Carlo Sampling**

Monte Carlo (MC) methods are generally all computational methods that use random numbers (not just for integration)

Draw random quadrature points $x_i$ from a uniform distribution in [a, b] and calculate the mean function value:

$$
\int_{a}^{b} f(x) \, dx = (b - a) \langle f(x) \rangle \approx \frac{b - a}{N} \sum_{i=1}^{N} f(x_i)
$$

**Method 5: Shooting Method (Acceptance-Rejection Method)**

Another Monte Carlo method:
1. Choose $y_{min}, y_{max}$ such that $y_{min} \leq f(x) \leq y_{max}$ for all $x \in [a, b]$. This might be hard to do if $f$ is unknown
2. Draw random coordinates uniformly in the box: $(x_i, y_i) \in [a,b] \times [y_{min}, y_{max}]$
3. Count the fraction of coordinates $\rho \in [0, 1]$ for which $y_i < f(x_i)$
4. Evaluate the integral as follows: 

$$
\int_{a}^{b} f(x) \, dx \approx (b - a) \left( \rho y_{\text{max}} + (1 - \rho) y_{\text{min}} \right)
$$

This also works with points $(x_i, y_i)$ on a regular rectangular grid. It is then not a Monte Carlo method anymore. 
- Monte Carlo methods rely on randomness to sample points. The randomness helps in approximating the integral, especially in higher dimensions or for complex functions
- The points $(x_i, y_i)$ are randomly distributed within the integration domain, which allows for statistical techniques to estimate the integral. 
- If the points are placed on a regular rectangular grid, the randomness is removed. The method then becomes a deterministic numerical integration method, similar to Trapezoidal Rule or Simpson's Rule. 

The shooting method can be generalized to high-dimensional, non-regular domains:
1. Choose a box $B$ that fully contains the integration domain $Ω (Ω ⊂ B)$
2. Calculate the box volume $\lvert B \rvert$ 
3. Draw $N$ random coordinates $\bar{x_i} \in B$
4. Count the number $M$ of coordinates for which $\bar{x_i} \in Ω$
5. Evalulate the integral as follows:

$$
\int_{\Omega} f(\vec{x}) \, d\vec{x} \approx \frac{|B|}{N} \sum_{i=1}^{M} f(\vec{x}_i)
$$

For $f(\vec{x}) ≡ 1$, this yields the volume of the domain: 

$$
|\Omega| = \int_{\Omega} d\vec{x} \approx |B| \frac{M}{N}
$$

**Curse of Dimensionality**
- For classical quadrature methods with h-convergence order $α$: Error is $O(h^α)$
- Using the tensor product rule, one can solve d-dimensional integrals with $N ∼ 1/h^d$ integration points
- Total error in d dimensions: $O(N^{−α/d})$
    - $E ∼ h^α$
    - $N ∼ 1/h^d$
    - $h ∼ N^{−1/d}$
    - $E ∼ N^{−α/d}$
- Number of function evaluations $N$ needed to achieve a certain precision $P$: $N = O(P^{d/α})$ (Exponential complexity!)
    - To achieve desired precision $P$, we need to set the error $E$ to $P$: $E∼P∼N^{-α/d}$
    - $N∼P^{-d/α}$

- For high-dimensional domains, this is getting very slow
- The dimensions can be space $(x,y,z)$, time $(t)$, or any number of other parameters

Central limit theorem ⇒ for MC integration the error is $O(N^{-1/2})$
- With MC integration, the scaling of the error is independent of $d$
- Trapezoidal rule: $α = 2$, so MC is more efficient in $d > 4$ dimensions
- Simpson’s rule: $α = 4$, so MC is more efficient in $d > 8$ dimensions

**Advantages and disadvantages of Monte Carlo integration**
Advantgaes:
- No curse of dimensionality; very efficient for high-dimensional problems
- Easy to implement
- Can handle very complex integration domains
Disadvantages:
- Slow convergence for small $d$: error is $O(1/\sqrt{N})$
- Random nature of results

## Numerical Root Finding

A very frequent problem in science: find $\vec{x^∗}$ such that $f (\vec{x^∗}) = 0$ for a nonlinear function $f$.

>**Definition: Root of a function**
A point $\vec{x^∗}$ where $f (\vec{x^∗}) = 0$ is called a root of $f$.
 
- A root of a function f is also called a zero of $f$.
- How to find roots numerically?
- How to compare the suitability and efficiency of different methods?
- What if there are multiple solutions?

### How to solve nonlinear equations, i.e., find $x$ for which $f(x) = 0$

### Bisection method, regula falsi, secant method, Newton’s method

### Theory: Convergence order