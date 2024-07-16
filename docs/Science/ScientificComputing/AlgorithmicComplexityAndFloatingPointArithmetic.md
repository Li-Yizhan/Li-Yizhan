---
layout: default
title: Algorithmic Complexity and Floating-point Arithmetic
parent: ScientificComputing
grand_parent: Science
nav_order: 1
---

# Algorithmic Complexity and Floating-Point Arithmetic

### Background and Introduction

**Three pillars of science and engineering**

- Theory
- Computation
- Experiment



<figure>
    <div style="text-align:center;">
    <img src="/Images/ThreePillarScienceEngineering.png" alt="One Heart Beat" 
    style="width:50%; height:auto;">
    </div>
    <figcaption>Fig.1: Three Pillars of Science and Engineering</figcaption>
</figure>


**Pros and Cons of Numerical Simulations**
Pros
- Often cheaper
- Often faster
- Easy parameter variations
- Micro-scale to macro-scale
- No undesired side effects (bias/noise)
- No measurement inaccuracies

Cons
- A lot of theoretical knowledge needed
- Always a simplification of reality
- Only get out what you put in
- Risk of programming errors
- Result is often only approcimate; numerical errors
- Simulations are often not accepted as proof for the real world

>**Definition: Algorithm**
A finite sequence of well-defined instructions to solve a particular problem. 
- Decomposes a complex task into "simple" steps
- Each step could require itself a complicated algorithm to execute it
- "well-defined" means unambiguous, "with only one interpretation."
- No need to be linear (can contain loops, jumps, etc)
- Always finite (no infinite loops)
- Can be for a computer or a person
- Can be, but doesn't have to be, language-specific

**Top 10 algorithms of the 20th century**

(Named by Dongarra & Sullivan, 2020)

- <span style="color:blue">1946</span> Metropolis Algorithm (Monte Carlo simulations)
- <span style="color:blue">1947</span> Simplex Method (linear optimization)
- <span style="color:blue">1950</span> Krylov Subspace Methods (linear systems of equations)
- <span style="color:blue">1951</span> Matrix Decompositions (revolutionized matrix computations)
- <span style="color:blue">1957</span> Fortran Optimizing Compiler (high-level programming)
- <span style="color:blue">1959</span> QR Algorithm (matrix eigenvalues)
- <span style="color:blue">1962</span> Quicksort (list sorting)
- <span style="color:blue">1965</span> Fast Fourier Transform (spectral analysis)
- <span style="color:blue">1977</span> Integer Relation Detection (of mathematical interest)
- <span style="color:blue">1987</span> Fast Multipole Method (long-range many-body interactions)

### Laudau Notation of Complexity (The "big O" notation)

**How to measure and compare the computational cost of algorithms?**

- The constant prefactor is often not known (dependent on hardware, floating-point precision, and other circumstances)
- Forget the constant prefactor, and just call this $O(N)$ floating-point operations (FLOPs)
- Large-N scaling is relevant. We want to solve large problems

**Some facts**

- Polynomial complexity: $O(N^p)$ for some power $p$. Example: Nested loops
- Exponential complexity: $O(b^{N^p}
)$ for some base $b$ and power $p$.
Example: Brute-force password cracking
- Logarithmic complexity: $O(log_b(N^p))$ for some $b$ and $p$.
Example: Hierarchical structures, trees
- Constant complexity: $O(1)$. Example: Scalar operations
- Order (<ins>Relative Runtime</ins>):
$O(2^N) > O(N^3) > O(N^2 \log N) > O(N^2) > O(N \log N) > O(N) > O(\log N) > O(1)$
- Only the fastest-growing term is usually given: $O(N^3) = O(N^3 + N^2)$
- Also multivariate notation is possible: $O(N \log M + K^2)$
- For an input or output of size N, the scaling is at least O(N) with classical computers.
- Fun fact: Quantum computers can reach $O(log N)$ or even $O(1)$ for specific tasks, when the input/output data has N values!

**Best case vs. worst case vs. average case**

Important to know: Many algorithms have a best-case complexity, a worst-case complexity and an average (so-called "amortized") complexity

Example: Quicksort
- $O(N)$ if everything is already in order
- $O(N^2)$ in the worst case
- $O(N \log N)$ in the most typical cases

Typically the amortized complexity is the most important one in practice, because it corresponds to the typical/average use case. 

**Some Examples**

- $N \times N$ matrix multiplication or inversion: $O(N^3)$ for the naive way, $O(N^{2.373})$ for
optimized algorithms
- Fast Fourier transform: $O(N \log N)$
- Classical Molecular Dynamics simulations usually have $O(N)$, where $N$ is the number
of atoms/particles
- Sorting a list with $N$ values: $O(N^2)$ for Bubblesort, $O(N \log N)$ for Quicksort

**Important Notes**
- Computational complexity is a <ins>property of an algorithm</ins>, not of the problem it solves!
- It can depend on the <ins>actual</ins> data, not just on the number of values!
- Landau notation gives you <ins>relative runtime</ins> when N changes, not the absolute runtime for a given N!
- For small N, an algorithm with lower complexity can be slower than one with higher
complexity!
- For good performance, always choose the best-scaling available algorithm for each subproblem in your program, if you expect N to get large!
- Two algorithms with the same complexity are sometimes considered “equivalent”, even though their runtime can be quite different in practice.

### Finite Precision

**Problem with Scientific Computing**

1. Computers are <ins>finite state machines</ins>: They can only store a finite number of things
(values, states, pixels, timepoints, etc.)
2. Many problems in science and engineering can’t be solved analytically. Example:
$F (x) = ∫_0^x e^{−y2} \mathrm{d} y$ (normal distribution)
3. Many problems are <ins>infinite-dimensional</ins>! For instance, when the sought answer is a
function, not a number. Can you think of examples from your field?

**Consequences**

1. Not all numbers can be stored on a computer! Example: $\pi$
2. We need to find a numerical answer. Rather than some formula $F (x)$, we will get
$F = 0.2566...$ for a specific value of $x$
3. We have to suggest a finite set of solutions, from which the computer selects the
“optimal” one, even if it is not exact

**Symbolic Computation, a.k.a. Computer Algebra**

- Rearrange formulas & solve equations symbolically
- Example: $3 \times 2 = a ⇒ x = ±√a/3$
- Software: Mathematica, Maple, Python SymPy, MATLAB Symbolic Math Toolbox

**Integer Numbers**

- A 32-bit integer stores numbers $x ∈ [−2,147,483,648, 2,147,483,647]$
- Can be signed $(±)$ or unsigned $(+)$
- Division generally not possible, is rounded to lower int: $7/4 = 1$
- Overflow/underflow when maximum/minimum is reached: $2,147,483,647 + 1 = −2,147,483,648$

**IEEE 754 Standard for Floating-Point Numbers**

A floating-point number is represented by the formula:

$x = s \cdot m \cdot 2^e$

Where 

- $s$ is the sign (0 for positive, 1 for negative)
- $m$ is the mantissa or significant
- $e$ is the exponent

32-Bit Single Precision Layout
- Sign bit (1 bit)
- Exponent (8 bits): Encodes the exponent $e$ (with a bias to allow for negative exponents)
- Fraction/Mantissa (23 bits): Encodes the significant digits of the number

<ins>IEEE754-to-Number Example (32-bit Single Precision):</ins>

- Sign bit: 0
- Exponent: 01111100 (binary) = 124 (decimal)
- Fraction/Mantissa: 010000000000000000000000 (binary)

The value is decoded as follows:
- Sign: s = 0 (positive)
- Exponent: $e = 124 - 127 = -3$ (the bias for 32-bit single precision is 127)
- Mantissa: 1.01000000000000000000000 (The implicit leading 1 is added for normalized numbers)

The floating-point number is thus:

$x = 1 \cdot 1.01_s \cdot 2^{-3}$
$x = 1 \cdot 1.25 \cdot 2^{-3}$
$x = 1.25 \cdot 0.125$
$x = 0.15625$

<ins>Number-to-IEEE754 Example:</ins>

Target number: 5.75

1. Binary representation:
    - 5 in binary: 101
    - 0.75 in binary: 0.11 $(0.75 = 0.5 + 0.25)$
    - 5.75 in binary: 101.11
2. Normalize the Binary Representation
    - 101.11 becomes $1.0111 \times 2^2$
3. Sign bit
    - Positive number: 0
4. Exponent:
    - The exponent is 2
    - Add the bias (127 for single precision): 2 + 127 = 129
    - 129 in binary: 10000001
5. Mantissa:
    - The normalized binary is 1.0111. The leading 1 is implicit and not stored. 
    - The mantissa is 01110000000000000000000 (23 bit)
6. IEEE 754 Representation
    - 0 | 10000001 | 01110000000000000000000

### Representability

**Examples of representable numbers:**

- $1 = 2^0$
- $−64 = −2^6$
- $127 = 64 + 32 + 16 + 8 + 4 + 2 + 1 = ∑_{i=0}^6 2^i = 1111111_2$
- $1024.25 = 2^{10} + 2^{−2} = 10000000000.01_2$
- $0.15625 = 0.125 + 0.03125 = 2^{−3} + 2^{−5} = 0.001012$
- Single precision: all integers up to ±16,777,216
- Double precision: all integers up to ±9,007,199,254,740,992

**Examples of **not** representable numbers:**

- $\frac{1}{10} = 0.1$ cannot be written as a finite sum $∑_i b_i 2^i$ with $bi ∈ {0, 1}$
- All numbers with an infinite binary representation, like π, e, etc.
- $\frac{1}{5} = 0.2 = 0.00110011_2...$ has no finite binary representation
- $\frac{1}{3} = 0.010101_2...$
- $1.2 = 1 + \frac{1}{5}$
- Numbers that are too long to fit into the exponent and mantissa
- Values that are too large $(10^{400})$or too small $(10^{−400})$

**Special Values**

- ±0
- NaN (Not a number) Example: 0.0 / 0.0 = NaN
- ±Inf (±∞) Example: -1.0 / 0.0 = -Inf

**Consequences of finite precision**

- Numbers are rounded to the nearest representable floating-point number
- The computation continues with a small error
- Tiny round-off errors can add up to large inaccuracies
- Very small numbers cannot be added to very large numbers
- <ins>Numerical Cancellation</ins>

### Machine Epsilon

How large is the round-off error (in relation to the stored number?)

>**Definition: Machine epsilon**
The smallest positive representable number $\epsilon$ for which $1 + \epsilon \gt 1$ in a particular working precision.

- The machine epsilon is an <ins>upper bound</ins> for the <ins>relative error</ins> from rounding in one operation in floating-point arithmetic
- It depends on the hardware (in particular the CPU)
- It depends on the floating-point format (IEEE 754 single/double etc.)

Examples
- Single precision (32-bit): $\epsilon = 2^{−23} ≈ 1.19 × 10^{−7}$
- Double precision (64-bit): $\epsilon = 2^{−52} ≈ 2.22 × 10^{−16}$

What does that mean in practice?
- In single precision, everything after the 7th significant digit is numerical noise.
Example: 0.001234567890
- In double precision: everything after the 16th significant digit
- One cannot add numbers smaller than $\epsilon · x$ to a number $x$ (it will be rounded down to
$x$ again).
- Round-off errors add up if you’re unlucky. They can easily grow to the 6th, 5th etc. significant digit after continued computation.
- Everything below double precision is typically useless for scientific computing

**Strengths and Weaknesses of floating-point numbers**
Strengths:
- They can represent values between integers
- They cover a much larger range than integers (maximum in double precision: $≈ 1.8 × 10^{308}$)
- The absolute scale is not relevant. Example: $8.5 × 10^{−6}, 8.5, 8.5 × 10^3$ are equally
representable. (Whether you calculate in μm, km or inches does not matter!)
- There are special values to indicate that something went wrong (NaN, Inf)

Weaknesses
− Not all numbers are representable, even simple ones (e.g., 0.2)
− Round-off errors almost always occur
− Errors can add up and result in substantial loss of significance
− Floating-point addition is not generally associative: $(a + b) + c \neq a + (b + c)$
− Testing for equality is problematic

**Numerical Cancellation**

A very dangerous problem: Substracting nearly equal numbers can cause extreme loss of accuracy!

$123.456\textcolor{red}{\mathbf{89}} - 123.456\textcolor{red}{\mathbf{22}} = 0.0001\textcolor{red}{\mathbf{67}} = 1.67 \times 10^{-4}
$

(red numbers are noises)

If the computation continues with the value 1.67 instead of 1 (actual difference), the rounding error would be 67 percent in this case. 

Example: Approximation of the derivative via the difference quotient:

$$
f'(x) ≈ \frac{f(x + h) - f(x)}{h}
$$

The approximation should improve as $h$ shrinks, but the opposite happens for very small $$h$ due to numerical cancellation

How to avoid cancellation?
- Use high precision (at least double precision, 64-bit)
- Sometimes subtractions can be replaced by clever manipulation of formulas
- Whenever you subtract two numbers, think beforehand whether they could be nearly equal at some point in your computation
- Add a check to your program to test for (near) equality of the subtracted numbers, and print warnings when they are

### Summary

1.  An algorithm is a finite sequence of instructions to solve a problem (input → output).
2. Landau notation specifies the scaling of an algorithm with the size of its input or output, but not its runtime. For large problems, avoid poorly scaling algorithms.
3. Computers store numbers in floating-point format with finite precision. This is inevitable, and leads to round-off errors.
4. The machine epsilon quantifies this finite precision. It is the smallest positive representable number for which $1 + \epsilon \neq 1$.
5. For scientific computing, always use at least 64-bit precision (a.k.a. IEEE 754 double precision).
6. Numerical cancellation occurs if two similar numbers with finite precision are subtracted from each other. Avoid it whenever possible.
