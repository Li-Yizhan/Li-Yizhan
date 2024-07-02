---
layout: default
title: Fitting and Norm
parent: Mathematical Foundations of Computer Graphics and Vision
grand_parent: Science
nav_order: 
---

## What is Fitting?

**Fitting** refers to the process of finding a mathematical model that best describes a set of observed data points. This involves determining the parameters of the model such that the difference between the observed data and the model's predictions is minimized. 

It plays a crucial role in various computer vision tasks including:
- Object Detection and Recognition
- Camera Calibration
- Motion Tracking
- 3D Reconstruction
- Image Segmentation

## Line Fitting

**Line fitting** (or linear regression) is a specific type of fitting where the goal is to find the best-fitting straight line through a set of data points.

- Input: a set of $n$ 2D points $(x_i, y_i)$
- Output: the line $y = ax + b$ minimizing the fitting error

<div style="text-align:center;">
<img src="/Images/BestFittingLineExample.png" alt="Best Fitting Line Example" 
style="width:50%; height:auto;">
</div>

>Best Fitting Line Example

## Fitting Cost and Norms

In mathematical terms, a **norm** is a function that assigns a non-negative length or size to vectors in a vector space. In the context of fitting, the choice of norm determines how the fitting error is measured, leading to different optimization obectives and thus different fitting results. 





