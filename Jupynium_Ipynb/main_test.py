import random

size = 15
x = range(size)
y = [random.randint(i * 5, 100) for i in range(size)]
for i in y:
    print(i)

import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
img = ax.plot(x, y)
