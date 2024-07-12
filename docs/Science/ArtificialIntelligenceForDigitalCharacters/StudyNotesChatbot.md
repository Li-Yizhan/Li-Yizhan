---
layout: default
title: Study Notes - Chatbot
parent: Artificial Intelligence for Digital Characters
grand_parent: Science
nav_order: 4
---

# Study Notes - Chatbot

### Introduction
**Motivation**
Where are chatbots used?
- Customer Service
- Entertainment
- Education
- Health Care
- and many more...

What are common requirements?
- 24-hours Service
- Scalability
- Adaptability
- Context-Awareness
- and many more...

What is a chatbot?
- A chatbot is a computer program that simulates human conversation with an end user (No AI or NLP necessary to call it a chatbot)

**Rule-based Systems**
- Operates on a set of predefined rules
- Conceptually (and strongly simplified)...

How rule-based chatbots work?
- User Input
- Input Processing
- Rule Matching
- Response Retrieval

Characteristics of rule-based system
- Determinism
- High Precision
- Limited Flexibility
- Easy Control
- Lack of Scalability and Adaptability
- Low Risk

**Beyond Rule-based Systems**
- Two fundamentally different approaches
    - Response by Retrieval
    - Response by Generation

<div style="text-align:center;">
<img src="/Images/RetrievalAndGeneration.png" alt="Two Approaches" 
style="width:50%; height:auto;">
</div>

>Retrieval Approach vs. Generation Approach

### NLP for Dialogue Systems

**Text Preprocessing**

What is "text"?
- A sequence of...
    - sentence?
    - words?
    - characters?
    - ...
- In the form of...
    - an article?
    - a conversation?
    - an encoded document?
    - ...

Where do we split words/sentences?
- Spaces?
- Punctuation?
- <span style="color:red">CONTEXT!</span>

Word Tokenization
- The process of splitting text into individual words or tokens
- Sub-word Tokenization

Linguistic Morphology
- Words are not atoms (they have structure)
- Morphemes are minimal units of meaning forming words
    - Categorize = Catagory + ize
    - Overestimating = Over + estimate + ing

Text Representations
- List of Words (token_id)
- Set of Words (occurance_bool)
- Bag of Words (occurance_count)
- Vector (weight)

<div style="text-align:center;">
<img src="/Images/TextRepresentation_1.png" alt="Text Representation 1" 
style="width:50%; height:auto;">
</div>

>Text Representation

Text Similarity

<div style="text-align:center;">
<img src="/Images/TextSimilarity.png" alt="Text Similarity" 
style="width:50%; height:auto;">
</div>

>Text Similarity

**Embeddings**

Two fundamentally different approaches

**Response Generation**

**Sampling Strategies**

### LLM Adaptation

### Optimizations & Extensions