---
layout: default
title: Approximation of Multiplication, Polynomials, Smooth Functions, and Sinusoidals
parent: Neural Network
grand_parent: Science
nav_order: 2
---

## Approximation of Multiplication, Polynomials, Smooth Functions, and Sinusoidals

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

<h3 id="P28"></h3>

<h3 id="R29"></h3>

<h3 id="P210"></h3>

<h3 id="R211"></h3>

<h3 id="P212"></h3>

<h3 id="T213"></h3>

<h3 id="L214"></h3>

<h3 id="T215"></h3>

<h3 id="C216"></h3>

<h3 id="R217"></h3>
