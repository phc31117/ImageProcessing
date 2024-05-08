'''
python version : 3.8.8
opencv version : 4.8.1

target:
generate 50 variations with sigma = 35
np.random.normal(mean, sigma, (H, W, C)) # mean = 0, sigma = 35
np.clip(img, a_min, a_max) # limit the bound

photo credit : Photo by Biel Morro on Unsplash

'''

import cv2
import numpy as np
import random

img = cv2.imread('pics/pic1.jpg')

# [H, W, C] : height, width, channel
# print(img.shape)  # (853, 1280, 3) 


final = img

for i in range(50): # add 50 times
    noise = np.random.normal(0, 35, img.shape)
    img_add = np.add(img, noise)
    img_add = np.clip(img_add, 0, 255).astype(np.uint8) # limit the upper & lower bound
    final = np.mean(np.array([img_add, final]), axis = 0).astype(np.uint8)
    


cv2.imshow('pic1', final)
cv2.waitKey(0)                 # press any key to stop the window
cv2.destroyAllWindows()        # close the window

# 存下圖片檔
cv2.imwrite('pics/pic1_add_gaussian_noise.jpg', final)
