import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = 3*x**2 + 2*x +5

plt.figure()
plt.plot(x,y,'r-')

