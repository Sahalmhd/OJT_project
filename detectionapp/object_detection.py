import numpy as np
from PIL import Image
import os

class ImageProcessor:
    def __init__(self, save_dir):
        # Set up the directory to save the processed images
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def preprocess_image(self, image_path):
        # Load and preprocess the image
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file does not exist at: {image_path}")

        img = Image.open(image_path)
        img = img.resize((300, 300))  # Resize image as needed by your future model
        img = np.array(img)
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        img = img / 255.0  # Normalize to [0, 1] range
        return img

    def save_image(self, image_array, file_name):
        # Convert back to image format and save it
        image_array = (image_array[0] * 255).astype(np.uint8)  # Remove batch dimension and scale back to [0, 255]
        img = Image.fromarray(image_array)
        save_path = os.path.join(self.save_dir, file_name)
        img.save(save_path)
        print(f"Image saved at: {save_path}")

# Example Usage
save_dir = 'media/images'  # Updated save path
image_path = 'path/to/your/image.jpg'
processor = ImageProcessor(save_dir)
preprocessed_img = processor.preprocess_image(image_path)
processor.save_image(preprocessed_img, 'processed_image.jpg')
