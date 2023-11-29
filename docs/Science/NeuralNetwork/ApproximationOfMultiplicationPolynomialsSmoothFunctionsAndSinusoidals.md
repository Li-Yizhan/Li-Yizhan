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

$$\begin{align*}
\sup_{x\in[0,1]} |x^2 - (x - I_m(x))| &= \sup_{x\in[0,1]} |x^2 - x + I_m(x)|\\
&= \sup_{x\in[0,1]} |(x-x^2) - I_m(x)|\\
&=\sup_{x\in[0,1]}|F(x) - I_m(x)| \\
&= \sup_{x\in[0,1]}|f_m(x)| \\
&= 2^{-2m-2}
\end{align*}$$

Here we can see why we previously set $F(x)$ to be $x-x^2$ instead of $x^2$. We can find the approximation error easily in this way. It paves way for the neural network realization in the next step. 

The second observation we build on is a manisfestation of the sawtooth construction described above and leads to economic realizations of the $H_k$ through k-layer networks with two neurons in each layer; a third neuron is used to realize the approximation $x-I_m$ to $x^2$. 

Concretely, let $s_k(x) := 2^{-1} \rho(x) - \rho(x-2^{-2k-1})$, and note that, for $x \in [0,1]$, $H_0 = s_0$, we get $H_k = s_k \circ H_{k-1}$. We can thus construct a network realizing $x-I_m(x)$, for $x\in[0,1]$, as follows. Let $A_1 := (1,1,1)^T\in ℝ^{3\times1}, b_1 := (0, -2^{-1}, 0)^T \in ℝ^3$,

$$
A_l := \begin{pmatrix}
2^{-1} \quad -1 \quad 0 \\
2^{-1} \quad -1 \quad 0 \\
-2^{-1} \quad 1 \quad 1
\end{pmatrix} \in ℝ^{3 \times 3}, \quad b_l := \begin{pmatrix}
0\\
-2^{-2l+1}\\
0
\end{pmatrix}, \text{ for }l\in {2, \ldots, m} 
$$

and $A_{m+1} := (-2,1, 1) \in ℝ^{1 \times 3}, b_{m+1} = 0$. 

Here is a brief explanation of the above construction. We can expand $A_1x+b_1$ in the following way:

$$\begin{align*}
A_1x + b_1 &= \begin{pmatrix} 1\\1\\1\end{pmatrix}x + \begin{pmatrix} 0\\-2^{-1}\\0\end{pmatrix} \\ &=\begin{pmatrix} x\\x-2^{-1}\\x\end{pmatrix}
\end{align*}$$

If we continue constructing the neural network with $A_2$ and $b_2$, we get:

$$\begin{align*}
A_2(\rho (A_1x + b_1)) + b_2 &= \begin{pmatrix}
2^{-1} \quad -1 \quad 0 \\
2^{-1} \quad -1 \quad 0 \\
-2^{-1} \quad 1 \quad 1
\end{pmatrix} \begin{pmatrix} \rho(x)\\\rho(x-2^{-1})\\\rho(x)\end{pmatrix}  + \begin{pmatrix} 0 \\ -2^{-3} \\0\end{pmatrix}\\
&= \begin{pmatrix}2^{-1} \rho(x) - \rho(x-2^{-2k-1})\\
2^{-1} \rho(x) - \rho(x-2^{-2k-1}) \\
-(2^{-1} \rho(x) - \rho(x-2^{-2k-1} + \rho(x)))
\end{pmatrix}+ \begin{pmatrix} 0 \\ -2^{-3} \\0\end{pmatrix}\\
&= \begin{pmatrix}2^{-1} \rho(x) - \rho(x-2^{-2k-1})\\
2^{-1} \rho(x) - \rho(x-2^{-2k-1}) -2^{-3}\\
-(2^{-1} \rho(x) - \rho(x-2^{-2k-1}) + \rho(x)))
\end{pmatrix}
\end{align*}$$

It is clear that the first rows realizes the sawtooth function $H_0$. If we consider $H_0$ as the new input $x$ for the next layer, then it is also clear that the second layer is calculating the new $x-2^{-2k-1}$. Therefore, the first two layers are indeed iteratively implementing the sawtooth function $H_k$. As for the third layer in the above equation, we find the value of $x - H_0$, which is also $x - I_1$ since $I_1 = H_0$. We can foresee that as we add more layers, the third row's value will become

$$\begin{align*}
((((x - H_0) - H_1) - H_2) - \ldots -H_{m-2}) = x - I_{m-1}
\end{align*}$$

Eventually, in the last layer, we apply $A_{m+1}$, the final outcome turns out to be

$$\begin{align*}
(-2,1, 1)\begin{pmatrix} \rho(H_{m-2})\\\rho(H_{m-2} - 2^{-2(m-2)-1}) \\ \rho(x - \sum_{k=0}^{m-2} H_k(x) )\end{pmatrix} 
&= \rho(x-\sum_{k=0}^{m-2} H_k(x)) - H_{m-1}(x) \\
&= x-\sum_{k=0}^{m-2} H_k(x) - H_{m-1}(x) \\
&= x - \sum_{k=0}^{m-1} H_k(x) \\
&= x - I_m
\end{align*}$$

Now, setting $W_l(x) := A_lx + b_l, l \in {1, 2, \ldots, m+1}$, we have

$$
\tilde{\Phi}_m := W_{m+1} \circ \rho \circ W_m \circ \rho \circ \ldots \circ \rho \circ W_1
$$

A direct calculation yields $\tilde{\Phi}_m(x) = x - \sum_{k=0}^{m-1} H_k(x)$, for $x \in [0,1]$. The proof is completed upon noting that the network $\Phi_\epsilon := \tilde{\Phi}_{\left\lceil \log(\epsilon^{-1})/2\right\rceil-1}$ satisfies the claimed properties.

$\log(\epsilon^{-1})/2 -1$ is derived from the equality $2^{-2m-2} = \epsilon$

$$\begin{align*}
\log_2(\epsilon) &= \log_2(2^{-2m-2}) \\
\log_2(\epsilon) &= -2m-2 \\
m &= -\log_2(\epsilon)/2 - 1 \\ 
&= \log(\epsilon^{-1})/2 -1
\end{align*}$$

If we graph the function about $\epsilon$, we will see that it is monotonously decreasing within the range (0, 1/2). It is intuitive, because we need denser interpolations to achieve a smaller approximation error, resulting in having more layers in our neural network model. 

The symmetry properties of $g_s(x)$ lead to the interpolation error in the proof of Proposition 2.8 to be identical in each interval, with the maximum error taken
on at the center of the respective intervals. More importantly, however, the approximating neural networks realize linear interpolation at a number of points that grows exponentially in network depth. This is a manifestation of the fact that the number of linear regions in the sawtooth construction grows exponentially with depth, which is optimal. We emphasize that the theory developed in this paper hinges critically on this optimality property of the sawtooth construction, which, however, is brittle in the sense that networks with weights obtained through training will, in general, not exhibit exponential growth of the number of linear regions with network depth. 

We proceed to the construction of networks that approximate the multiplication function over the interval $[−D, D]$. This will be effected by using the result on the approximation of $x^2$ just established combined with the polarization identity $xy =
\frac{1}{4}((x+y)^2 −(x−y)^2)$, the fact that $ρ(x)+ ρ(−x) = |x|$, and a scaling argument exploiting that the ReLU function is positive homogeneous,
i.e., $ρ(λx) = λρ(x), \text{ for all } λ ≥ 0, x ∈ ℝ$.

<h3 id="R29"></h3>

**Proposition 2.10.** There exists a constant $C > 0$ such that, for all $D \in ℝ_+$ and $\epsilon \in (0, 1/2)$, there is a network $\Phi_{D, \epsilon} \in N_{2,1}$ with $L(\Phi_{D, \epsilon}) \leq C(log(\left\lceil D\right\rceil)) + log(\epsilon^{-1})$, $W(\Phi_{D, \epsilon}) \leq 5$, $B(\Phi_{D, \epsilon}) \leq 1$, satisfying $\Phi_{0, x} = (\Phi_{x, 0}) = 0$, for all $x \in ℝ$, and 

$$
\lVert\Phi_{x, y} - xy \rVert _{L^\infty([-D,D]^2)} \leq \epsilon
$$

*Proof.* We first note that, w.l.o.g., we can assume $D \geq 1$ in the following, as for $D < 1$, we can simply employ the network constructed for $D = 1$ to guarantee the claimed properties. The proof builds on the polarization identity and essentially constructs two squaring networks according to Proposition 2.8 which share the neuron responsible for summing up the $H_k$, preceded by a layer mapping $(x,y)$ to $(|x+y|/2D, |x-y|/2D)$ and followed by layers realizing the multiplication by $D^2$ through weights bounded by 1. Specifically, consider the network $\tilde\Psi_m$ with associated matrices $A_l$ and vectors $b_l$ given by 

$$
A_1 := \frac{1}{2D} \begin{pmatrix}1 & 1 \\ -1 & -1 \\ 1 & -1 \\ -1 & 1\end{pmatrix} \in ℝ^{4 \times 2}, \quad b_1 := 0 \in ℝ^4 \\
A_2 := \begin{pmatrix}
1 & 1 & 0 & 0\\ 
1 & 1 & 0 & 0\\
1 & 1 & -1 & -1\\ 
0 & 0 & 1 & 1\\ 
0 & 0 & 1 & 1\\
\end{pmatrix} \in ℝ^{5 \times 4}, \quad b_2 := \begin{pmatrix} 0 \\-2^{-1}\\0\\0\\-2^{-1} \end{pmatrix} \\
A_l := \begin{pmatrix} 
2^{-1} & -1 & 0 & 0 & 0\\
2^{-1} & -1 & 0 & 0 & 0\\
-2^{-1} & 1 & 1 &  2^{-1} & -1\\
0 & 0 & 0 & 2^{-1} & -1\\
0 & 0 & 0 & 2^{-1} & -1\\
\end{pmatrix} \in ℝ^{5 \times 5}, \quad b_l := \begin{pmatrix} 0 \\-2^{-2l+3}\\0\\0\\-2^{-2l+3} \end{pmatrix}, \text{ for } l \in {3, \ldots, m+1},
$$

and $A_{m+2} := (-2^{-1},1,1,2^{-1}) \in ℝ^{1 \times 5}, b_{m+2} := 0$. A direct calculation yields 

$$
\tilde\Psi_m(x,y) = \frac{|x+y}{2D} 
$$

<h3 id="P210"></h3>

<h3 id="R211"></h3>

<h3 id="P212"></h3>

<h3 id="T213"></h3>

<h3 id="L214"></h3>

<h3 id="T215"></h3>

<h3 id="C216"></h3>

<h3 id="R217"></h3>
