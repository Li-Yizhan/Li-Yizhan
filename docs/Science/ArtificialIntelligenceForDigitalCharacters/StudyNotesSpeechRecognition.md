---
layout: default
title: Study Notes - Speech Recognition
parent: Artificial Intelligence for Digital Characters
grand_parent: Science
nav_order: 3
---

# Study Notes - Speech Recognition

### Phonetics

**Phones**
- Speech sounds, each represented with symbols
- String of phones: Pronunciation of a word
- [ARPAbet](https://en.wikipedia.org/wiki/ARPABET), [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet): Alphabets for transcriting American English phonetic sounds

**Prosody**
- Prosody is the study of the <ins>intonational</ins> and <ins>rhythmic</ins> aspects of language
- Based on frequency, energy (loudness) and duration of words
- Important for discourse structure (statements vs. questions) and affective meaning (happiness, surprise, anger)
-Three Aspects of Prosody:
    - <span style="color:red">Prominence:</span> some syllables/words are more prominent than others (louder, slower, varying frequency)
        - Accenting
        - Lexical Stress
    - <span style="color:red">Structure/boundaries:</span> sentences have prosodic structure
        - Some words group naturally together
        - Others have a noticeable break or disjuncture between them
    - <span style="color:red">Tune:</span> the intonational melody of an utterance
        - Statements (final fall) vs. questions (final rise)
        - Expressing contradiction

**Acoustic Signals: Sine and Cosine**
- Frequency $f = 10 Hz$ (cycles per second)
- Amplitude $A = 1$ (max value on y axis)
- Period $T = 1 / f = 0.1s$ (time for one cycle)

$$
y = A sin(2 \pi ft)
$$

**Speech Sound Waves**

<div style="text-align:center;">
<img src="/Images/WaveformVowel.png" alt="One Heart Beat" 
style="width:50%; height:auto;">
</div>

>Waveform of the vowel [iy] 

- Frequency: 10 repetitions / .03875 seconds = 258 Hz
- Change in air pressure over time (Pascals Pa) (Acount of compressioin of air molecules at a plate)
- Analog-to-digital conversion: Sampling and Quantization
    - Nyquist frequency: maximum frequency for a given sampling rate (10,000 Hz frequency -> 20,000 Hz sampling rate)
    - Quantization: Representing real-valued numbers as integers

**Pitch**
- <span style="color:red">Pitch is not frequency</span>
- Pitch and Frequency
    - Perceptual Nature of Pitch: Pitch is how we perceive the frequency of a sound. It is subjective and can vary from person to person
    - F0: The fundamental frequency is the lowest frequency of a periodic waveform and determines the perceived pitch of the sound
- Relationship between pitch and F0:
    - Linear Below 1000 Hz: In the lower frequency range (100 Hz to 1000 Hz), pitch perception is approximately linear. This means that changes in frequency result in proportional changes in perceived pitch
    - Logrithmic Above 1000 Hz: In higher frequencies (above 1000 Hz), pitch perception follows a logarithmic scale. This means that each octave (doubling of frequency) is perceived as a constant interval in pitch, regardless of the starting frequency.
- Mel scale 
    - Purpose: The Mel scale translates the linear frequency scale into a scale that aligns more closely with human perception
    - Conversion Formula: 
    $M(f) = 1127 \ln{(1 + \frac{f}{700})}$
    - Mel scale is important for speech recognition

**Intensity**
- Average of square of amplitude (dB)
- Relationship between intensity and loudness is <ins>not linear</ins>
    - Greater resolution in the low-power range
    - Depending on frequency range

**Interpretation of Phones from a Waveform**

<div style="text-align:center;">
<img src="/Images/PhonesWaveform.png" alt="Phones Waveform" 
style="width:50%; height:auto;">
</div>

>Waveforms for Different Phones

- Note that vowels [a, e, i, o, u] all have regular amplitude peaks
- Stop consonant [p, b, t, d, k, g]
    - Closure followed by release
    - Notice the silence followed by slight burst of emphasis
- Fricative consonant: noisy [f, v, s, z, sh, zh]

**Frequency Domain**

<div style="text-align:center;">
<img src="/Images/Spectrogram.png" alt="Spectrogram" 
style="width:50%; height:auto;">
</div>

>Spectrograms for Different Phones

- Every complex wave can be represented as a sum of many sine waves of different frequencies
- Spectrum: Frequency components and amplitudes of a signal 
- Phones have characteristic spectral signatures (peaks)
- Spectral representations important for speech recognition
- Spectrogram (frequencies over time)
    - Time (x-axis)
    - Frequencies (y-axis)
    - Color Coding (amplitude)

**Praat**
- Software for analysis of speech
    - Spectral Analysis
    - Formant Analysis
    - Pitch Tracking

### Feature Extraction

**Pre-Empasis Filter**
- High-pass filter: 
    - Amplifies the high-frequency components of the signal while reducing the low-frequency components
    - Effects of filter:
        - Balancing the frequency spectrum
        - Avoiding numerical problems during Fourier transform
        - Improving Signal-to-Noise Ratio (SNR)
    - Equation: $y(t) = x(t) - \alpha x(t-1) \quad \alpha \in [0.9, 1.0]$

**Windowing**
- Frequency in a signal change over time
- Frequencies in a signal stationary over short period of time
- Frame: Speech in a window
- Parameters:
    - Window size: typically between 20 ms to 40 ms
    - Stride of window: typically 50% (+/- 10%)
    - Shape of window
        - Rectangular Window
        - Hamming Window
            - Formula: $w(n) = 0.54 - 0.46 \cos{(\frac{2 \pi n}{N - 1})} \quad 0 \leq n \leq N-1$ ($n$ is the index of sample, and $N$ is the total number of samples)
            - Minimizes discontinuities
            - Reduces amplitude of the side lobes in the frequency spectrum. This helps in minimizing spectral leakage, which occurs when the signal's energy spreads into adjacent frequency bins.

<div style="text-align:center;">
<img src="/Images/Window.png" alt="Window" 
style="width:50%; height:auto;">
</div>

>Rectangular Window vs. Hamming Window

**Discrete Fourier Transform**
- Extract spectral information for each window
- Discrete Fourier transform (DFT): 
    - $X_k = \sum_{n=0}^{N-1} x_n e^{-j \frac{2\pi}{N} kn} \quad \text{for } k = 0, 1, \ldots, N-1$
    - $x(n)$: signal with $N$ frames
    - $k$: Frequency bin, typically $k = 256$ or $512$
    - $X(k)$: Complex number representing magnitude and phase of frequency $k$. 
- Fast Fourier Transform (FFT)
    - Very efficient calculation of DFT
    - Works only for values of $N$ that are powers of 2

<div style="text-align:center;">
<img src="/Images/SignaltoSpectrum.png" alt="Signal to Spectrum" 
style="width:50%; height:auto;">
</div>

>Signal to Spectrum

- Frequency Resolution:
    - $Δf = \frac{f_{sample}}{N}$
- Mapping to Frequency:
    - $f_k = kΔf = k \frac{f_{sample}}{N}$ 
        - $k$: The index that represents the specific frequency bin in the DFT output
        - $f_k$: Frequency corresponding to $X(k)$
        - $f_{sample}$: Sampling rate of the signal$
- Power spectrum: 
    - Represents the power at the k-th frequency bin
    - $P(k) = \frac{|X(k)|^2}{N}$

**Mel Filter Bank**
- Roughly uniformly spaced before 1 kHz, and logarithmic scale after 1kHz 
- The Mel filter bank effectively reduces the dimensionality of the spectral data while retaining the most important perceptual information
- We have values $P(k), k: 1, \ldots, K$
- Apply triangular filters on a Mel-scale (closer together at lower frequencies and further apart at higher frequencies) to extract frequency bands
- Take the log of each of the mel spectrum values
- The purpose is to extract perceptually relevant features from audio signals

<div style="text-align:center;">
<img src="/Images/MelFilterBank.png" alt="Mel Filter Bank" 
style="width:50%; height:auto;">
</div>

>Mel Filter Bank and Illustration of Signal Filtering

How to Construct Mel Filter Bank:
1. Convert lower and upper frequency to Mels (Mels = $1127 \ln{(1 + f/700)}$)
2. Space points linearly between lower and upper frequency (e.g., for 10 filterbanks, add 10 additional points)
3. Convert points back to Hertz: $f = 7-(10^\frac{Mel}{1127}-1)$
4. Round frequencies to nearest FFT bin
5. Create filterbanks (First filterbank starts at first point, peaks at second point and returns to zero at third point etc.)
$$
H_m(k) = \begin{cases} 
      0 & \text{if } k < f(m-1) \\
      \frac{k - f(m-1)}{f(m) - f(m-1)} & \text{if } f(m-1) \leq k \leq f(m) \\
      \frac{f(m+1) - k}{f(m+1) - f(m)} & \text{if } f(m) \leq k \leq f(m+1) \\
      0 & \text{if } k > f(m+1) 
   \end{cases}
$$

**Spectrogram**

<div style="text-align:center;">
<img src="/Images/Spectrogram40D.png" alt="Spectrogram" 
style="width:50%; height:auto;">
</div>

>Spectrogram with 40 Dimensional Vector

**Training Augmentation**
- Time Warping
    - Distorting the time axis
    - e.g., make the model more robust to various speaking rate
- Frequency Masking
    - Masking certain frequency bands
    - e.g., make the model more robust to background noise
- Time Masking
    - Masking certain time frames
    - e.g., make the model more robust to background noise

<div style="text-align:center;">
<img src="/Images/TrainingAugmentation.png" alt="Spectrogram" 
style="width:50%; height:auto;">
</div>

>Original Spectrogram with 3 Training Augmentation Methods

### Architectures

**Encoder-Decoder**

<div style="text-align:center;">
<img src="/Images/EncoderDecoderArchitecture.png" alt="Encoder Decoder Architecture" 
style="width:50%; height:auto;">
</div>

>Encoder-decoder Speech Recognizer

**Subsampling**
- Size input >> size output
- Compression to shorten acoustic feature sequence
- Algorithm:
    - Low frame rate: $f_i = \text{concat}(f_i, f_{i-1}, f_{i-2}),$ delete $f_{i-1}$ and $f_{i-2}$
    - Convolutional network (downsamples with max pooling)
    - Pyramidal RNNs (each successive layer has half the number of time steps)

**Hypothesis Rescoring**
- Decoder outputs n-best sentences ([beam search](https://en.wikipedia.org/wiki/Beam_search))
- Rescore each sentence $Y$ given input $X$
    - Score sentence using a language model (likelihood, fluency)
    - $Score(Y|X) = \frac{1}{\lvert Y \rvert}_c \log{P(Y \vert X)} +  \lambda \log{P_{LM}(Y)}$
        - $\frac{1}{\lvert Y \rvert}_c \log{P(Y \vert X)}$: The mormalized log-probability of the sentence $Y$ given the input $X$. This term accounts for the likelihood of the sentence as predicted by the model
        - $\lambda \log{P_{LM}(Y)}$: The log-probability of the sentence $Y$ according to an external language model (LM), weighted by a parameter $\lambda$. This term accounts for the fluency and naturalness of the sentence
    - $\lambda$ tuned on held-out set
        - The held-out set is a subset of data not used in training but reserved for tuning and evaluating model parameters. 
        - Tuning $\lambda$ ensures that the balance between the likelihood term and the language model term is optimized for better performance.
- Select sentence with highest score

<details>
  <summary>Why we use log-likelihood?</summary>
  
  In many machine learning and statistical models, log-likelihood is used instead of the raw probability (likelihood) for several important reasons:
  
  1. **Numerical Stability**:
     Raw probabilities can be extremely small, especially when dealing with sequences of probabilities (e.g., in language models where each word's probability multiplies with the others). Using the log transformation:

     \[
    P(Y) = P(y_1) \times P(y_2) \times \ldots \times P(y_n)
    \]

     \[
     \log P(Y) = \log P(y_1) + \log P(y_2) + \ldots + \log P(y_n)
     \]
     transforms multiplication into addition, which helps avoid numerical underflow.
  
  2. **Simplification of Calculations**:
     Logarithms simplify the product of probabilities into a sum of log-probabilities, making computations more straightforward and stable.
  
  3. **Ease of Differentiation**:
     Many optimization algorithms require the differentiation of the objective function with respect to model parameters. Logarithmic functions are easier to differentiate, and their derivatives are more stable.
  
  4. **Additivity of Log-Likelihoods**:
     Log-likelihoods are additive, making it easier to accumulate and interpret the combined score of a sequence.
  
</details>

**Connectionist Temporal Classification (CTC)**

<div style="text-align:center;">
<img src="/Images/CTC.png" alt="CTC" 
style="width:50%; height:auto;">
</div>

- Output a single character for every frame $x_i$ (alignment)
- Special symbol for a blank (e.g., slience)
- Collapsing function collapses consecutive duplicate letters
- Collapsing function is many-to-one: Different alignments map to same output string
- Assumption: Output at time $t$ is independent of the output labels at any other time

$$
\begin{align*}
P_{CTC}(A \lvert C) &= \Pi_{t=1}^T p(a_t \lvert C) \\
a_t &= \argmax_{c \in C}(c \lvert X) \quad A = {a_1, \ldots, a_T}
\end{align*}
$$

- Problem: Most likely alignment $A$ may not correspond to the most likely final collapsed output string $Y$
- Pick output string $Y$ that has highest sum over the probability of all its possible alignments
- Approximation of sum of probabilities
    - Training: Dynamic programming
    Inference: Keep in beam high-probability algnments that map to same output string
- Rescoring with language model important

$$
\begin{align*}
P_{CTC}(Y \lvert X) &= \sum_{A \in B^{-1}(Y)} P(A \lvert X) \\
&= \sum_{A \in B^{-1}(Y)} \Pi_{t=1}^T p(a_t \lvert h_t) \\
\hat{y} &= \argmax_Y P_{CTC}(Y \lvert X)
\end{align*} 
$$

>CTC Model

Combining CTC and Encoder-Decoder

**RNN-Transducer**

**Whisper**

**Microsoft Azure**

**Foundation Models**

### Word Error Rate