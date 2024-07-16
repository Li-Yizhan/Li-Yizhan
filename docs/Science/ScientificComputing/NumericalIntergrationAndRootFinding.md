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

### Monte Carlo integration & the curse of dimensionality**

## Numerical Root Finding

### How to solve nonlinear equations, i.e., find $x$ for which $f(x) = 0$

### Bisection method, regula falsi, secant method, Newton’s method

### Theory: Convergence order