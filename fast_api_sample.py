#pip install fastapi
#pip install uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.linear_model import LinearRegression

city = pd.read_csv('/workspaces/DS-learning/Tetuan City power consumption.csv')
x=city[["Temperature","Humidity","Wind Speed"]].values
y=city["Zone 1 Power Consumption"].values

app = FastAPI()

model=LinearRegression().fit(x,y)

class predict(BaseModel):
    temp: float
    hum: float
    wind: float

@app.get("/predit_value")
async def predit_value(pr: predict):
    rel = model.predict([[pr.temp,pr.hum,pr.wind]])
    return {"result": rel}

if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run(app)#, host="127.0.0.1", port=8000)
