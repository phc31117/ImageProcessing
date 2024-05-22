import cv2
from matplotlib import pyplot as plt

def HE_image(image_path, save_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    he_image = cv2.equalizeHist(image)
    
    # Calculate histograms
    hist_src = cv2.calcHist([image], [0], None, [256], [0,256])
    hist_dst = cv2.calcHist([he_image], [0], None, [256], [0,256])
    
    # Set up the plot with subplots
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    # Plot the original image
    axes[0, 0].imshow(image, cmap='gray')
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # Plot histogram for the original image
    axes[1, 0].plot(hist_src)
    axes[1, 0].set_title('Histogram of Original Image')
    
    # Plot the equalized image
    axes[0, 1].imshow(he_image, cmap='gray')
    axes[0, 1].set_title('Equalized Image')
    axes[0, 1].axis('off')
    
    # Plot histogram for the equalized image
    axes[1, 1].plot(hist_dst)
    axes[1, 1].set_title('Histogram of Equalized Image')
    
    # Display all plots nicely
    plt.tight_layout()

    plt.savefig(save_path)
    plt.show()


def CLAHE_image(image_path, save_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Validate image loading
    if image is None:
        raise ValueError("Image not found or unable to load.")
    
    # Create a CLAHE object (with default parameters)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    
    # Apply CLAHE to the grayscale image
    clahe_image = clahe.apply(image)
    
    # Calculate histograms
    hist_src = cv2.calcHist([image], [0], None, [256], [0,256])
    hist_clahe = cv2.calcHist([clahe_image], [0], None, [256], [0,256])
    
    # Set up the plot with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot the original image
    axes[0, 0].imshow(image, cmap='gray')
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # Plot histogram for the original image
    axes[1, 0].plot(hist_src)
    axes[1, 0].set_title('Histogram of Original Image')
    
    # Plot the CLAHE image
    axes[0, 1].imshow(clahe_image, cmap='gray')
    axes[0, 1].set_title('CLAHE Image')
    axes[0, 1].axis('off')
    
    # Plot histogram for the CLAHE image
    axes[1, 1].plot(hist_clahe)
    axes[1, 1].set_title('Histogram of CLAHE Image')
    
    # Adjust layout to fit everything nicely
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(save_path)
    plt.show()
