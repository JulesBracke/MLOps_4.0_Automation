from fastapi import FastAPI
from PIL import Image
import torch
import torchvision.transforms as transforms
import os

app = FastAPI()

MODEL_PATH = "model/"
MODEL_FILE = os.path.join(MODEL_PATH, "model.pth")

model = None

def load_model():
    global model
    if os.path.exists(MODEL_FILE):
        model = torch.load(MODEL_FILE, map_location=torch.device("cpu"))
        model.eval()
        print("Model loaded successfully.")
    else:
        print("⚠️ No model found at:", MODEL_FILE)

load_model()

@app.get("/")
def root():
    return {"message": "Animals classification API is running"}

@app.post("/predict")
async def predict():
    return {"status": "Model loaded", "model_present": model is not None}