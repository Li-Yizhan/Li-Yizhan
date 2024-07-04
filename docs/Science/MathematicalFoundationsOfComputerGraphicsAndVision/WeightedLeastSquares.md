---
layout: default
title: Weighted Least Squares
parent: Mathematical Foundations of Computer Graphics and Vision
grand_parent: Science
nav_order: 
---

## Weighted Least Squares

The **Ordinary Least Squares** method aims to minimize the usm of squared residuals (errors). The problem can be formulated as: 

$$
\arg \min_{\mathbf{x}} \sum_{i=1}^{m} (A_i \mathbf{x} - b_i)^2 = \arg \min_{\mathbf{x}} \sum_{i=1}^{m} e_i^2
$$

The **Weighted Least Squares** method assigns a weight to each residual, which is inversely proportional to the **variance** of the corresponding observation's error term. This method ensures that observations with higher variance (less reliable) have less influence on the fitted model, while observations with lower variance (more reliable) have more influence. 

$$
\arg \min_{\mathbf{x}} \sum_{i=1}^{m} \frac{1}{\sigma_i^2} (A_i \mathbf{x} - b_i)^2 = \arg \min_{\mathbf{x}} \sum_{i=1}^{m} \frac{1}{\sigma_i^2} e_i^2
$$

## Why Weighted Least Squares?

Advantages:
- Regression in situations where data points are of varying quality
- Can handle non-constant standard deviation of the random errors in the data cross all levels of the explanatory variables

Disadvantages:
- In real life applications, weights are unknown and using estimated weights "breaks" the assumptions
- Can increase the influence of an outlier