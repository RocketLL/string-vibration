import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tqdm

rho = 5.9e-3
tau = 67.29 * 10
F0 = 0.1
gamma = 0.1
omega = 80

x = 0.6
t = 1

nx = 50
nt = 100000

dx = x / nx
dt = t / nt

x_domain = np.linspace(0, x, nx)
y = np.zeros((3, nx))

frames = []
fig = plt.figure()

def gaussian_pdf(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2) \
        / (sigma * np.sqrt(2 * np.pi))

for j in tqdm.tqdm(range(nt)):
    for i in range(1, nx - 1):
        y[0, i] = (
            (2 * rho / dt ** 2) * y[1, i]
            - (rho / dt ** 2) * y[2, i]
            + (gamma / dt / 2) * y[2, i]
            + (tau / dx ** 2) * (y[1, i+1] - 2 * y[1, i] + y[1, i-1])
            + F0 * np.sin(omega * j * dt) / x * gaussian_pdf(x_domain[i], x/2, 0.1)
        ) / (rho / dt ** 2 + gamma / dt / 2)

    if j % 100 == 0:
        frame, = plt.plot(x_domain, y[0, :], color="k")
        frames.append([frame])
        # print(f"{j} / {nt}")
    
    y[2, :] = y[1, :]
    y[1, :] = y[0, :]

plt.ylim((-0.0001, 0.0001))
ani = animation.ArtistAnimation(fig, frames, interval=100, blit=True)
ani.save("plot.mp4")