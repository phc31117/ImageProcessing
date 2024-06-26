# Image Processing

**python version : 3.8.8**

**opencv version : 4.8.1**

## Add Gaussian Noise
Random generate noise : 50 variations with sigma = 35
![](pics/gaussian_noise_result.jpg)
Credit : Photo by <a href="https://unsplash.com/@bielmorro?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Biel Morro</a> on <a href="https://unsplash.com/photos/black-string-lights-J_F_003jcEQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>


## Basic OpenCV
`cv2.resize` : Resize the image.
-  `cv2.INTER_NEAREST`
-  `cv2.INTER_LINEAR`
-  `cv2.INTER_CUBIC`

```python
img = cv2.imread('img.png')
resized_img = cv2.resize(img, (500, 500), cv2.INTER_NEAREST)

```
![](pics/resize.jpg)

`cv2.getRotationMatrix2D`

`cv2.wrapAffine`


## HE (Histogram Equalization)
![](pics/HE_1.jpg)
![](pics/HE_2.jpg)

## CLAHE (Contrast Limited Adaptive Histogram Equalization)
![](pics/CLAHE_1.jpg)
![](pics/CLAHE_2.jpg)