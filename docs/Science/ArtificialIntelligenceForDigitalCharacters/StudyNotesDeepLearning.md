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
    - Attention:
        - Used in encoder-decoder models to dynamically focus on relevant parts of the input sequence during decoding
        - Involves computing alignment scores, attention weights, and context vectors for each decoding step
        - Helps the decoder generate contextually appropriate outputs by focusing on specific parts of the input sequence
    - Self-attention: 
        - Used within the same sequence to compute dependencies between different positions
        - Involves projecting input tokens into queries, keys, and values and computing attention scores within the sequence
        - Fundamental to Transformer models, enabling efficient parallel processing and capturing long-range dependencies

<div style="text-align:center;">
<img src="/Images/SelfAttentionLayer.png" alt="Self Attentioin Layer" 
style="width:50%; height:auto;">
</div>

>Self Attention Layer for Transformer (There is no recurrent connection)

**Attention Mechanism**
Split the input $x_i \in R^d$ in encoder (or decoder) into query, keys, and values vectors using three different matrices $W^Q, W^K, W^V$:
- Query $Q$: represents the current token or word for which we are calculating the attention. It is used to determine how much focus or attention should be placed on other tokens in the sequence. 
$q_i = W^Q x_i$
- Key $K$: represents the tokens in the sequence that the query will compare itself against to determine relevance. Each token in the sequence has an associated key that helps the model compute similarity scores with the query.
$k_i = W^K x_i$
- Value $V$: represents the actual information or content of the tokens. They are used to generate the weighted sum that becomes the new representation of the query token after attention is applied. 
$v_i = W^V x_i$
- $W^Q, W^K, W^V \in R^{d \times d}$ are learned through training.

To calculate attention:
1. Step 1: Define a similarity function $\text{sim}(q,k)$
    - Dot Product with a Weight Matrix
        - Equation: $\text{sim}(q,k) = q^TWk_t$
        - Here, $W$ is a learned weight matrix that projects the query and key into a different space before computing their dot product. This allows the model to learn an appropriate space for comparing the query and key vectors
    - Dot Product
        - Equation: $\text{sim}(q,k) = q^Tk_t$
        - The dot product measures the cosine similarity between the query and the key, assuming they are normalized. It captures the idea of how aligned or similar the two vectors are in the vector space. This is a simple yet effective way to measure similarity
    - Scaled Dot Product
        - Equation: $\text{sim}(q,k) = \frac{q^Tk_t}{\sqrt{d}}$
        - The scaled dot product includes a scaling factor $\sqrt{d}$, where $d$ is the dimensionality of the query and key vectors. The scaling factor prevents the dot product values from growing too large, which can happen when $d$ is large. This scaling helps maintain stable gradients during training
2. Step 2: Compute attention weights $a_t$
    $a_t = \frac{e^{\text{sim}(q,k_t)}}{\sum_{s=1}^T e^{\text{sim}(q,k_s)}}$ (Softmax)
    Where $k_t$ is the key vector at position $t$, while $k_s$ represents the key vectors for all positions in the input sequence, where $s$ ranges from 1 to $T$.
3. Step 3: Attend to value vectors
    $c = \sum_{t=1}^T a_t v_t$ (weighted linear combo of values)

<div style="text-align:center;">
<img src="/Images/Transformer.png" alt="Transformer" 
style="width:50%; height:auto;">
</div>

>Transformer High-level Model Illustration

Computation of queries $Q$, keys $K$, and values $V$ from the input embeddings $X$ with $N$ rows (each row is one token) and $d$ dimensionality using <ins>matrix multiplication</ins>:
$$
\begin{align*}
X &\in R ^{N \times d} \\
Q &= XW^Q \in R ^{N \times d} \\
K &= XW^K \in R ^{N \times d} \\
V &= XW^V \in R ^{N \times d}
\end{align*}
$$

<div style="text-align:center;">
<img src="/Images/AttentionMatrix.png" alt="Transformer" 
style="width:50%; height:auto;">
</div>

>Calculation of Self-Attention Matrix

- We use $-\infty$ because after applying softmax, these values will become 0.
- If the matrix is a diagonal matrix, it implies that all words are independent of each other. 
- If the matrix only has non-zero values for the first column, it implies that the first word is the most important for all other words.

**Multi-Headed Attention**
- Content-based
    - This is my big red <span style="color:red">dog, Clifford</span>
- Description-based
    - This is my <span style="color:red">big red</span> dog, Clifford
- Reference-based
    - This is <span style="color:red">my</span> big red dog, Clifford

<div style="text-align:center;">
<img src="/Images/MultiheadAttention.png" alt="Multi-Headed Attention" 
style="width:50%; height:auto;">
</div>

>Multi-Headed Attention Illustration

### Transformers

- A transformer layer is composed of an <ins>encoder</ins> and a <ins>decoder</ins>
- Both use the same building blocks

<div style="text-align:center;">
<img src="/Images/TransformerModel.png" alt="Transformer Model" 
style="width:50%; height:auto;">
</div>

>Transformer Model

**Input Embedding (Encoder)**
- Mel Spectrogram
- Waveform

**Positional Encoding (Encoder)**
- Unlike RNNs, transformers have no order
- But speech and text is left-to-right so it might be useful to tell the model that
- Positional Encoding Methods:
    - Learn position embedding during training
        - Assign position embedding vector
        - Problem: fewer training samples for later positions
    - Positional Encoding
        - Integration with Input Embedding: 
            - $e_t = e_t + PE(t,d)$
            - $e^t$ is the original input embedding at position $t$, and $PE(t)$ is the positional encoding for position $t$
        - General Form of Positional Encoding: $PE(t) = [PE(t,0), PE(t,1), \ldots, PE(t,d)]$ ($d$ is the dimensionality of the embeddings)
        - Specific Equations for Positional Encoding: 
            - $PE(t, 2i) = \sin{(t/10000^{2i/d})}$
            - $PE(t, 2i+1) = \cos{(t/10000^{2i/d})}$
            ($t$ is the position of the token in the sequence, and $i$ is the dimension index)
            - The term $10000^{2i/d}$ scales the position $t$ differently for each dimension. This ensures that each dimension $i$ has a unique positionla encoding, creating a unique pattern that the model can learn to interpret as positional information
    
**Multi-Head Attention (Encoder)**
    - Inputs $(e_1, e_2, \ldots, e_T)$, each $e_t$ is now a vector
    - Outputs $(c_1, c_2, \ldots, c_T)$ each $c_t \in R^d$

**Skip Connections (Encoder and Decoder)**
    - Mitigate Vanishing Gradients
    - Improving Gradient Flow
    - Training Deeper Networks
    - Combining Features
    - Stabilizing Training

**Layer Normalization (Encoder and Decoder)**
- The mean and variance are over the sequence of size $T$
- Not like batch norm (which is over a batch of examples). This is only on 1 example. 

**Masked Multi-Head Attention (Decoder)**
- The purpose of masking in the decoder's self-attention mechanism is to prevent the model from looking ahead at future tokens during training. 

**Multi-Head Attention (Decoder)**
- Output of encoder: $(h^{enc}, h^{enc}, \ldots, h^{enc})$
- Use this for keys and values in attention
- Query vectors come from decoder
- This blends information from encoder into the decoder
- <ins>Note:</ins> no bleeding problem here. 

**Stacked Transformers**
Stack decoder $N$ times. Each layer takes inputs from the encoder and the layers before it.

### Summary
**Neural Networks**
- Weighted sum of inputs plus non-linear activation function
- Input layer, hidden layers, output layer
- Training through backpropagation
**Recurrent Neural Networks**
- Map input sequence to output sequence
- Recurrent connections to keep a notion of time
- LSTMs can memorize longer context windows
**Transformers**
- Encoder-decoder model capturing long-term dependencies
- Through attention mechanism model can attend to different parts of input (and generated output)
- Decoded output can be sampled using different strategies (greedy search, beam search, ...)
