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
        Where the label $y$ for each instance is typically represented as a one-hot encoder vector. 
- Backward pass
    - Chain Rule
    $f(x) = u(v(x))$
    $\frac{df}{dx} = \frac{du}{dv} \frac{dv}{dx}$
    - Update Weights Using Chain Rule
    $\frac{\partial{L}}{\partial{w_i}} = \frac{\partial{L}}{\partial{y}}\frac{\partial{y}}{\partial{z}}\frac{\partial{z}}{\partial{w_i}}$ 
    $w^{t+1} = w^t - h \frac{\partial{L}}{\partial{w}}$

**Application**
- Sentiment Classification
    - Goal is to classify the sentiment as positive, negative, or neutral based on the text's content
    - Assumes a fixed size length
        - Make the input the length of the longest text
            - Padding with zero embeddings
            - Truncate 
        - Create a single "sentence embedding" (the same dimensionality as a word) to represent all the words (Example simplified word embedding: $[0.2, 0.5, 0.1]$)
            - Take the mean of all the word embeddings
            - Take the element-wise max of all the word embeddings (For each dimension, pick the max value from all words)
- Language Model 
    - Goal is to predict the probability of a sequence of words

### Recurrent Neural Networks

- Input: $x_t$
- Output: $y_t$
- Trainable Parameter (weights): $U, V, W$
    - Shared over all timesteps (<span style="color:red">same one for each timestep</span>)
- Forward Pass: 
    - map $x_t$ to a "hidden state" $h_t$ (a real-valued vector)
    - Use $h_{t-1}$ and $x_t$ to predict $y_t$
    $h_t = \sigma(U h_{t-1} + W x_t)$
    $y_t = f(V h_t)$
- Backpropagation through time (BPTT)
    - Loss Function (<ins>Minimize the cumulative cross-entropy loss over all time steps</ins>)
    $J(x, y, \theta) = -\sum_{t} \log p(y_t \mid x_1, x_2, \ldots, x_t)$ 
    $J(x, y, \theta) = -\sum_{t} \sum_{i} y_t^{(i)} \log(\hat{y}_t^{(i)})$
    Where $\log p(y_t \mid x_1, x_2, \ldots, x_t)$ is the log probability of the true output $y_t$ given the input sequence up to time $t$.

<div style="text-align:center;">
<img src="/Images/RNN.png" alt="Recurrent Neural Network" 
style="width:50%; height:auto;">
</div>

>Recurrent Neural Network Illustration

**RNNs Applications**

- Language Model
    - Predict next word from current word and previous hidden state 
    - Input sequence is a series of word embeddings (one-hot vectors)
    - Output sequence is a series of probability distributions over the vocabulary
    - Probability of a sequence is product of probabilities of each item in sequence
    - Teacher forcing for training: Provide correct history sequence to predict next word

<div style="text-align:center;">
<img src="/Images/RNNLanModel.png" alt="Recurrent Neural Network Language Model Application Example" 
style="width:50%; height:auto;">
</div>

>RNN Application for Language Model

- Sequence Classification (Assigning a label to an entire sequence of data)
    - Sentiment Classification
    - Spam Detection
    - Topic Classification
    - <ins>Only hidden layer for last token of text used</ins>

<div style="text-align:center;">
<img src="/Images/RNNSeqClassification.png" alt="Recurrent Neural Network Sequence Classification Application Example" 
style="width:50%; height:auto;">
</div>

- Generation
    - Autoregressive Generation: Repeatedly sampling next word conditioned on previous words
    - Start with $<s>$ and sample word from output distribution
    - Generate more words
    - Stop when $</s>$ or length limit is reached
    - Provide appropriate context

>RNN Application for Sequence Classification

**Different Types of RNNs**
- Stacked RNNs (deep RNNs)
    - Multiple Layers (Increased Capacity)
    - Enhanced Representation
    - Improved Performance
- Bidirectional RNNs
    - Two Separate RNNs (Left-to-right and right-to-left)
    - Combining Forward and Backward States (e.g., concatenated or averaged)
    - Enhanced Contextual Understanding
- Long Short Term Memory (LSTM)
    - Problem: Information encoded in hidden states tend to be local
        - Hidden layers provide information for current decision and future decisions
        - Vanishing gradients (repeated multiplications drive gradient to zero)
    - LSTMs have the ability to "forget" information and "store" information that could be useful later
        - Adding contect layer
        - Gates to control the flow of information
            - Forget Gate
                - Decides what information from the previous cell state should be discarded
                - Equation: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$
                - Results in a vector $f_t$, with values between 0 and 1, where values close to 0 mean "forget this information" and values close to 1 mean "keep this information"
            - Add Gate (Input Gate)
                - Decides what new information should be added to the cell state
                - Consists of two parts: the input gate and the candidate value
                - Equations: 
                $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$
                $\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$
                - The input gate $i_t$ determines which values will be updated, while $\tilde{C}_t$ is the candidate value, representing new information to be added to the cell state. The candidate value is calculated using tanh activation function to ensure the values are between -1 and 1. (Maintaining numerical stability during training)
            - Cell State Update
                - Updates the cell state $C_t$ based on the forget gate and input gate
                - Equation: $C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$
                - The new cell state $C_t$ is a combination of the old cell state $C_{t-1}$, scaled by the forget gate $f_t$, and the new candidate values $\tilde{C}_t$, scaled by the input gate $i_t$.
            - Output Gate
                - Decides what information from the cell state should be output
                - Equations: 
                $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$
                $h_t = o_t * \tanh(C_t)$
                - The output gate $o_t$ determines which parts of the cell state $C_t$ are output as the hidden state $h_t$. The cell state is passed through a tanh activation function to limit the values between -1 and 1, and then element-wise multiplied by the output gate values. 


<div style="text-align:center;">
<img src="/Images/NNCompare.png" alt="NN Comparison" 
style="width:50%; height:auto;">
</div>

>Difference between FNN, RNN, and LSTM

### Encoder-Decoder Models

- Two different RNNs glue'd together (separate parameters)
- One of them encodes $(x_1, x_2, \ldots, x_T)$ into a summary vector $h_t$ (context)
- The other one uses $h_t$ to initialize a language model (word by word generation)
- <ins>Output sequence can be of different length than input sequence</ins> (On the contrary, RNN typically process input sequences and generates output sequences of the same length)
- Encoder and Decoder: 
    - LSTMs
    - CNNs
    - Transformers
- Applications (sequence-to-sequence tasks)
    - Summarization
    - Dialogue
    - Translation
        - Inferece: Use estimated output at $x_t$ as input to next time step $x_{t+1}$
        - Training: Use correct gold value at $x_t$ as input to next time step $x_{t+1}$ (teacher forcing)

*Inference is the process of using a trained model to make predictions on new, unseen data, while Training is the process where a machine learning model learns from data.*

<div style="text-align:center;">
<img src="/Images/EDModel.png" alt="Encoder Decoder Model" 
style="width:50%; height:auto;">
</div>

>Encoder Decoder Model

### Attention

Q: What is the problem with RNNs?
A: The context vector is a fixed-length representation of the entire input sequence, regardless of its length. When the input sequence is long, summarizing all the information into a single fixed-length vector can be insufficient, leading to information loss. Transformers with Attention mechanism overcomes the aforesaid problem. 

- <span style="color:red">Holy Grail: </span> capturing long term dependencies
    - Vanishing gradient problem & local dependency of RNNs
    - Attention gets at this more directly (and simply)

<div style="text-align:center;">
<img src="/Images/EDInference.png" alt="Encoder Decoder Inference Model" 
style="width:50%; height:auto;">
</div>

>For Encoder Decoder Model, context vector is the last hidden state

<div style="text-align:center;">
<img src="/Images/AttentionModel.png" alt="Attention Model" 
style="width:50%; height:auto;">
</div>

>For Attention Mechanism, context vector considers the encoder weight for each hidden state. 

**Attention**
- Transformers are not based on recurrent connections (like RNNs)
    - Vanilla transformer does not have any notion of the positions of tokens in input
- Two types of attention
    - Attention of input in decoder to inputs in encoder
    - Self-attention: Attention of input in encoder (decoder) to other inputs in encoder (decoder)

### Transformers