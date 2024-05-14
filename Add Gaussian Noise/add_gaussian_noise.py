'''
python version : 3.8.8
opencv version : 4.8.1

target:
generate 50 variations with sigma = 35 as noise, then add the noise into the picture
np.random.normal(mean, sigma, (H, W, C)) # mean = 0, sigma = 35
np.clip(img, a_min, a_max) # limit the bound

photo credit : Photo by Biel Morro on Unsplash

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pics/pic1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img.shape) # (5730, 3810, 3)

# add noise
final = img
for i in range(50): # add 50 times
    noise = np.random.normal(0, 35, img.shape)
    img_add = np.add(img, noise)
    img_add = np.clip(img_add, 0, 255).astype(np.uint8) # limit the upper & lower bound
    final = np.mean(np.array([img_add, final]), axis = 0).astype(np.uint8)

diffrence = final - img

# Initial Image
plt.figure(figsize=(img.shape[0]*0.005,img.shape[1]*0.005))
plt.subplot(1,3,1)
plt.axis("off")
plt.title("Before (Initial Image)", fontsize=50)
plt.imshow(img)

# Image with Gaussian Noise
plt.subplot(1,3,2)
plt.axis("off")
plt.title("After (With Gaissian Noise)", fontsize=50)
plt.imshow(final)

# Difference
plt.subplot(1,3,3)
plt.axis("off")
plt.title("Difference", fontsize=50)
plt.imshow(diffrence)


plt.subplots_adjust(top=1, bottom=0, right=1, left=0, wspace=0.5, hspace=0)
plt.margins(0, 0)

# save the result
plt.savefig("pics/gaussian_noise_result.jpg", bbox_inches='tight', pad_inches=1.0)
plt.show()
