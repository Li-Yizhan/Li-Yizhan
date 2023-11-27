---
layout: default
title: Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)
parent: Neural Network
grand_parent: Science
nav_order: 
---

## [Assignment Solutions] Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)

---

In this (Part 1) and the following article (Part 2), the goal is to construct **ReLU neural networks** which efficiently approximate polynomials and establish **approximation rates**, which quantify the size of the approximating neural networks relative to the approximation error. 

We start by recalling the definition of ReLU neural network. 

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

The goal of this article (part 1) is to prove the following result. Instead of directly construct a neural network and approximate polynomials quantitatively, we pick a particular polynomial, $x^{2}$, as a starter. 

>**Theorem 1.** There exist constants $C>0$ and $D \in ℕ_{+}$ such that for all $	ε \in (0, 1/2)$, there is a ReLU network $\Phi_{ε}$ of depth $L(\Phi_{ε}) \leq C \log (ε^{-1})$ and width $W(\Phi_{ε}) \leq D$, such that 
>
>$$
\lVert \Phi_{ε}(x) - x^{2} \rVert_{L^{∞}([0,1])} \leq ε \text{ and } \Phi_{ε}(0) = 0, \quad \lVert \Phi_{ε}(x) \rVert_{L^{∞}([0,1])} \leq 1, \quad \lVert \Phi_{ε}(x) \rVert_{L^{∞}([0,1/2])} \leq 1/4
$$

We begin the proof by by demonstrating that <ins>every ReLU network realizes a *continuous piecewise linear function*</ins>, a function that can be represented in the following way

$$
\tag{2}
\sum_{j=1}^{N} α_{j} \rho (y_{j}^{T}x + \theta_{j}),\quad  x \in \mathbb{R}^{n}
$$

It might be hard to visualize equation (2) as a piecewise function at a glance. So, we can illustrate with a concrete example $\Phi(x) := 2 \rho(x) - \rho(x-1/2) - \rho(x-1)$. The activation function $\rho$ plays a crucial role here, in that any negative input would be considered as 0. For instance, when $x \in [0, 1/2)$:

$$
\begin{align*}
   x-1/2 &< 0 \\
   \rho(x-1/2) &= 0 \\
   \\
   x - 1 &< 0 \\
   \rho(x-1) &= 0 \\
   \\
   \Phi(x) &= 2 \rho(x) \\
   &= 2x
\end{align*}   
$$

By following a similar procedure on the intervals $[1/2, 1)$ and $[1, +∞)$, we can rewrite $\Phi(x)$ as a piecewise linear function in the conventional form

$$  
    \Phi(x) = 
    \begin{cases} 
      2x & x \in [0, 1/2) \\
      x + 1/2 & x \in [1/2, 1) \\
      3/2 & x \in [1, +∞)
   \end{cases}
$$

Meanwhile, we observe that $\Phi(x) := 2 \rho(x) - \rho(x-1/2) - \rho(x-1)$ can also be written in the form we have seen in **definition 1**

$$
W_{2} \circ \rho \circ W_{1}
$$

with $W_{1}$ and $W_{2}$ to be

$$
W_{1}(x) =  \begin{pmatrix} 1\\ 1\\ 1 \end{pmatrix} x - \begin{pmatrix} 0 \\ 1/2 \\ 1\\ \end{pmatrix}, \quad W_{2}(x) = \begin{pmatrix} 2 & -1 & -1 \\ \end{pmatrix} x
$$

We can verify by conducting the matrix composition $W_{2} \circ \rho \circ W_{1}$

$$\begin{align*}
   W_{1}(x) &= \begin{pmatrix} x \\ x - 1/2 \\ x - 1 \end{pmatrix} \\
   \rho \circ W_{1}(x) &= \begin{pmatrix} \rho (x) \\ \rho (x - 1/2) \\ \rho (x - 1) \end{pmatrix} \\
   W_{2}(x) \circ \rho \circ W_{1}(x) &= \begin{pmatrix} 2 & -1 & -1 \\ \end{pmatrix}\begin{pmatrix} \rho (x) \\ \rho (x - 1/2) \\ \rho (x - 1) \end{pmatrix} \\
   &= 2\rho(x)-\rho(x-1/2)-\rho(x-1)
\end{align*}$$

In general, a function of form (2), a piecewise linear function, can be achieved by a 2-layer ReLU network 

$$
W_{2} \circ \rho \circ W_{1}
$$

with 

$$
W_{1}(x) =  \begin{pmatrix} y_{1}^{T}\\ y_{2}^{T}\\ \ldots \\ y_{N}^{T}\\ \end{pmatrix} x + \begin{pmatrix} \theta_{1} \\ \theta_{2} \\ \ldots \\ \theta_{N}\\ \end{pmatrix}, \quad W_{2}(x) = \begin{pmatrix} \alpha_{1} & \alpha_{2} & \ldots & \alpha_{N} \\ \end{pmatrix} x
$$

Thus far, we demonstrated how a *continuous piecewise linear function* can be realized by a ReLU network. This conclusion is meaningful because <ins>we can now approximate a polynomial with ReLU network if we manage to find a piecewise linear interpolation of such polynomial</ins>.  

Now consider the approximation of $x^{2}$, a particular case of polynomial, through continuous piecewise linear functions. Specifically, for $m \in ℕ_{0}$, let $f_{m}$ be the piecewise linear function of $x^{2}$ with $2^{m}+1$ uniformly spaced "knots" according to 

$$
\tag{3}
f_{m}\left(\dfrac{k}{2^{m}}\right) = \left(\dfrac{k}{2^{m}}\right)^{2}, \quad k = 0, \ldots, 2^{m}
$$

We want to quantify the error, in other words, the difference between the function $x^{2}$ and its linear interpolation $f_{m}(x)$.

To achieve our goal, let $m \in ℕ_{0}$ and define $r_{m}(x) = f_{m}(x) - x^{2}$, for $x \in [0, 1]$. Suppose that $k \in \{1, 2, \ldots, 2^{m}\}$. By definition of $f_{m}$, we have $f_{m}(x) = x^{2}$ and $r_{m}(x) = 0$ for $x=\frac{k-1}{2^{m}}$, $\frac{k}{2^{m}}$. We know that the linearly interpolation of $x^{2}$, $f_{m}(x)$, was structured to have $2^{m} + 1$ uniformly spaced "knots" and thus $2^{m}$ intervals. We want to find one formula to represent the error $r_{m}$ on each interval. It follows from the linearity of $f_{m}(x)$ on $[\frac{k-1}{2^{m}}, \frac{k}{2^{m}}]$ that $f_{m}(x) = \frac{2k-1}{2^{m}}x + \frac{k(k-1)}{2^{2m}}$ and $r_{m}(x) = -x^{2} + \frac{2k-1}{2^{m}}x + \frac{k(k-1)}{2^{2m}}$, for $x \in [\frac{k-1}{2^{m}}, \frac{k}{2^{m}}]$, a downward parabola on each interval with $r_{m}(x) = 0$ at both ends. Formally, we say that using concaveness of $r_{m}$ yields

$$
r_{m}(x) \geq min\{r_{m}\left(\frac{k-1}{2^{m}}\right), r_{m}\left(\frac{k}{2^{m}}\right)\} = 0, \quad x \in \left[\frac{k-1}{2^{m}}, \frac{k}{2^{m}}\right]
$$

Therefore, the maximum of $\lvert r_{m}\rvert$ on $\left[\frac{k-1}{2^{m}}, \frac{k}{2^{m}}\right]$ is achieved when the maximum of $r_{m}$ on $\left[\frac{k-1}{2^{m}}, \frac{k}{2^{m}}\right]$ is achieved. 

Since $r_{m}$ is concave down, setting the derivative of $r_{m}$ to be zero establishes that the maximum of $r_{m}$ is achieved at $\frac{k-1/2}{2^{m}}$, the middle of the interval, with $r_{m}\left(\frac{2k-1}{2^{m+1}}\right) = 2^{-2m-2}$, which implies

$$
\lvert r_{m}(x) \rvert = r_{m}(x) \leq 2^{-2m-2}, \quad x \in \left[\frac{k-1}{2^{m}}, \frac{k}{2^{m}}\right]
$$

The same analysis holds for any $k \in \{1, 2, \ldots, 2^{m}\}$, and therefore

$$
\lvert f_{m}(x) - x^{2}\rvert = \lvert r_{m}(x) \rvert \leq 2^{-2m-2} \quad \forall x \in [0, 1]
$$

Now, we construct a ReLU network that realize $f_{m}$. To this end, let 

$$
\tag{4}
\Psi_{m}(x) := \frac{1}{2^{m}} \rho (x) + \sum_{i=1}^{2^{m}-1} \frac{1}{2^{m-1}} \rho \left( x - \frac{i}{2^{m}} \right)
$$

which can be considered as a 2-layer ReLU network. It is easy to check that $\Psi_{m}(0) = 0$, and that $\Psi_{m}$ and $f_{m}$ are both piecewise-linear with the same break points and slopes on each of their linear regions on [0, 1], which implies $\Psi_{m}(0) = f_{m}$, for $x \in [0, 1]$. To convince ourselves fully, let's verify with a concrete example $\Psi_{2}(x)$

$$\begin{align*}
   \Psi_{2}(x) = \frac{1}{4} \rho(x) + \frac{1}{2} \rho \left(x - \frac{1}{4}\right) + \frac{1}{2} \rho \left(x - \frac{2}{4}\right) + \frac{1}{2} \rho \left(x - \frac{3}{4}\right)
\end{align*}$$

For the above ReLU network, we have 4 $(2^{m-1} + 1 = 2^{m} = 2^{2})$ non-zero entries with activation function $\rho$ in the hidden layer. Similar to what we have done earlier, we can rewrite the ReLU network as a continuous piecewise linear function for $x \in [0, 1]$

$$  
    \Psi_{2}(x) = 
    \begin{cases} 
      \frac{1}{4}x & x \in \left[0, \frac{1}{4}\right) \\
      \frac{3}{4}x - \frac{1}{8} & x \in \left[\frac{1}{4}, \frac{1}{2}\right) \\
      \frac{5}{4}x - \frac{3}{8} & x \in  \left[\frac{1}{2}, \frac{3}{4}\right) \\
      \frac{7}{4}x - \frac{3}{4} & x \in \left[\frac{3}{4}, 1\right] \\
   \end{cases}
$$

Which is indeed idential to the 4 "knot" linear interpolation $f_{2}$. <ins>However, This construction is not optimal as the corresponding approximation error $2^{-2m-2}$ scales only polynomially with respect to (the reciprocal of) the connectivity, which is at least $2^{m}$, while **Theorem 1** requires an exponential scaling</ins>. The polynomial scaling is undesirable in that we do not want the non-zero entries of the hidden layer to expand exponentially as we decrease the error by increasing the value of m. Therefore, <ins>we need to use a different construction to improve the scaling</ins>. 

To represent the functions $f_{m}$ more economically, a better understanding of their structure is needed. For $m \in ℕ_{+}$, define

$$
h_{m}(x) := f_{m-1}(x) - f_{m}(x), \quad x \in [0, 1]
$$

Consider the function $g: [0, 1] \rightarrow [0, 1]$

