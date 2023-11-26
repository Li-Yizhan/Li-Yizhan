---
layout: default
title: Approximation of Multiplication, Polynomials, Smooth Functions, and Sinusoidals
parent: Neural Network
grand_parent: Science
nav_order: 2
---

## [Lecture Notes] Approximation of Multiplication, Polynomials, Smooth Functions, and Sinusoidals

---

**Table of Contents**
* [Introduction](#Intro)
* [Lemma 2.7](#L27)
* [Proposition 2.8](#P28)
* [Remark 2.9](#R29)
* [Proposition 2.10](#P210)
* [Remark 2.11](#R211)
* [Proposition 2.12](#P212)
* [Theorem 2.13](#T213)
* [Lemma 2.14](#L214)
* [Theorem 2.15](#T215)
* [Corollary 2.16](#C216)
* [Remark 2.17](#R217)

---

<h3 id="Intro"></h3>

This section deals with the approximation of basic function "templates" through neural networks. Specifically, we shall develop an algebra of neural network approximation by starting with the squaring function, building thereom to approximate the multiplication function, proceeding to polynomials and general smooth functions, and ending with sinusoidal functions. 

We start by reviewing the sawtooth construction underlying our program. Consider the hat function $g:\mathbb{R} \rightarrow [0,1]$, 

$$
g(x) = 2 \rho(x) - 4 \rho(x-\frac{1}{2})+2 \rho(x-1) = 
    \begin{cases} 
      2x, & \text{if } 0 \leq x < \frac{1}{2}\\
      2(1-x), & \text{if } \frac{1}{2} \leq x < 1
   \end{cases}
$$

let $g_0(x) = x, g_1(x) = g(x)$, and define the s-th order sawtooth function g, as the s-fold composition of g with itself, i.e., 

$$
\tag{2.2}
g_s := g \circ g \circ \ldots \circ g, \quad s \geq 2
$$

To help ourselves visualize the construction, let's take a concrete example of $g_2(x) := g \circ g$. In this case, to compose a piece-wise function of itself, we need to consider 4 possible events: 

$$
\begin{cases} 
0 \leq x < 1/2 \quad \text{ and } \quad 0 \leq g(x) < 1/2 \quad \Rightarrow \quad 0 \leq x < 1/4\\ 
0 \leq x < 1/2 \quad \text{ and } \quad 1/2 \leq g(x) < 1 \quad \Rightarrow \quad 1/4 \leq x < 1/2\\
1/2 \leq x < 1 \quad \text{ and } \quad 1/2 \leq g(x) < 1 \quad \Rightarrow \quad 1/2 \leq x < 3/4\\
1/2 \leq x < 1 \quad \text{ and } \quad 0 \leq g(x) < 1/2 \quad \Rightarrow \quad 3/4 \leq x < 1\\ 
\end{cases}
$$

Therefore, the above events can be represented as a new piece-wise function with 4 conditions:

$$
g(g(x)) = 
    \begin{cases} 
      2(2x) = 4x, & \text{if } 0 \leq x < 1/4\\
      2(1-(2x)) = 2-4x, & \text{if } 1/4 \leq x < 1/2\\
      2(1-(2(1-x))) = -2+4x, & \text{if } 1/2 \leq x < 3/4\\
      2(2(1-x)) = 4-4x, & \text{if } 3/4 \leq x < 1\\
   \end{cases}
$$

From the above example, we can see that the number of peaks grows exponentially as the order of the function increases. Geometrically, we get $2^{s-1}$ peaks for the sawtooth function $g_s, s \geq 2$.

We note that $g$ can be realized by a 2-layer network $\Phi_g \in N_{1,1}$ according to $\Phi_g := W_2 \circ \rho \circ W_1 = g$ 

with

$$
W_1(x) = \begin{pmatrix} 1\\ 1\\ 1\end{pmatrix}x - \begin{pmatrix} 0\\ 1/2\\ 1\end{pmatrix}, \qquad W_2(x) = (2 \quad -4 \quad 2)\begin{pmatrix} x_1\\ x_2\\x_3\end{pmatrix}
$$

The s-th order sawtooth function $g_s$ can be realized by a network $\Phi_g^s \in N_{1,1}$ according to

$$\begin{align*}
\Phi_g^s &= W_2 \circ \rho \circ W_1 \circ \rho \circ W_2 \circ \rho \circ W_1 \ldots W_2 \circ \rho \circ W_1 \\
         &= W_2 \circ \rho \circ W_g \circ \ldots \circ W_g \circ \rho \circ W_1 = g_s
\end{align*}$$

with

$$\begin{align*}
W_g(x) &= W_1 \circ \rho \circ W_2 \\
       &= \begin{pmatrix} 2 \quad -4 \quad 2\\ 2 \quad -4 \quad 2\\ 2 \quad -4 \quad 2\end{pmatrix} \begin{pmatrix} x_1\\ x_2\\ x_3\end{pmatrix} - \begin{pmatrix} 0\\ 1/2\\ 1\end{pmatrix}
\end{align*}$$

Lemma 2.7 summarizes the self-similarity and symmetry properties of $g_s(x)$ we will frequently make use of.

<h3 id="L27"></h3>

**Lemma 2.7.** For $s \in \mathbb{N}, k \in \{0, 1, \ldots, 2^{s-1} -1\}$, it holds that $g(2^{s-1} -k)$ is supported in $[\frac{k}{2^{s-1}},\frac{k+1}{2^{s-1}}]$,

$$
g_s(x) = \sum_{k=0}^{2^{s-1}-1} g(2^{s-1}x-k), \text{ for } x \in [0, 1]\\
$$

and

$$
g_s\left(\frac{k}{s^{s-1}}+x
\right) = g_s\left(\frac{k+1}{s^{s-1}}-x\right), \text{ for } x \in \left[0, \frac{1}{2^{s-1}}\right]
$$

The first equation demonstrates the self-similarity property while the second equation shows the symmetry property. We are now ready to proceed with the statement of the basic building block of our neural network agebra, namely the approximation of the squaring function through deep ReLU Network.

<h3 id="P28"></h3>

**Proposition 2.8** There exists a constant $C>0$ such that for all $\epsilon \in (0, 1/2)$, there is a network $\Phi_\epsilon \in N_{1,1}$ with $L(\Phi_\epsilon) \leq C \log(\epsilon^-1), W(\Phi_\epsilon) = 3, B(\Phi_\epsilon) \leq1, \Phi_\epsilon(0) = 0$, satisfying

$$
\| \Phi_\epsilon(x) - x^2\|_{L^∞([0,1])} \leq \epsilon
$$

*Proof.* The proof builds on two rather elementary observations. 

<div style="text-align:center;">
<img src="/Images/NNT23_22.jpg" alt="3TypesofRegion" 
style="width:100%; height:auto;">
</div>

>First Three Steps of Approximating $F(x) = x -x^2$ by an Equispaced Linear Interpolation $I_m$ at $2^m+1$ points

The first one concerns the linear interpolation $I_m: [0, 1] \rightarrow \mathbb{R}, m \in \mathbb{N}$, of the function $F(x) := x - x^2$ at the points $j/2^m, j \in {0, 1, \ldots, 2^m}$, and in particular the self-similarity of the refinement step $I_m \rightarrow I_{m+1}.$ (Later, we will see why we want to approximate the function $x-x^2$ in stead of $x^2$ directly). For every $m \in \mathbb{N}$, the residual $F-I_m$ is identical on each interval between two points of interpolation. Concretely, let $f_m: [0, 2^{-m}] \rightarrow [0, 2^{-2m-2}]$ be defined as $f_m(x) = 2^{-m}x-x^2$ and consider its linear interpolation $h_m: [0, 2^{-m}] \rightarrow [0, 2^{-2m-2}]$ at the midpoint and the endpoints of the interval $[0, 2^{-m}]$ given by

$$
h_m(x) := \begin{cases} 
2^{-m-1}x, &x\in [0, 2^{-m-1}]\\
-2^{-m-1}x + 2^{-2m-1}, &x\in [2^{-m-1}, 2^{-m}]
\end{cases}
$$

Direct calculation shows that 

$$
f_m(x) - h_m(x) = \begin{cases}
f_{m+1}(x), &x\in [0, 2^{-m-1}]\\
f_{m+1}(x-2^{-m-1}), &x\in [2^{-m-1}, 2^{-m}]
\end{cases}
$$

As $F = f_0$ and $I_1 = h_0$ this implies that, for all $m\in\mathbb{N}$, 

$$
F(x) - I_m(x) = f_m(x-\frac{j}{2^m}), \quad \text{for }x \in [\frac{j}{2^m}, \frac{j+1}{2^m}], \quad j\in {0, 1, \ldots, 2^m-1}
$$

and $I_m = \sum_{k=0}^{m-1} H_k$, where $H_k : [0,1] \rightarrow \mathbb{R}$ is given by 

$$
H_k(x) = h_k(x-j/2^k), \quad \text{for } x \in [\frac{j}{2^k}, \frac{j+1}{2^k}], \quad j \in {0, 1, \ldots, 2^k-1}.
$$

In general, we define the sawtooth function in each schope (with different m values) as $H_k$, with $h_k$ representing each "spike". By summing $H_k$, we get the linear interpolation $I_m$ that approximates the function $F(x) = x-x^2$. 

Since we have

$$\begin{align*}
f_0(x) - h_0(x) &= f_1(x)\\
f_1(x) - h_1(x) &= f_2(x)\\
f_2(x) - h_2(x) &= f_3(x)\\
\ldots
\end{align*}$$

we can rewrite the above equations as:

$$\begin{align*}
f_0(x) - h_0(x) - h_1(x) - h_2(x) - \ldots -h_{m-1}(x) &= f_1(x) - h_1(x) - h_2(x) - \ldots -h_{m-1}(x) \\
&= f_2(x) - h_2(x) - \ldots -h_{m-1}(x) \\
&= f_m(x)
\end{align*}$$

Due to the self-similarity property of the function, we can write the general form for $x \in [\frac{j}{2^k}, \frac{j+1}{2^k}], j\in {0, 1, \ldots, 2^k-1} $. 

$$\begin{align*}
F(x) - H_0(x) - H_1(x) - \ldots - H_{m-1}(x) &= F(x) - \sum_{k=0}^{m-1} H_k(x) \\
&= f_0(x) - \sum_{k=0}^{m-1}h_k(x-\frac{j}{2^k})\\
&= f_m(x-\frac{j}{2^k})
\end{align*}$$

Thus we have

$$
\sup_{x\in[0,1]} |x^2 - (x - I_m(x))| = \sup_{x\in[0,1]}|F(x) - I_m(x)| = \sup_{x\in[0,1]}|f_m(x)| = 2^{-2m-2}
$$



<h3 id="R29"></h3>

<h3 id="P210"></h3>

<h3 id="R211"></h3>

<h3 id="P212"></h3>

<h3 id="T213"></h3>

<h3 id="L214"></h3>

<h3 id="T215"></h3>

<h3 id="C216"></h3>

<h3 id="R217"></h3>
