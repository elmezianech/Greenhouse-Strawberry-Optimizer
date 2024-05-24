from fastapi import FastAPI
from baseModel import Data
import pickle
import uvicorn
import logging

# Add this line to configure logging
logging.basicConfig(level=logging.DEBUG)

# Load your serialized model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI
app = FastAPI()

# Define a route to provide basic information about your API
@app.get("/")
async def root():
    return {"message": "Welcome to the API for your machine learning model!"}

# Define a route to make predictions
@app.post("/predict")
async def predict(data: Data):
    # Assuming your model expects input features in a dictionary
    # Make predictions
    prediction = model.predict([[data.temperature, data.humidity, data.light]])
    predicted_light = int(prediction[0][0])
    predicted_water = int(round(prediction[0][1]))

    return {
        "predicted_light": predicted_light,
        "predicted_water": predicted_water,
        "temp": data.temperature,
        "humidity": data.humidity,
        "light": data.light
    }


if __name__ == '__main__' :
    uvicorn.run(app, host='127.0.0.1', port= 8000)
