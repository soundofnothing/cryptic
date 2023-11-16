
import numpy as np
import matplotlib.pyplot as plt

def plot_elliptic_curve(a, b):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), y**2 - x**3 - a*x - b, levels=[0], colors='blue')
    plt.grid()
    plt.show()

# Example elliptic curve: y^2 = x^3 - x + 1
plot_elliptic_curve(-1, 1)
