---
layout: default
title: Principal Component Analysis
parent: Mathematical Foundations of Computer Graphics and Vision
grand_parent: Science
nav_order: 
---

## Principal Component Analysis

PCA is a statistical technique used for dimensionality reduction, which involves transforming data from a high-dimensional space into a lower-dimensioinal space while retraining as much variance (information) as possible. 

In other words, the goal of PCA is to find a mapping from inputs in a $d$ dimensional space to a new $k < d$ dimensional space with "minimum loss of information."

The motivation for this technique is that PCA reduces the memory requirements and running time for data processing, often serving as a first step for more complex analyses. 

1. Mean Centering
    - Compute and subtract the mean of the data for each dimension to center the data around the origin

2. Covariance Matrix Computation
    - Form the covariance matrix $C$ of the centered data, which measures how much each pair of dimensions varies together
    $$
    C = \frac{1}{n} \sum_{i=1}^n x_i x_i^T
    $$

3. Eigen Decomposition
    - Compute the eigenvalues and eigenvectors of the covariance matrix. The eigenvectors (principal components) define the directions of maximum variance, and the corresponding eigenvalues indicate the magnitude of variance in those directions
    $$
    Cv_j = \lambda _j v_j
    $$
    Where $\lambda _j$ are the eigenvalues and $v_j$ are the eigenvectors of $C$.

4. Projection
    - Project the original data onto the eigenvectors. The projections onto the first few eigenvectors (those with the largest eigenvalues) capture the most significant features of the data. 
    $$
    p^{(i)} = v_1^T x^{(i)}
    $$
    where $v_1$ is the principal component, which corresponds to the direction of the highest variance in the data. It is the eigenvector associated with the largest eigenvalue $\lambda _1$. 