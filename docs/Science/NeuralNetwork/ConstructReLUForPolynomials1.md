---
layout: default
title: Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)
parent: Neural Network
grand_parent: Science
nav_order: 
extra_dependencies: ["amsmath", "amssymb"]
---

### Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)

In this and the following article, the goal is to construct **ReLU neural networks** which efficiently approximate polynomials and establish **approximation rates**, which quantify the size of the approximating neural networks relative to the approximation error. 

We start by recalling the definition of ReLU neural network. 

**Definition 1.** Let $ L \in \mathbb{N} $ and $ N_{0}, N_{1}, \ldots, N_{L} \in \mathbb{N} $ given by

$$  
    \Phi = 
    \begin{cases} 
      W_{1} & L = 1 \\
      W_{2} \circ \rho \circ W_{1} & L = 2 \\
      W_{L} \circ \rho \circ W_{L-1} \circ \rho \ldots \circ \rho \circ W_{1} & L \geq 3
   \end{cases}
$$

$ where, for l \in \left\{ 1, 2, \ldots, L\right\}$, 





