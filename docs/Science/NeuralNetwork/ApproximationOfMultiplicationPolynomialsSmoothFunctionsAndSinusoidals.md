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
      2(1-x), & \text{if } \frac{1}{2} \leq x < 1\\
      0, & \text{else }
   \end{cases}
$$

let $g_0(x) = x, g_1(x) = g(x)$, and define the s-th order sawtooth function g, as the s-fold composition of g with itself, i.e., 

$$
\tag{2.2}
g_s := g \circ g \circ \ldots \circ g, \quad s \geq 2
$$

We note that $g$ can be realized by a 2-layer network $\Phi_g \in N_{1,1}$ according to $\Phi_g := W_2 \circ \rho \circ W_1 = g$ 

with

$$
W_1(x) = \begin{pmatrix} 1\\ 1\\ 1\end{pmatrix}x - \begin{pmatrix} 0\\ 1/2\\ 1\end{pmatrix}, \qquad W_2(x) = (2 \quad -4 \quad 2)\begin{pmatrix} x_1\\ x_2\\x_3\end{pmatrix}
$$

<h3 id="L27"></h3>

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
