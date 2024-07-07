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

## Projections and Variance

The projection of a point $x^{(i)}$ in $R^d$ onto the eigenvector $v_j$ (principal component) is given by:

$$
p_j^{(i)} = v_j^T x^{(i)}
$$

Here, $p_j^{(i)}$ is the scalar projection of the data point $x^{(i)}$ onto the principal component $v_j$.

Since the data has been mean-centered (the mean of each feature has been subtracted), the average of the projections over the entire dataset is zero. This is expressed as:

$$
E[v_j^T x^{(i)}] = v_j^T E[x^{(i)}] = 0
$$

This equation states that the expected value (mean) of the projections is zero, which follows from the fact that the data is centered around the origin

The variance of the projections onto $v_j$ is calculated to measure how much the data varies along this principal component:

$$

$$