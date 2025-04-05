import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='sin(2x)')
plt.title('Plot of Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

