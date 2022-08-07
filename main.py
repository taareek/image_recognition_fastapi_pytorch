from typing import Optional
from fastapi import FastAPI

# making app object 
app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Hello there.."}

# prediction route 
@app.post("/predict")
async def predict():
    return {"message": "hello from prediction."}