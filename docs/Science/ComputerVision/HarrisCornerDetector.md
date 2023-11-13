---
layout: default
title: Harris Corner Detector 
parent: Computer Vision
grand_parent: Science
nav_order: 
---

## Harris Corner Detector

---

The Harris Corner Detector is a keypoint localization mathod used in computer vision to identify interest points or corners in an image. Developed by Chris Harris and Mike Stephens in 1988, the Harris Corner Detector is particularly useful for feature detection and matching, which are crucial tasks in various computer vision applications, such as object recognition, image stitching, and tracking.

If we consider an image as a 2-D matrix, and let the value of each matrix element representing the intensity of each pixel, we can observe the pixel patterns by taking the derivative of the image and observing the intensity change in horizontal and vertical directions. Here is an illustration showing how we can calculate image derivatives in a 1-D scenario:

<div style="text-align:center;">
<img src="/Images/ImageDerivativeIlustration.png" alt="Illustration of Image Derivatives" 
style="width:50%; height:auto;">
</div>

<center>Image Derivatives</center>

</p>

In computer vision, a patch refers to a small, rectangular or square region extracted from an image. Patches allow for the capture of local information and details. In addition, patches provide a form of translation invariance. By analyzing local regions, the feature extraction process becomes less sensitive to the aobsolute position of objects withint the image. 

In general, we can find three types of pixel pattern within a patch: 
* Flat region: no change in all directions
* Edge region: no change along the edge direction
* Corner region: significant change in all directions

<div style="text-align:center;">
<img src="/Images/ThreeTypesOfRegion.png" alt="3TypesofRegion" 
style="width:100%; height:auto;">
</div>

<center>Three Types of pixel pattern</center>

</p>

Now consider shifting the patch by $(u,v)$. We compare each pixel before and after by summing up the squared differences (SSD) and define that to be the SSD Error $E(u,v)$ with the equation

$$\begin{align*}
E(u,v) &= \sum_{(x,y) \in W}[I(x+u, y+v)-I(x,y)]^2\\
&≈ \sum_{(x,y) \in W}\left[[I_x \quad I_y]\begin{bmatrix} u \\v \end{bmatrix} \right]^2 \\
&= \sum_{(x,y) \in W} [u \quad v] \begin{bmatrix} I_x^2 \quad I_xI_y \\ I_yI_x \quad I_y^2 \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix}
\end{align*}$$ 

To understand the above equation, let's have a quick review of [Taylor Series](https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=156s), which is largely used to approximate non-polynomial functions with polynomials, because polynomials tend to be much easier to deal with. 

Essentially, Taylor Series approximation takes the information of different order derivatives at a single point and translating that into information about the value of the function near that point. The number of the series determines the number of control terms we want for the approximation. 

The generalization of taylor series  approximating functions at origin can be written as: 

$$
P(x) = f(0) + \frac{df}{dx}(0)\frac{x^1}{1!} + \frac{d^2f}{dx^2}(0)\frac{x^2}{2!}+\frac{d^3f}{dx^3}(0)\frac{x^3}{3!} \ldots
$$

The first term in the above equation, the constant term, ensures that the value of the polynomial approximation $P$ at origin matches that of the function $F$. The second term ensures the slope the the polynomial approximation $P$ at origin matches that of the function $F$ and so on so forth. 

For approximation of the function at the point $a$, the formula becomes:

$$
P(x) = f(a) + \frac{df}{dx}(a)\frac{(x-a)^1}{1!}+\frac{d^2f}{dx^2}(a)\frac{(x-a)^2}{2!}+ \ldots
$$

