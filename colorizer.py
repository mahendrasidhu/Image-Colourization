import cv2
import os


def load_image(image_name):

    base = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(base, "bw_images", image_name)

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image '{image_name}' not found.")

    return image