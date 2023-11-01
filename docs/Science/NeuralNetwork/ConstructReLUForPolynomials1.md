---
layout: default
title: Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)
parent: Neural Network
grand_parent: Science
nav_order: 
header-includes:
   - \usepackage{amsmath}
   - \usepackage{amssymb}
---

## Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)

---

In this (Part 1) and the following article (Part 2), the goal is to construct **ReLU neural networks** which efficiently approximate polynomials and establish **approximation rates**, which quantify the size of the approximating neural networks relative to the approximation error. 

We start by recalling the definition of ReLU neural network. 

**Definition 1.** Let $L \in \mathbb{N} $ and $ N_{0}, N_{1}, \ldots, N_{L} \in \mathbb{N}$ given by

<br/>

$$  
    \Phi = 
    \tag{1}
    \begin{cases} 
      W_{1} & L = 1 \\
      W_{2} \circ \rho \circ W_{1} & L = 2 \\
      W_{L} \circ \rho \circ W_{L-1} \circ \rho \ldots \circ \rho \circ W_{1} & L \geq 3
   \end{cases}
$$

<br/>

where, for $l \in \{ 1, 2, \ldots, L\}$, $W_{l}: \mathbb{R}^{N_{l-1}} \rightarrow \mathbb{R}^{N_{l}}$, $W_{l}(x) := A_{l}x + b_{l}$ are the affine transformations with matrices $A_{l} \in \mathbb{R}^{N_{l} \times N_{l-1}}$ and (bias) vectors $b_{l} \in \mathbb{R}^{N_{l}} $, and the ReLU activation function $\rho: \mathbb{R} \rightarrow \mathbb{R}, \rho(x) := max(x, 0)$ acts component-wise. We denote by $N_{d,d'}$ the set of all ReLU networks with input dimension $N_{0} = d$ and output dimension $N_{L} = d'$. Moreover, we define the following quantities related to the notion of size of the ReLU network $\Phi$:

* connectivity $M(\Phi)$ : the total number of non-zero entries in the matrices $ A_{l}, l \in \{1, 2, \ldots, L \}$, and the vectors $b_{l}, l \in \{1, 2, \ldots, L \}$

* depth $L(\Phi) := L$

* width $W(\Phi) := max_{l=0,\ldots,L}N_{l}$

* weight manitude $B(\Phi) := max_{l=1, \ldots, L} max( \lVert A_{l} \rVert_{∞}, \lVert b_{l} \rVert_{∞} )$

Let's dissect **Definition 1** and examine the important concepts. A neural network is composed of the *input layer*, *hidden layers*, and the *output layer*. $N_{0}$ is the *dimension of the input layer* indexed as the 0-th layer; $N_{1}, \ldots, N_{L-1}$ are the *dimensions of the $L-1$ hidden layers*, and $N_{L}$ is the *dimension of the output layer*. 

The neural network defined in the equation (1) is essentially a sequence of [matrix compositions](https://www.youtube.com/watch?v=XkY2DOUCWMU). By rule, matrix composition is read from right to left. That is why $W_1$ appears at far right of the equation, followed by $W_{2}, W_{3}, \ldots$ on its left side. Geometrically, we can imagine neural networks as applying multiple *affine transformations* $W_{l}(x) := A_{l}x + b_{l}$ with activation functions $\rho$ sequentially. There is a [fascinating visualization](https://www.youtube.com/watch?v=UOvPeC8WOt8) that explains how the data input is manipulated through multiple layers of affine transformations and activation functions to generate the desired outcome. 

As for now, we proceed to proving the following result: 

**Theorem 1.** There exist constants $C>0$ and $D \in ℕ_{+}$ such that for all $	ε \in (0, 1/2)$, there is a ReLU network $\Phi_{ε}$ of depth $L(\Phi_{ε}) \leq C \log (ε^{-1})$ and width $W(\Phi_{ε}) \leq D$, such that 

$$
\lVert \Phi_{ε}(x) - x^{2} \rVert_{L^{∞}([0,1])} \leq ε 
$$

and $\Phi_{ε}(0) = 0$, $\lVert \Phi_{ε}(x) \rVert_{L^{∞}([0,1])} \leq 1$, $\lVert \Phi_{ε}(x) \rVert_{L^{∞}([0,1/2])} \leq 1/4$.

We start by demonstrating that every ReLU network realizes a continuous piecewise linear function. Consider a general function

$$
\tag{2}
\sum_{j=1}^{N} α_{j} \rho (y_{j}^{T}x + \theta_{j}), x \in \mathbb{R}^{n}
$$

Consider a concrete example of the form above: $\Phi(x) = 2 \rho(x) - \rho(x-1/2) - \rho(x-1)$, which is a piecewise-linear function with break points $\{0, 1/2, 1\}$



we start with the approximation of $x^{2}$ through continuous piecewise linear functions. 

