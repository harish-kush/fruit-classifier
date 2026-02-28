# 🍎 FreshScan — Fruit Freshness Detector

FreshScan is an **AI-powered web application** that detects whether a fruit is **Fresh or Rotten** using a **Convolutional Neural Network (CNN)** model.
Users can upload their own images or test the model using built-in sample images.

The system uses a **TensorFlow deep learning model** served through a **FastAPI backend** with a modern interactive frontend.

---

## 🚀 Features

* 📷 Upload fruit images for prediction
* 🧪 Try built-in sample images
* ⚡ Real-time prediction using FastAPI
* 🎯 Confidence score for predictions
* 🧠 CNN-based deep learning model
* 🎨 Modern UI with drag & drop upload
* 🔍 Image preview before prediction
* 🌐 REST API support

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Framework: TensorFlow / Keras
* Input Size: 224 × 224
* Output:

  * **Fresh Fruit**
  * **Rotten Fruit**
* Loss Function: Binary Crossentropy
* Optimizer: Adam
* Training Accuracy: ~98–100%
* Test Accuracy: ~97–99%

---

## 🏗️ Project Structure

```
fruit_classifier/

backend/
   main.py
   requirements.txt

frontend/
   index.html

images/
   f1.jpg
   f2.jpg
   r1.jpg
   r2.jpg

model/
   fruits_classifier.h5

venv/
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/freshscan.git
cd freshscan
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run FastAPI Server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

### 5️⃣ Run Frontend

Open:

```
index.html
```

in your browser.

---

## 📡 API Endpoint

### POST `/predict`

Upload an image file for prediction.

Example Response:

```
{
  "Prediction": "Fresh Fruit",
}
```

---

## 🖥️ Tech Stack

### Backend

* FastAPI
* TensorFlow
* NumPy
* Pillow

### Frontend

* HTML
* CSS
* JavaScript

### Machine Learning

* Convolutional Neural Network (CNN)
* Image Classification

---

## 🎯 How It Works

1. User uploads an image
2. Image is resized to **224×224**
3. Image is normalized
4. CNN model processes the image
5. Prediction is returned
6. Result is displayed on UI

---

## 📸 Screenshots

### Main Interface

* Upload image
* Drag & drop support
* Sample images
* Prediction result

---

## 🔮 Future Improvements

* MobileNet / ResNet transfer learning
* Multi-fruit classification
* Cloud deployment
* Mobile app version
* Real-time camera detection

---

## 👨‍💻 Author

**Harish Kushwaha**

* Electronics and Communication Engineering Student
* Frontend Developer
* Machine Learning Enthusiast

---

## ⭐ Resume Project Description

Built an AI-powered fruit freshness detection web application using **TensorFlow CNN**, **FastAPI**, and **HTML/CSS/JavaScript**, achieving **~98% accuracy** with real-time image prediction.

---
