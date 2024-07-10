---
layout: default
title: Study Notes  - Deep Learning
parent: Artificial Intelligence for Digital Characters
grand_parent: Science
nav_order: 2
---

# Study Notes - Deep Learning

### Neural Network Review

**Neural Network Unit**
- Input layer $x_i$
- Weights $w_i$
- bias $b$
- Weighted sum $z = b + \sum_i w_ix_i = wx + b$
- Non-linear activation function $a = \sigma(z)$
    - Sigmoid
    - tanh
    - ReLU
- Output value $y = a$

**Feedforward Neural Networks**

<div style="text-align:center;">
<img src="/Images/NeuralNetworkFeedForward.png" alt="Feedforward Neural Network" 
style="width:50%; height:auto;">
</div>

>Feedforward Neural Network Example

Softmax:
- Can be used for output data in the context of classification problems involving multiple classes. 
- Converts a vector of raw scores into a probability distribution over multiple classes. 
- The output probabilities from the softmax function sum to 1, making them interpretable as probabilities.

$$
\sigma(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

Where $z_i$ is the raw score for the $i$-th class class

**Training**
- Training Instance
- Forward Pass
    - System Output
    - Actual Answer
    - Loss Function
        - Binary Cross-entropy Loss (Binary Classification)
        $L_{CE}(\hat{y},y) = -[y \log(\hat{y}) + (1-y)\log{(1-\hat{y})}]$
        Where $\hat{y}$ is the predicted probability of the positive class (output of the sigmoid function) and $y$ is the actual binary label (0 or 1).
        - Categorical Cross-entropy Loss (Multi-class Classification)
        $L_{CCE}(\hat{y},y) = - \sum_i y_i \log{(\hat{y_i})}$
- Backward pass
    - Chain Rule
    $f(x) = u(v(x))$
    $\frac{df}{dx} = \frac{du}{dv} \frac{dv}{dx}$
    - Update Weights Using Chain Rule
    $\frac{\partial{L}}{\partial{w_i}} = \frac{\partial{L}}{\partial{y}}\frac{\partial{y}}{\partial{z}}\frac{\partial{z}}{\partial{w_i}}$ 
    $w^{t+1} = w^t - h \frac{\partial{L}}{\partial{w}}$

**Application**

### Recurrent Neural Networks

### Encoder-Decoder Models

### Attention

### Transformers