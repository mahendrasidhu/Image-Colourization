import cv2
import numpy as np
import os


def load_model():

    # Get project directory
    base = os.path.dirname(os.path.abspath(__file__))

    # Path to models folder
    models = os.path.join(base, "models")

    # Model files
    prototxt = os.path.join(models, "colorization_deploy_v2.prototxt")
    model = os.path.join(models, "colorization_release_v2.caffemodel")
    points = os.path.join(models, "pts_in_hull.npy")

    print("Loading Deep Learning Model...")

    net = cv2.dnn.readNetFromCaffe(prototxt, model)

    pts = np.load(points)

    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")

    pts = pts.transpose().reshape(2, 313, 1, 1)

    net.getLayer(class8).blobs = [pts.astype(np.float32)]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    print("Model loaded successfully.")

    return net