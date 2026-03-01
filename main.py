from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware
import io
import os
import gdown

# TensorFlow logs off + faster startup
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "model/fruits_classifier.h5"

# Create model folder
os.makedirs("model", exist_ok=True)


# ---------- STARTUP LOAD ----------
@app.on_event("startup")
def load_model_startup():

    global model

    # Download model if not exists
    if not os.path.exists(MODEL_PATH):

        print("Downloading model from Google Drive...")

        url = "https://drive.google.com/uc?id=1qbtgJ1V0RxGQZgXVGN-Jb9SkkqnyD8BB"

        gdown.download(url, MODEL_PATH, quiet=False)

    # Load model
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)

    print("Model Loaded 🚀")

    # Dummy warmup prediction
    dummy = np.zeros((1,224,224,3))
    model.predict(dummy)

    print("Model Warmed Up ⚡")
# ---------------------------------


# Image preprocessing
def preprocess(image):

    image = image.resize((224,224))
    image = np.array(image)/255.0
    image = np.expand_dims(image,axis=0)

    return image


@app.get("/")
def home():
    return {"message":"Fruit Classifier API Running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = Image.open(io.BytesIO(await file.read()))

    img = preprocess(image)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        result = "Rotten Fruit"
    else:
        result = "Fresh Fruit"

    return {"Prediction": result}
