from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from babel.numbers import format_currency

app = FastAPI()

# Load model only once
model = joblib.load("model.pkl")


class HouseInput(BaseModel):
    RM: float


@app.post("/predict")
def predict(data: HouseInput):

    df = pd.DataFrame({"RM": [data.RM]})

    prediction = model.predict(df)[0]

    usd_to_inr = 95.25
    price_in_inr = prediction * 1000 * usd_to_inr

    return {
        "Predicted Price (USD Thousands)": round(prediction, 2),
        "Predicted Price (INR)": format_currency(
            price_in_inr,
            "INR",
            locale="en_IN"
        )
    }