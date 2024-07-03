---
layout: default
title: Fitting and Norm
parent: Mathematical Foundations of Computer Graphics and Vision
grand_parent: Science
nav_order: 
---

## What is Fitting?

**Fitting** refers to the process of finding a mathematical model that best describes a set of observed data points. This involves determining the parameters of the model such that the difference between the observed data and the model's predictions is minimized. 

It plays a crucial role in various computer vision tasks including:
- Object Detection and Recognition
- Camera Calibration
- Motion Tracking
- 3D Reconstruction
- Image Segmentation

## Line Fitting

**Line fitting** (or linear regression) is a specific type of fitting where the goal is to find the best-fitting straight line through a set of data points.

- Input: a set of $n$ 2D points $(x_i, y_i)$
- Output: the line $y = ax + b$ minimizing the fitting error

<div style="text-align:center;">
<img src="/Images/BestFittingLineExample.png" alt="Best Fitting Line Example" 
style="width:50%; height:auto;">
</div>

>Best Fitting Line Example

## Fitting Cost and Norms

**Fitting Cost** represents the total discrepancy between the observed data points and the model's predictions. The goal is to minimize the fitting cost during the fitting process to improve the model's accuracy.

In mathematical terms, a **norm** is a function that assigns a non-negative length or size to vectors in a vector space. In the context of fitting, the choice of norm determines how the fitting cost is measured, leading to different optimization obectives and thus different fitting results. 

$$
\|\mathbf{x}\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{1/p}
$$
>General Lp Norm

For instance, let $x = (-3, 0, 4):$

- $L2$ Norm Calculation:

$$
\|\mathbf{x}\|_2 = \sqrt{(-3)^2 + 0^2 + 4^2} = \sqrt{25} = 5
$$

- $L1$ Norm Calculation:

$$
\|\mathbf{x}\|_1 = | -3 | + | 0 | + | 4 | = 7
$$

- $L_\infty$ Norm Calculation:

$$
\|\mathbf{x}\|_\infty = \max_i |x_i| = \max (|x_1|, \ldots, |x_n|) = 4
$$

- $L_0$ Norm Calculation (very popular in sparse representation and learning):

$$
\|\mathbf{x}\|_0 = \text{card} (i|x_i \neq 0) = 2
$$

Here is the formal definition for norm:

Let us consider a vector space $V$ over a subfield $F$ of the complex numbers. A norm on $V$ is a function $p: V \rightarrow \mathbb{R}$ with the following properties:
For all $a \in F$ and all $\mathbf{u}, \mathbf{v} \in V$,

$$
\begin{align*}
p(a\mathbf{v})& = |a|p(\mathbf{v}) \\
p(\mathbf{u} + \mathbf{v}) &\leq p(\mathbf{u}) + p(\mathbf{v}) \\
\text{If } p(\mathbf{v}) &= 0 \text{ then }\mathbf{v} \text{ is the zero vector}
\end{align*}
$$

## Loss Function

As mentioned earlier, norms are mathematical functions that measure the size or length of a vector in a vector space. Commonly used norms in the context of loss functions include:

- L2 Norm (Euclidean Norm)
    - Loss Function: Mean Squared Error (MSE): $\frac{1}{n} \sum_{i=1}^{n} (y_i - \^{y_i})^2$

- L1 Norm (manhattan Norm)
    - Loss function: Mean Absolute Error (MAE): $\frac{1}{n} \sum_{i=1}^{n} |y_i - \^{y_i}|$

There are also loss functions used in machine learning and optimization that do not directly correspond to any specific norm. These loss functions are designed to handle particular scenarios or requirements and provide flexibility beyond what norms can offer. 

- Cross-Entropy Loss
    - Binary Classification: $-(y \log{(\^y)}+(1-y)\log{(1-\^{y})}) $

- Hinge Loss

- Huber Loss

## Solving L2 Norm Fitting Cost

When applied to fitting, the **L2 Norm (Euclidean Norm)** minimizes the sum of squared residuals. Here, the residual is the vertical distance between actual y value and the predicted y value $(ax+b)$: 

$$
\min_{a,b} \sum_{i=1}^{n} (y_i - (ax_i + b))^2
$$
>Fitting Cost Function for L2 Norm

To minimize the function $R(a,b) = \sum_{i=1}^{n} (y_i - (ax_i + b))^2$, we use calculus, specifically the gradient. The gradient of a function points in the direction of the steepest ascent. By setting the gradient to zero, we find the critical points, which are potential minima, maxima, or saddle points. If we can prove that the objective function $R(a,b)$ is convex, the critical points would be corresponded to the minimum. 

The Hessian matrix is a square matrix that describes the local curvature of the function. It is commonly used for convexity determination of a function. Quadratic functions are convex if their Hessian matrix (the matrix of second-order partial derivatives) is positive semi-definite. 

To calculate the Hessian matrix of a function $R(a,b)$, we need to find the second-order partial derivatives of the function with respect to the parameters $a$ and $b$. Given the sum of squared errors function:

$$
R(a,b) = \sum_{i=1}^{n} (y_i - (ax_i + b))^2
$$

First-order partial derivatives of $R(a,b)$ with respect to $a$ and $b$:

$$
\begin{align*}
\frac{\partial R}{\partial a} &= -2 \sum_{i=1}^{n} (y_i - (ax_i + b)) x_i \\
\frac{\partial R}{\partial b} &= -2 \sum_{i=1}^{n} (y_i - (ax_i + b))
\end{align*}
$$

Second-order partial derivatives of $R(a,b)$ with respect to $a$ and $b$ respectively:

$$
\begin{align*}
\frac{\partial^2 R}{\partial a^2} &= \frac{\partial}{\partial a} (-2 \sum_{i=1}^{n} (y_i - (ax_i + b)) x_i) \\
&= -2 \sum_{i=1}^{n} (-x_i) x_i \\ &= 2 \sum_{i=1}^{n} x_i^2 \\
\frac{\partial^2 R}{\partial b^2} &= \frac{\partial}{\partial a} (-2 \sum_{i=1}^{n} (y_i - (ax_i + b)))\\
&= -2 \sum_{i=1}^{n} (-1) \\ &= 2n
\end{align*}
$$

Second-order partial derivatives of $R(a,b)$ with respect to $a$ and $b$ altogether:

$$
\begin{align*}
\frac{\partial^2 R}{\partial a \partial b} &= \frac{\partial}{\partial b} (-2 \sum_{i=1}^{n} (y_i - (ax_i + b)) x_i) \\
&= -2 \sum_{i=1}^{n} (-x_i) \\ &= 2 \sum_{i=1}^{n} x_i
\end{align*}
$$

The **Hessian matrix** $H$ is then:

$$
H = \begin{bmatrix}
\frac{\partial^2 R}{\partial a^2} & \frac{\partial^2 R}{\partial a \partial b} \\
\frac{\partial^2 R}{\partial b \partial a} & \frac{\partial^2 R}{\partial b^2}
\end{bmatrix}
= \begin{bmatrix}
2 \sum_{i=1}^{n} x_i^2 & 2 \sum_{i=1}^{n} x_i \\
2 \sum_{i=1}^{n} x_i & 2n
\end{bmatrix}
$$

We need to prove that $H$ is positive semi-definite to verify its convex shape. 

Let $A$ be a symmetric matrix $(A = A^T)$ in $\mathbb{R}^{n \times n}$. We say that $A$ is: 

1. **positive definite** iff $\mathbf{x}^\top A \mathbf{x} > 0$ for all $\mathbf{x} \in \mathbb{R}^n \setminus \{0\}$;

2. **positive semidefinite** iff $\mathbf{x}^\top A \mathbf{x} \geq 0$ for all $\mathbf{x} \in \mathbb{R}^n$;

3. If neither $A$ nor $-A$ is positive semidefinite, we say that $A$ is **indefinite**.

Let $A$ be a symmetric matrix in $\mathbb{R}^{n \times n}$. 
1. A is **positive definite** iff all its eigenvalues are positive;
2. A is **positive semidefinite** iff all its eigenvalues are non-negative.

For a symmetric $2 \times 2$ matrix, this condition can be efficiently checked by examining the leading principal minors of the matrix. The leading principal minors are determinants of the top-left submatrices of increasing size. 

For H to be positive semi-definite:
1. The first leading principal minor, in this case $\sum_{i=1}^{n} x_i^2$. must be non-negative;
2. The second leading principal minor, $\det(H)$, must be non-negative. 

For the Hessian matrix we constructed, both conditions are satisfied: 
1. $\sum_{i=1}^{n} x_i^2 \geq 0$
2. $\det(H) = n \sum_{i=1}^{n} x_i^2 - (\sum_{i=1}^{n} x_i)^2 \geq 0$ (Cauchy-Schwarz inequality)

Therefore, we can conclude that the fitting cost function $R(a,b)$ is always convex. To find the critical point (minimum error), we need to solve the following two equations:
$$
\begin{align*}
\frac{\partial R}{\partial a} &= -2 \sum_{i=1}^{n} (y_i - (ax_i + b)) x_i = 0 \\
\frac{\partial R}{\partial b} &= -2 \sum_{i=1}^{n} (y_i - (ax_i + b)) = 0
\end{align*}
$$

The L2 norm offers following advantages:
- Non-negativity: squaring ensures that all error contributions are positive, so errors don't cancel each other out.
- Emphasizes Larger Errors: squaring disproportionately penalizes larger errors.
- Differentiability: the squared fitting cost function is smooth and differentiable, making it easier to work with mathematically, particularly for optimization using calculus. 

## Linear System