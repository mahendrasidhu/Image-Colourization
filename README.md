
# 🎨 Image Colorization using Deep Learning

A deep learning-based image colorization system that automatically converts grayscale images into realistic color images using Convolutional Neural Networks (CNNs). The project leverages the LAB color space to predict chrominance channels while preserving image structure, producing visually appealing colorized outputs.

---

## 📌 Overview

Image colorization is a computer vision task that aims to restore color information in grayscale images. This project implements a CNN-based approach that learns color distributions from training data and predicts realistic colors for unseen grayscale images.

The model is trained using deep learning techniques and image preprocessing methods to generate high-quality colorized images.

---

## ✨ Features

- Automatic colorization of grayscale images
- CNN-based deep learning architecture
- LAB color space representation
- Image preprocessing and normalization
- Model evaluation using standard image quality metrics
- Supports testing on custom grayscale images

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Framework:** TensorFlow / Keras
- **Libraries:**
  - OpenCV
  - NumPy
  - Matplotlib
  - Scikit-learn (optional)
- **Development Environment:** Jupyter Notebook / VS Code

---

## 📂 Project Structure

```text
Image-Colorization/
│
├── dataset/              # Training and testing images
├── models/               # Saved trained models
├── notebooks/            # Jupyter notebooks
├── outputs/              # Generated colorized images
├── src/                  # Source code
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

1. Load the dataset.
2. Convert RGB images to the LAB color space.
3. Extract the L (grayscale) channel as input.
4. Train the CNN to predict the A and B color channels.
5. Combine the predicted channels with the original L channel.
6. Convert the LAB image back to RGB.
7. Evaluate the generated images.

---

## 📊 Evaluation Metrics

The generated images can be evaluated using:

- Structural Similarity Index (SSIM)
- Peak Signal-to-Noise Ratio (PSNR)
- Mean Squared Error (MSE)

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Image-Colorization.git
cd Image-Colorization
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python main.py
```

or

```bash
jupyter notebook
```

---

## 📸 Sample Results

| Input (Grayscale) | Output (Colorized) |
|-------------------|--------------------|
| *(Add Image)* | *(Add Image)* |

> Replace the placeholders above with screenshots of your project's results.

---

## 📈 Future Improvements

- Improve color prediction accuracy using larger datasets.
- Implement GAN-based image colorization.
- Experiment with Vision Transformers (ViTs).
- Support high-resolution image colorization.
- Deploy the model as a web application using Flask or FastAPI.

---

## 👨‍💻 Author

**Mahendra Sidhu Chagantipati**

- LinkedIn: https://www.linkedin.com/in/mahendra-sidhu-chagantipati-82553b293

---

## 📄 License

This project is intended for educational and research purposes.
