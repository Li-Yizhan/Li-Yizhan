---
layout: default
title: Setup and Basic ReLU Calculus
parent: Neural Network
grand_parent: Science
nav_order: 1
---

## Setup and Basic ReLU Calculus

---

There is a plethora of neural network architectures and activation functions in the literature. Here, we restrict to the ReLU activation function and consider the following general network architecture.

>**Definition 1.** Let $L \in \mathbb{N} $ and $ N_{0}, N_{1}, \ldots, N_{L} \in \mathbb{N}$ given by
>
>$$  
    \Phi = 
    \tag{1}
    \begin{cases} 
      W_{1} & L = 1 \\
      W_{2} \circ \rho \circ W_{1} & L = 2 \\
      W_{L} \circ \rho \circ W_{L-1} \circ \rho \ldots \circ \rho \circ W_{1} & L \geq 3
   \end{cases}
$$

where, for $l \in \{ 1, 2, \ldots, L\}$, $W_{l}: \mathbb{R}^{N_{l-1}} \rightarrow \mathbb{R}^{N_{l}}$, $W_{l}(x) := A_{l}x + b_{l}$ are the affine transformations with matrices $A_{l} \in \mathbb{R}^{N_{l} \times N_{l-1}}$ and (bias) vectors $b_{l} \in \mathbb{R}^{N_{l}} $, and the ReLU activation function $\rho: \mathbb{R} \rightarrow \mathbb{R}, \rho(x) := max(x, 0)$ acts component-wise. We denote by $N_{d,d'}$ the set of all ReLU networks with input dimension $N_{0} = d$ and output dimension $N_{L} = d'$. Moreover, we define the following quantities related to the notion of size of the ReLU network $\Phi$:

* connectivity $M(\Phi)$ : the total number of non-zero entries in the matrices $ A_{l}, l \in \{1, 2, \ldots, L \}$, and the vectors $b_{l}, l \in \{1, 2, \ldots, L \}$

* depth $L(\Phi) := L$

* width $W(\Phi) := max_{l=0,\ldots,L}N_{l}$

* weight manitude $B(\Phi) := max_{l=1, \ldots, L} max( \lVert A_{l} \rVert_{∞}, \lVert b_{l} \rVert_{∞} )$

**Lemma 2.3** Let $d_{1}, d_{2}, d_{3} \in ℕ, \Phi_{1} \in N_{d1, d2}$, and $\Phi_{2} \in N_{d2, d3}$. Then, there exists a network $\Psi \in N_{d1, d2}$ with $L(\Psi) = L(\Phi_{1}) + L(\Phi_{2}), M(\Psi) = 2M(\Phi_{1}) + 2M(\Phi_{2}), W(\Psi) \leq max\{2d_{2}, W(\Phi_{1}), W(\Phi_{2})\}, B(\Psi) = max\{B(\Phi_{1}), B(\Phi_{2})\}$, and satisfying

$$
\Psi(x) = (\Phi_{2} \circ \Phi_{1})(x) = \Phi_{2}(\Phi_{1}(x)), \quad \text{for all }x \in \mathbb{R}^{d_1}
$$