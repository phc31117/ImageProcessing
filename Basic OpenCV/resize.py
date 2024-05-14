import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pics/1.png')

# print(img.shape)  # (107, 87, 3)

resized_nearest = cv2.resize(img, (500, 500), cv2.INTER_NEAREST)
resized_linear = cv2.resize(img, (500, 500), cv2.INTER_LINEAR)
resized_cubic = cv2.resize(img, (500, 500), cv2.INTER_CUBIC)


# ORIGINAL
plt.figure(figsize=(img.shape[0],img.shape[1]))
plt.subplot(1,4,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

# INTER_NEAREST
plt.subplot(1,4,2)
plt.axis("off")
plt.title("cv2.INTER_NEAREST")
plt.imshow(resized_nearest)

# INTER_LINEAR
plt.subplot(1,4,3)
plt.axis("off")
plt.title("cv2.INTER_LINEAR")
plt.imshow(resized_linear)

# INTER_CUBIC
plt.subplot(1,4,4)
plt.axis("off")
plt.title("cv2.INTER_CUBIC")
plt.imshow(resized_cubic)


plt.subplots_adjust(top=1, bottom=0, right=1, left=0, wspace=0.5, hspace=0)
plt.margins(0, 0)

# save the result
plt.savefig("pics/resize.jpg", bbox_inches='tight', pad_inches=1.0)
plt.show()
