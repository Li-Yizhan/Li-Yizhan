import matplotlib.pyplot as plt
import numpy as np

def pw(x):
 if x < 1/2: return 2 * x
 elif x >= 1/2 and x < 1: return x + 1/2
 else: return 3/2

x = np.arange(0., 1.5, 0.01)
plt.plot(x, list(map(pw, x)))

plt.show()