---
layout: default
title: RANSAC
parent: Mathematical Foundations of Computer Graphics and Vision
grand_parent: Science
nav_order: 
---

## RANSAC

RANSAC - RANdom SAmple Consensus - is an iterative method used for robust fitting of models in the repsence of outliers. It aims to **maximize the number of inliers** by random sampling. 

## How RANSAC Works

1. Select Random Subset 
    - Randomly select a subset of the original data points. This subset should be large enough to fit the model of interest
2. Fit Model
    - Fit the model to the selected subset of points
3. Evaluate Model
    - Determine how many points from the entire dataset fit the model within a predefined tolerance (inliers)
4. Repeat
    - Repeat the process for a fixed number of iterations or until a satisfactory model is found
5. Select Best Model
    - The best model is the one with the highest number of inliers

## RANSAC Iterations

Notations: 

- $p$: probability that at least one sample has no outliers ("success rate")
    - i.e. The selected points are all inliers at least once, usually set to 0.99
- $\epsilon$: outlier ratio
- $s$: simple size (minimum data)
    - e.g. $s=2$ for line fitting, $s=3$ for circle (we need at least 3 points to determine a circle)

Derivations:
- Probability that the $s$ selected points at an iteration are all inliers: $(1-\epsilon)^s$
- Probability that at least one of the $s$ points is an outlier: $1 - (1-\epsilon)^s$ 
    - The complement of the probaility that all $s$ points are inliers
- Repeating over $N$ iterations: $(1 - (1-\epsilon)^s)^N$
- To ensure that we have at least one successful iteration where all selected points are inliers with probability $p$, we set $(1 - (1-\epsilon)^s)^N = 1-p$
    - This equation ensures that the probability of not having a pure inlier set in all $N$ iterations is equal to $1-p$

Therefore, we can determine how many iterations $N$ required for our RANSAC algorithm to robustly fit a model in the presence of outliers: 

$$
N = \frac{log(1-p)}{log(1-(1-\epsilon)^s)}
$$

## RANSAC Limitations

- Probabilistic behavior
    - Different runs might lead to different results

- Number of Iterations
    - It can be challenging to determine the optimal number of iterations required to achieve a high probability of finding a good model
- Hypothesizes only models directly supported by the samples
    - The algorithm generates models based on subsets of the data points. This means that if the selected subsets are not representative of the best model, the final model may not be optimal
    - The success of RANSAC depends on the identification of inliers for each sampled model. If the inliers are not correctly identified, the model quality can degrade
- No guarantee to obtain the **optimal** solution.

