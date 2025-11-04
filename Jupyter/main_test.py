import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

# Load the image using imread
img = mpimg.imread('../Assets/stinkbug.png')

# Display the image
plt.imshow(img)
plt.show()
