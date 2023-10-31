---
layout: default
title: Construct ReLU Neural Network Which Efficiently Approximate Polynomials (Part 1)
parent: Neural Network Theories
grand_parent: Science
nav_order: 
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