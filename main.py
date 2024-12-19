from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

class ApiInput(BaseModel):
    form: List

class ApiOutput(BaseModel):
    approve: int

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/credit")
async def approve_credit(data: ApiInput) -> ApiOutput:
    prediction = int(model.predict([data.form])[0])
    pred = ApiOutput(approve=prediction)
    return pred
