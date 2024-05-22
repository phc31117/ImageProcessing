
import cv2
import numpy as np
import matplotlib.pyplot as plt


def AddGaussianNoise(image_path, save_path, times=50, mean=0, stdev=35):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    # add noise
    final = img
    
    
    for i in range(times): # add 50 times
        noise = np.random.normal(mean, stdev, img.shape)
        img_add = np.add(img, noise)
        img_add = np.clip(img_add, 0, 255).astype(np.uint8) # limit the upper & lower bound
        final = np.mean(np.array([img_add, final]), axis = 0).astype(np.uint8)

    diffrence = final - img

    # Initial Image
    plt.figure(figsize=(img.shape[0],img.shape[1]))
    plt.subplot(1,3,1)
    plt.axis("off")
    plt.title("Before (Initial Image)")
    plt.imshow(img)

    # Image with Gaussian Noise
    plt.subplot(1,3,2)
    plt.axis("off")
    plt.title("After (With Gaissian Noise)")
    plt.imshow(final)

    # Difference
    plt.subplot(1,3,3)
    plt.axis("off")
    plt.title("Difference")
    plt.imshow(diffrence)


    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, wspace=0.5, hspace=0)
    plt.margins(0, 0)

    # save the result
    plt.savefig(save_path, bbox_inches='tight', pad_inches=1.0)
    plt.show()
