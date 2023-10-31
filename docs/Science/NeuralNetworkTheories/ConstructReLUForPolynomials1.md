---
layout: default
title: Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)
parent: Neural Network Theories
grand_parent: Science
nav_order: 
---

## Neural Network Theories 1 - Setup and Basic ReLU calculus

---

**Definition 2.1.** Let $ L \in \mathbb{N} $ and $ N_{0}, N_{1}, \ldots, N_{L} \in \mathbb{N} $ given by

\[  
    \tag{2.1}
    \Phi = 
    \begin{cases} 
      W_{1} & L = 1 \\
      W_{2} \circ \rho \circ W_{1} & L = 2 \\
      W_{L} \circ \rho \circ W_{L-1} \circ \rho \ldots \circ \rho \circ W_{1} & L \geq 3
   \end{cases}
\] 

where, for $ l \in \left\{ 1, 2, \ldots, L\right\} $, $ W_{l}: \mathbb{R}^{N_{l-1}} \rightarrow \mathbb{R}^{N_{l}} $, $ W_{l}(x) := A_{l}x + b_{l} $ are the affine transformations with matrices $A_{l} \in \mathbb{R}^{N_{l} \times N_{l-1}} $ and (bias) vectors $ b_{l} \in \mathbb{R}^{N_{l}} $, and the ReLU activation function $ \rho: \mathbb{R} \rightarrow \mathbb{R}, \rho(x) := max(x, 0) $ acts component-wise. We denote by $ \mathcal{N}_{d,d'} $ the set of all ReLU networks with input dimension $ N_{0} = d $ and output dimension $ N_{L} = d' $. Moreover, we define the following quantities related to the notion of size of the ReLU network $ \Phi $:

- *connectivity* $ \mathcal{M}_{\Phi} $ : the total number of non-zero entries in the matrices $ A_{l}, l \in \left\{{1, 2, \ldots, L} \right\}$, and the vectors $ b_{l}, l \in \left\{{1, 2, \ldots, L} \right\} $

- *depth* $ \mathcal{L}(\Phi) := L$

- *width* $ \mathcal{W}(\Phi) := max_{l=0,\ldots,L}N_{l}$

- *weight manitude* $\mathcal{B}(\Phi) := max_{l=1,\ldots,L} max\left\{\left\| A_{l}\right\|_{\infty},\left\|b_{l}\right\|_{\infty}\right\}$