import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rho = 5.9e-3
tau = 67.29
F0 = 0.1
gamma = 0.01
omega = 80

x = 0.6
t = 0.1

nx = 100
nt = 10000

dx = x / nx
dt = t / nt

x_domain = np.linspace(0, x, nx)
y = np.zeros((3, nx))

fn = lambda i: np.exp(-((x_domain[i] - x/2)/0.01) ** 2)
dom = np.arange(0, nx, 1)
plt.plot(
  x_domain,
  fn(dom)
)

plt.show()