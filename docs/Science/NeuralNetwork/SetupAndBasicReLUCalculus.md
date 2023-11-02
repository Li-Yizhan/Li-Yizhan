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

**Definition 1.** Let $L \in \mathbb{N} $ and $ N_{0}, N_{1}, \ldots, N_{L} \in \mathbb{N}$ given by

$$  
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

**Remark.** A neural network is composed of the *input layer*, *hidden layers*, and the *output layer*. $N_{0}$ is the *dimension of the input layer* indexed as the 0-th layer; $N_{1}, \ldots, N_{L-1}$ are the *dimensions of the $L-1$ hidden layers*, and $N_{L}$ is the *dimension of the output layer*. 

The neural network defined in the equation (1) is essentially a sequence of [matrix compositions](https://www.youtube.com/watch?v=XkY2DOUCWMU). By rule, matrix composition is read from right to left. That is why $W_1$ appears at far right of the equation, followed by $W_{2}, W_{3}, \ldots$ on its left side. Geometrically, we can imagine neural networks as applying multiple *affine transformations* $W_{l}(x) := A_{l}x + b_{l}$ with activation functions $\rho$ sequentially. There is a [fascinating visualization](https://www.youtube.com/watch?v=UOvPeC8WOt8) that explains how the data input is manipulated through multiple layers of affine transformations and activation functions to generate the desired outcome. 

---

**Lemma 2.3** Let $d_{1}, d_{2}, d_{3} \in ℕ, \Phi_{1} \in N_{d1, d2}$, and $\Phi_{2} \in N_{d2, d3}$. Then, there exists a network $\Psi \in N_{d1, d2}$ with $ L(\Psi) = L(\Phi_{1}) + L(\Phi_{2}), M(\Psi) = 2M(\Phi_{1}) + 2M(\Phi_{2}), W(\Psi) \leq \max(2d_{2}, W(\Phi_{1}), W(\Phi_{2})), B(\Psi) = \max(B(\Phi_{1}), B(\Phi_{2}))$ and satisfying $\Psi(x) = (\Phi_{2} \circ \Phi_{1})(x) = \Phi_{2}(\Phi_{1}(x)), \quad \text{for all } x \in \mathbb{R}^{d_1}$

*Proof.* The proof is based on the identity $x = \rho(x) - \rho(-x)$ for ReLU activation function. First, note that by **Definition 1**, we can write 

$$
\Phi_{1} = W_{L1}^{1} \circ \rho \circ W_{L1-1}^{1} \circ \ldots \circ \rho \circ W_{1}^{1} \quad \text{and} \quad \Phi_{2} = W_{L2}^{2} \circ \rho \circ \ldots \circ \rho \circ W_{1}^{2}
$$

If we compose $\Phi_2$ with $\Phi_1$ directly, the outcome $ W_{L2}^{2} \circ \rho \circ \ldots \circ \rho \circ W_{1}^{2} \circ W_{L1}^{1} \circ \rho \circ W_{L1-1}^{1} \circ \ldots \circ \rho \circ W_{1}^{1}$ does not match the general architecture of the neural network defined earlier, because the section $W_{1}^{2} \circ W_{L1}^{1}$ does not have an activation function $\rho$ in between. Therefore, our goal is to replace the section $W_{1}^{2} \circ W_{L1}^{1}$ with something equivalent but in the form of $W \circ \rho \circ W$.

Let $N_{L1-1}^1$ denote the width of layer $L_1-1$ in $\Phi_1$ and let $N_1^2$ denote the width of layer 1 in $\Phi_2$. We define the affine transformations $\~W_{L_1}^1: ℝ^{N_{L_1-1}^1} \rightarrow ℝ^{2d_2}$ and $\~W_1^2: ℝ^{2d_2} \rightarrow ℝ^{N_1^2}$ according to

$$
\tilde{W}_{L1}^1(x):= \begin{pmatrix} I_{d_2}\\ -I_{d_2}\end{pmatrix} W_{L1}^1 (x) \quad \text{and} \quad \tilde{W}_1^2(y):= W_1^2 (\begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} y)
$$ 

Now we can show that, step by step, why $\~W_1^2 \circ \rho \circ \~W_{L_1}^1 $ is the same as $W_{1}^{2} \circ W_{L1}^{1}$

$$\begin{align*}
\tilde{W}_{L1}^1(x)&= \begin{pmatrix} I_{d_2}\\ -I_{d_2}\end{pmatrix} W_{L1}^1 (x) \\ &= \begin{pmatrix} W_{L1}^1 (x)\\ -W_{L1}^1 (x)\end{pmatrix} \\
\rho \circ \begin{pmatrix} W_{L1}^1 (x)\\ 
\\
-W_{L1}^1 (x)\end{pmatrix} &= \begin{pmatrix} \rho (W_{L1}^1 (x))\\ \rho(-W_{L1}^1 (x))\end{pmatrix} \\
\\
\tilde{W_1}^2 \circ \rho \circ \tilde{W}_{L_1}^1 &= W_1^2 (\begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} \begin{pmatrix} \rho (W_{L1}^1 (x))\\ \rho(-W_{L1}^1 (x))\end{pmatrix}) \\
&= W_1^2 \circ \begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} \begin{pmatrix} \rho (W_{L1}^1 (x))\\ \rho(-W_{L1}^1 (x))\end{pmatrix}\\
&= W_1^2 \circ (\rho (W_{L1}^1 (x)) - \rho (-W_{L1}^1 (x))) \\
&= W_1^2 \circ W_{L1}^1
\end{align*}$$

Therefore, the network $\Psi = W_{L2}^{2} \circ \rho \circ \ldots \circ \rho \circ \~W_{1}^{2} \circ \rho \circ W_{L1}^{1} \circ \rho \circ W_{L1-1}^{1} \circ \ldots \circ \rho \circ W_{1}^{1}$ is equivalent to $(\Phi_2 \circ \Phi_1)(x)$. And by examine the architecture of $\Psi(x)$, we notice that the claimed properties are all satisfied. 

---

**Lemma 2.4** Let $d_1, d_2, K \in \mathbb{N}$ and $\Phi \in N_{d_1, d_2}$ with $L(\Phi) < K$. Then, there exists a network $\Psi \in N_{d_1, d_2}$ with $L(\Psi) = K, M(\Psi) \leq M(\Psi) + d_2 W(\Psi) + 2d_2(K-L(\Phi)), W(\Psi) = \max(2d_2, W(\Phi)), B(\Psi) = \max(1, B(\Phi))$
and satisfying

$$
\Psi (x) = \Phi (x) \text{ for all } x \in ℝ^{d_1}
$$

*Proof.* Let $\~W_j(x) := diag \begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} x$, for $j \in \{L(\Phi) + 1, \ldots, K-1\}$

