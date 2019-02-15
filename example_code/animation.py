import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


ims = []
for i in range(60):

    line, = plt.plot(float(i/10), float(i/10), 'ro')
    ims.append([line])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

# ani.save('dynamic_images.mp4')
plt.show()

