---
layout: default
title: Setup and Basic ReLU Calculus
parent: Neural Network
grand_parent: Science
nav_order: 1
---

## Setup and Basic ReLU Calculus

---

**Table of Contents**
* [General Definition](#GD)
* [Lemma 2.3](#L23)
* [Lemma 2.4](#L24)
* [Lemma 2.5](#L25)
* [Lemma 2.6](#L26)

---

There is a plethora of neural network architectures and activation functions in the literature. Here, we restrict to the ReLU activation function and consider the following general network architecture.

<h3 id="GD"></h3>

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
<h3 id="L23"></h3>

**Lemma 2.3** Let $d_{1}, d_{2}, d_{3} \in ℕ, \Phi_{1} \in N_{d1, d2}$, and $\Phi_{2} \in N_{d2, d3}$. Then, there exists a network $\Psi \in N_{d1, d2}$ with 
* $ L(\Psi) = L(\Phi_{1}) + L(\Phi_{2})$, 
* $M(\Psi) = 2M(\Phi_{1}) + 2M(\Phi_{2})$, 
* $W(\Psi) \leq \max(2d_{2}, W(\Phi_{1}), W(\Phi_{2}))$, 
* $B(\Psi) = \max(B(\Phi_{1}), B(\Phi_{2}))$ 

and satisfying $\Psi(x) = (\Phi_{2} \circ \Phi_{1})(x) = \Phi_{2}(\Phi_{1}(x)), \text{for all } x \in \mathbb{R}^{d_1}$

*Proof.* The proof is based on the identity $x = \rho(x) - \rho(-x)$ for ReLU activation function. First, note that by **Definition 1**, we can write 

$$
\Phi_{1} = W_{L1}^{1} \circ \rho \circ W_{L1-1}^{1} \circ \ldots \circ \rho \circ W_{1}^{1} \quad \text{and} \quad \Phi_{2} = W_{L2}^{2} \circ \rho \circ \ldots \circ \rho \circ W_{1}^{2}
$$

If we compose $\Phi_2$ with $\Phi_1$ directly, the outcome $ W_{L2}^{2} \circ \rho \circ \ldots \circ \rho \circ W_{1}^{2} \circ W_{L1}^{1} \circ \rho \circ W_{L1-1}^{1} \circ \ldots \circ \rho \circ W_{1}^{1}$ does not match the general architecture of the neural network defined earlier, because the section $W_{1}^{2} \circ W_{L1}^{1}$ does not have an activation function $\rho$ in between. Therefore, our goal is to replace the section $W_{1}^{2} \circ W_{L1}^{1}$ with something equivalent but in the form of $W \circ \rho \circ W$.

Let $N_{L1-1}^1$ denote the width of layer $L_1-1$ in $\Phi_1$ and let $N_1^2$ denote the width of layer 1 in $\Phi_2$. We define the affine transformations $\~W_{L_1}^1: ℝ^{N_{L_1-1}^1} \rightarrow ℝ^{2d_2}$ and $\~W_1^2: ℝ^{2d_2} \rightarrow ℝ^{N_1^2}$ according to

$$
\tilde{W}_{L1}^1(x):= \begin{pmatrix} I_{d_2}\\ -I_{d_2}\end{pmatrix} W_{L1}^1 (x) \quad \text{and} \quad \tilde{W}_1^2(y):= W_1^2 (\begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} y)
$$ 

Now we can show that, step by step, why $\~W_1^2 \circ \rho \circ \~W_{L_1}^1 $ is the same as $W_{1}^{2} \circ W_{L_1}^{1}$

$$\begin{align*}
\tilde{W}_{L_1}^1(x)&= \begin{pmatrix} I_{d_2}\\ -I_{d_2}\end{pmatrix} W_{L_1}^1 (x) \\ &= \begin{pmatrix} W_{L_1}^1 (x)\\ -W_{L_1}^1 (x)\end{pmatrix} \\
\rho \circ \begin{pmatrix} W_{L_1}^1 (x)\\ 
\\
-W_{L1}^1 (x)\end{pmatrix} &= \begin{pmatrix} \rho (W_{L_1}^1 (x))\\ \rho(-W_{L_1}^1 (x))\end{pmatrix} \\
\\
\tilde{W_1}^2 \circ \rho \circ \tilde{W}_{L_1}^1 &= W_1^2 (\begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} \begin{pmatrix} \rho (W_{L_1}^1 (x))\\ \rho(-W_{L_1}^1 (x))\end{pmatrix}) \\
&= W_1^2 \circ \begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} \begin{pmatrix} \rho (W_{L_1}^1 (x))\\ \rho(-W_{L_1}^1 (x))\end{pmatrix}\\
&= W_1^2 \circ (\rho (W_{L_1}^1 (x)) - \rho (-W_{L_1}^1 (x))) \\
&= W_1^2 \circ W_{L_1}^1
\end{align*}$$

Therefore, the network $\Psi = W_{L_2}^{2} \circ \rho \circ \ldots \circ \rho \circ \~W_{1}^{2} \circ \rho \circ W_{L_1}^{1} \circ \rho \circ W_{L_1-1}^{1} \circ \ldots \circ \rho \circ W_{1}^{1}$ is equivalent to $(\Phi_2 \circ \Phi_1)(x)$. And by examine the architecture of $\Psi(x)$, we notice that the claimed properties are all satisfied. 

---
<h3 id="L24"></h3>

**Lemma 2.4** Let $d_1, d_2, K \in \mathbb{N}$ and $\Phi \in N_{d_1, d_2}$ with $L(\Phi) < K$. Then, there exists a network $\Psi \in N_{d_1, d_2}$ with
* $L(\Psi) = K$, 
* $M(\Psi) \leq M(\Psi) + d_2 W(\Psi) + 2d_2(K-L(\Phi))$, 
* $W(\Psi) = \max(2d_2, W(\Phi))$, 
* $B(\Psi) = \max(1, B(\Phi))$

and satisfying $\Psi (x) = \Phi (x), \text{ for all } x \in ℝ^{d_1}$

*Proof.* Let 
$$
\begin{align*}
\tilde{W}_j(x) &:= diag \begin{pmatrix} I_{d_2} \quad I_{d_2}\end{pmatrix} x, \text{ for } j \in \{L(\Phi) + 1, \ldots, K-1\}\\
\tilde{W}_{K}(x) &:= \begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix}x,
\end{align*}
$$

and note that with

$$
\Phi = W_{L(\Phi)} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \ldots \circ \rho \circ W_1
$$

we can construct a new network

$$
\Psi := \tilde{W}_K \circ \rho \circ \tilde{W}_{K-1} \circ \rho \circ \ldots \circ \rho \circ \tilde{W}_{L(\Phi)+1} \circ \rho \circ \begin{pmatrix} W_{L(\Phi)} \\ -W_{L(\Phi)}\end{pmatrix} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1
$$

By observing that 

$$
\tilde{W}_j\begin{pmatrix} \rho(W_{L(\Phi)}) \\ \rho(-W_{L(\Phi)})\end{pmatrix} = \begin{pmatrix} \rho(W_{L(\Phi)}) \\ \rho(-W_{L(\Phi)})\end{pmatrix} \text{and } \rho(\rho(x)) = \rho(x)$$

for ReLU activation function, it can be shown that the network $\Psi$ defined above generates the same outcome as the network $\Phi$

$$\begin{align*}
\Psi &= \tilde{W}_K \circ \rho \circ \tilde{W}_{K-1} \circ \rho \circ \ldots \circ \rho \circ \tilde{W}_{L(\Phi)+1} \circ \rho \circ \begin{pmatrix} W_{L(\Phi)} \\ -W_{L(\Phi)}\end{pmatrix} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1 \\
&= \tilde{W}_K \circ \rho \circ \begin{pmatrix} W_{L(\Phi)} \\ -W_{L(\Phi)}\end{pmatrix} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1 \\
&= \begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} \circ \rho \circ \begin{pmatrix} W_{L(\Phi)} \\ -W_{L(\Phi)}\end{pmatrix} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1 \\
&= \begin{pmatrix} I_{d_2} -I_{d_2}\end{pmatrix} \circ \begin{pmatrix} \rho(W_{L(\Phi)}) \\ \rho(-W_{L(\Phi)})\end{pmatrix} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1 \\
&= (\rho(W_{L(\Phi)}) - \rho(-W_{L(\Phi)})) \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1 \\
&= W_{L(\Phi)} \circ \rho \circ W_{L(\Phi)-1} \circ \rho \circ \ldots \circ \rho \circ W_1 \\
&= \Phi 
\end{align*}$$

Next, we can check the new architecture of network $\Psi(x)$ and see that the claimed properties are indeed all satisfied.

For the sake of simplicity of expositioin, <ins>we state the following two lemmas only for networks of the same depth</ins>, the extension to the general case follows by straightforward application of **Lemma 2.4**.

---
<h3 id="L25"></h3>

**Lemma 2.5** Let $n, L \in ℕ$ and, for $i \in \{1, 2, \ldots, n\}$, let $d_i, d_i' \in ℕ$ and $\Phi_i \in N_{d_i,d_i'}$ with $L(\Phi_i) = L$. Then, there exists a network $\Psi \in N_{\sum_{i=1}^{n}d_i, \sum_{i=1}^{n}d_i'}$ with 
* $L(\Psi) = L$, 
* $M(\Psi) = \sum_{i=1}^{n} M(\Phi_i)$, 
* $W(\Psi) = \sum_{i=1}^{n} W(\Phi_i)$, 
* $B(\Psi) = max_i B(\Phi_i)$, 

and satisfying

$$
\Psi(x) = (\Phi_1(x_1), \Phi_2(x_2), \ldots, \Phi_n(x_n)) \in ℝ^{\sum_{i=1}^{n}d_i'}
$$

for tuple $x = (x_1, x_2, \ldots, x_n) \in ℝ^{\sum_{i=1}^{n}d_i}$ with $x_i \in ℝ^{d_i}, i \in ℕ$.

*Proof.*

We write the networks $\Phi_i$ as

$$
\Phi_i = W_L^i \circ \rho \circ W_{L-1}^i \circ \rho \circ \ldots \circ \rho \circ W_1^i
$$

with $W_l^i(x) = A_l^i x + B_l^i$. Furthermore, we denote the layer dimensions of $\Phi_i$ by $N_0^i, \ldots, N_L^i$ and set $N_l := \sum_{i = 1}^n N_l^i$, for $l \in \{0, 1, \ldots, L\}$ Next, define, for $l \in \{0, 1, \ldots, L\}$, the block-diagonal matrices $A_l := diag(A_l^1, A_l^2,...,A_l^n)$, the vectors $b_l = (b_l^1, b_l^2, \ldots, b_l^n)$, and the affine transformations $W_l(x) := A_l(x) + b_l$. For each layer, we can write the $W_l$ as

$$\begin{align*}
W_l(x) &= 
\begin{bmatrix} 
    A_l^1 & \dots &0 \\
    \vdots& \ddots & \vdots\\
    0 & \dots & A_l^n 
\end{bmatrix} 
\begin{bmatrix} 
x_1 \\
\vdots \\
x_n
\end{bmatrix} + 
\begin{bmatrix} 
b_1 \\
\vdots \\
b_n
\end{bmatrix} \\
&= 
\begin{bmatrix} 
A_l^1 x_1 + b_1 \\
\vdots \\
A_l^n x_n + b_n
\end{bmatrix} \\
\end{align*}$$

The proof is concluded by noting that 

$$
\Psi := W_L \circ \rho \circ W_{L-1} \circ \rho \ldots \circ \rho \circ W_1
$$

satisfies the claimed properties. 

We are now ready to <ins>formalize the concept of a linear combination of neural networks</ins>. 

---
<h3 id="L26"></h3>

**Lemma 2.6** 

Let $n, L, d' \in ℕ$ and for $i \in \{1, 2, \ldots, n\}$, let $d_i \in ℕ, a_i \in ℝ$, and $\Phi_i \in N_{d_i, d_i'}$ with $L(\Phi_i) = L$. Then, there exists a network $\Psi \in N_{\sum_{i=1}^{n}d_i,d'}$ with 
* $L(\Psi) = L$,
* $M(\Psi) \leq \sum_{i=1}^{n}M(\Phi_i)$,
* $W(\Psi) \leq \sum_{i=1}^{n} W(\Phi_i)$, 
* $B(\Psi) \leq max(\sum_{i=1}^{n}\lvert a_i \rvert B(\Phi_i), max_{i \in \{1, \ldots, n\}}\lvert a_i \rvert B(\Phi_i))$ 

and satisfying 

$$
\Psi(x) = \sum_{i=1}^{n} a_i \Phi_i(x_i) \in ℝ^{d'}
$$

for $x = (x_1, x_2, \ldots, x_n) \in ℝ^{\sum_{i=1}^{n}d_i}$ with $x_i \in \{1, 2, \ldots, n\}$.

*Proof.* The proof is effected by taking the construction in **Lemma 2.5**, replacing $A_L$ by $(a_1A_L^1, a_2A_L^2, \ldots, a_nA_L^n)$ and $b_L$ by $\sum_{i=1}^{n}a_ib_L^i$, and observing the following. For all $l \in \{1, \ldots, L-1\}$, we have $\lVert A_l \rVert_∞ \leq max_iB(\Phi_i)$ and $\lVert b_l \rVert_∞ \leq max_iB(\Phi_i)$. In addition, we note that $\lVert A_L \rVert_∞ \leq max_i(\lvert a_i \rvert B(\Phi_i))$ and $\lVert b_L \rVert_∞ \leq \sum_{i=1}^{n} \lvert a_i \rvert B(\Phi_i)$. The remaining claimed properties follow directly. 
