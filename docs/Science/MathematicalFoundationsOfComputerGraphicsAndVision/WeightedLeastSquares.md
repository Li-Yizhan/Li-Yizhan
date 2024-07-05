---
layout: default
title: Weighted Least Squares
parent: Mathematical Foundations of Computer Graphics and Vision
grand_parent: Science
nav_order: 
---

## Weighted Least Squares

The **Ordinary Least Squares** method aims to minimize the usm of squared residuals (errors). The problem can be formulated as: 

$$
\arg \min_{\mathbf{x}} \sum_{i=1}^{m} (A_i \mathbf{x} - b_i)^2 = \arg \min_{\mathbf{x}} \sum_{i=1}^{m} e_i^2
$$

The **Weighted Least Squares (WLS)** method assigns a weight to each residual, which is inversely proportional to the **variance** of the corresponding observation's error term. This method ensures that observations with higher variance (less reliable) have less influence on the fitted model, while observations with lower variance (more reliable) have more influence. 

$$
\arg \min_{\mathbf{x}} \sum_{i=1}^{m} \frac{1}{\sigma_i^2} (A_i \mathbf{x} - b_i)^2 = \arg \min_{\mathbf{x}} \sum_{i=1}^{m} \frac{1}{\sigma_i^2} e_i^2
$$

## Why Weighted Least Squares?

Advantages:
- Regression in situations where data points are of varying quality
- Can handle non-constant standard deviation of the random errors in the data cross all levels of the explanatory variables

Disadvantages:
- In real life applications, weights are unknown and using estimated weights "breaks" the assumptions
- Can increase the influence of an outlier

## Iterative Re-weighted Least Squares (IRLS)

IRLS is a method used to solve optimization problems, particularly those involving robust regression. It is used to find the parameter estimates that minimize a loss function which may not be suitable fo rdirect minimization using ordinary least squares due to non-linearity or other complexities. 

1. Initialization
    - Set the initial parameter estimates $\Theta^{(0)}$

2. Compute Weights
    - For each iteration $t$:
    $$
    w_i(\Theta^{(t)}) = \left( |y_i - f(\Theta^{(t)}, x_i)| \right)^{p-2}
    $$

3. Solve Weighted Least Squares: 
    - Update the parater estimates by minimizing the weighted sum of squared residuals:
    $$
    \Theta^{(t+1)} = \arg \min_{\Theta} \sum_{i=1}^{n} w_i(\Theta^{(t)}) (y_i - f(\Theta, x_i))^2
    $$

4. Check for Convergence:
    - The process is repeated until the parameter estimates converge (i.e., the changes between iterations are sufficiently small)

## Moving Least Squares (MLS)

MLS is a method used to construct smooth surfaces or curves from a set of points. MLS extends the idea of least squares by incorporating a "moving" window or weight function that varies over the domain, allowing the method to adapt to local data structures. 

1. Define Weight Function
    - Choose an appropriate weight function $w(x)$ that decays with distance. For example, a Gaussian weight function:
    $$
    w_i(x) = \exp\left(-\left(\frac{x_i - x}{h}\right)^2\right)
    $$
    Where $h$ is a smoothing parameter controlling the width of the neighborhood

2. Formulate Local Polynomial
    - Construct a local polynomial approximation around the point of interest $x$. A common choice is a linear polynomial:
    $$
    f(x_i) = a + b(x_i - x)
    $$

3. Minimize Weighted Least Squares:
    - Solve for the coefficients $a$ and $b$ by minimizing the weighted sum of squared residuals:
    $$
    \arg \min_{a, b} \sum_{i=1}^{n} w_i(x) (y_i - (a + b(x_i - x)))^2
    $$

4. Compute Approximation
    - Evaluate the local polynomial at the point of interest to obtain the MLS approximation:
    $$
    f(x) = a
    $$