---
layout: default
title: Study Notes - Affective Computing
parent: Artificial Intelligence for Digital Characters
grand_parent: Science
nav_order: 1
---

# Study Notes - Affective Computing

### Ingredients of Human Being
- <span style="color:red">Affect (feel)</span>
- <span style="color:blue">Behavior (act)</span>
- <span style="color:green">Cognition (think)</span> 

### What is Affect?
- **Emotions**
    - Angry
    - Sad
    - Fearful
- Moods
    - Relaxed
    - Bored
- Interpersonal Stances
    - Distant
    - Warm
    - Supportive
- Preferences & Attitudes
    - Liking 
    - Hating

### Affective Computing**
Study and development of systems that can <ins>recognize</ins>, <ins>interpret</ins>, <ins>process</ins>, and <ins>simulate</ins> human affects.
- Human-computer Interaction
- Human-like Computers
- Machine-understanding
- Ethics

Topics:
- **Sensing and Analysis**
- **Psycology and Behavior**
- Behavior generation

### Theories

**Components of Emotions**
- Subjective Experience
- physiological Changes
    - Autonomic Nervous System
    - Endocrine System
- Behavior Evoked

*What is the <ins>time sequence</ins> of these components in an emotion episode?*

**James-Lange Theory**
1. Perception of Emotion Arousing Stimulus 
2. Visceral and Skeletal Changes (Physiological arousal and behavior changes)
3. Interpretation (Subjective experience of emotion)

*<ins>physiological changes</ins> are the main driving factors of the emotion according to this model.*

Example:
1. I see a man by that parked car
2. I am trembling and running away
3. I am afraid!

**Cannon-Bard Theory**

1. Perception of Emotion Arousing Stimulus
    1. Experience of Emotion (Conscious emotion)
    2. Physiological (Bodily) Changes (Physiological arousal)

*In contrast with James-Lange Theory, Cannon-Bard Theory assumes the emotion to be only cognitive.*

Example:
1. I see a man by that parked car
2. I am afraid and trembling

**Schachter-Singer Theory**
1. Perception of Emotion Arousing Stimulus
    1. Physiological (bodily) Changes (Physiological arousal)
    2. Awareness of Physiological Arousal (Cognitive label for arousal)
2. Interpreting the Arousal as a Particular Emotion Given the Context (Conscious emotion)

*A compromise between two previous models - the emotion is physiological and cognitive.*

Example:
1. I see a man by that parked car
2. I am trembling
3. My trembling is caused by fear
4. I am afraid!

**Dimensional Theory**
- Core Affect: Most elementary affective feelings, part of a full-blown emotional episode
- Dimensional Model for Capturing Core Affect
    1. Valence: Positive or Negative Feeling
    2. Arousal: Intensity of Feeling
    3. Dominance: Degree of Control Over Situation

**Basic Emotions**
1. Caused by the perception of phylogenetic categories of events
    - Innate event such as perceiving a dangerous animal (bear)
2. Eliciting internal and external signals
    - Physiological changes and facial expression
3. Trigger innate hard-wired action plans
    - Fight or flight

Example:
- Ekman's basic emotions
- Plutchik Emotion Wheel

**Emotion Recognition** 

Multimodal sensing
- Non-invasive
    - Sounds
    - **Facial Expressions**
    - Interaction Data
    - Text
    - **Biosensors**
- Invasive
    - Blood Pressure
    - Hormone Levels
    - Neurotransmitter Levels

### Biosensors

**Heart Rate Variability**

Cardiac Activity (How to measure heart rate)
- <ins>ECG</ins>: Trace of electrical activity captured from the surface of the skin
- <ins>PPG</ins>: Measuring amount of light reflected by vessels
- Webcam: Measuring PPG signal from pupil and skin

<div style="text-align:center;">
<img src="/Images/OneHeartBeat.png" alt="One Heart Beat" 
style="width:50%; height:auto;">
</div>

>Simplified Heartbeat Diagram

<ins>Time Domain Analysis</ins> (analyze the time intervals between successive heartbeats)
- Standard deviation of R-R intervals
- Difference between max and min R-R interval
- Percentage of successive R-R intervals that differ by more than 50 ms
- Root mean square of successive R-R interval differences

<ins>Frequency Domain Analysis</ins> (analyze the power spectral density of heart rate variations, breaking down HRV into different frequency components)
- $LF / (LF + HF)$
- $LF / HF$
- $LF$ and $HF$ peak

**Skin Conductance**

- Indicative for arousal
- Measures sweating level
- Used in lie detector 

Types of Stimuli:
- Picture Simuli
- Audio Stimuli

Devices:
- Heart Measures 
- Skin Conductance

Features:
- Amplitude
- Latency
- Rise Time
- Half-recovery Time

*Motion affects skin conductance. Skin conductance response is not time invariant.*

cvxEDA library
- Implicit Filtering (Artifact detection not necessary)

**<ins>Biosensor Pipeline</ins>**

1. Input Signals (Physiological State)
    - electrodermal Activity
    - Interbeat Intervals
    - Skin Temperature
2. Preprocessing (Normalization of Bio-sensor Motion Artifacts)
    - <span style="color:red">Artifact Detection</span> 
    - Baseline Correction
3. Feature Extraction
    - Peaks
    - Signal Statistics
        - Phasic (transient and rapid changes in physiological data)
        - Tonic (baseline or steady-state level of physiological activities)
    - Spectral Analysis
4. Classification (Random Forest Classifier)
    - Ground Truth 
        - Basic Emotions & Stress
        - Self-assessment Manikin (A non-verbal pictorial assessment technique that measures an individual's emotional response to a stimulus)
            - Valence
            - Arousal
            - Dominance
    - [Decision Tree](https://www.youtube.com/watch?v=ZVR2Way4nwQ)
        - Highly sensitive to the training data, resulting in high variance
    - [Random Forest Algorithm](https://www.youtube.com/watch?v=v6VJ2RO66Ag)
        1. For $b=1$ to $B$ ($B$ is the number of total trees)
            1. Draw a bootstrap sample $\mathbf{Z}$ of size $N$ from the training data
            2. Grow a random forest tree $T_b$ to the bootstrapped data, by recursively repeating the following steps for each terminal node of the tree, until the minimum node size $n_min$ is reached or the node is pure:
                1. Select $m$ features at random from the $p$ features
                2. Pick the best feature/split-point among the $m$ by maximizing the entropy gain:
                    - $H(S) = - \sum_{i=1}^c p_i \log(p_i)$ ($p_i$ is the proportion of samples belonging to class $i$, and $c$ is the number of classes)
                3. Split the node into two child nodes
        2. Output the ensemble of trees ${T_b}_1^B$
    - To make a prediction at a new point x: 
        1. Let $C_b(x)$ be the class prediction of the $b\text{th}$ random forest tree. 
        2. $C(x)$ = majority vote ${C_b}_1^B$ (aggregation)

### Video Data

Method Overview:
- Preprocessing
    - Constant Frame Rate
    - Brightness Adjustment
- Feature Extraction
    - Action Unites
        - Identify independent motions of the face
    - Eye Blinks
    - Eye Gaze
    - Mouth Aspect Ratio
    - Head Movement
    - Fidgeting
        - Captures all movement in the video (body, face, ...)
            1. $f_temp = f_gray - b_gray$ ($f_temp$ measures the difference between new frame and past frame)
            2. Binarizing $f_temp$ (thresholding)
            3. Energy $E =$ Percentage of surviving pixels
            4. $b_gray = (1-a) * b_gray + a * f_gray$ (update past frame)
- Classification
    - Random Forest







