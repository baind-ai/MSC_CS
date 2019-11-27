from fastapi import FastAPI
import uvicorn

from datetime import datetime
import random
# from typing import List
# from pydantic import BaseModel


app = FastAPI()

"""
class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime = None
    friends: List[int] = []
"""


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/germany")
def read_weather():
    return {
        "datetime": datetime.now().strftime('%X %Y.%m.%d'),
        "temperature": 15 + random.random() * 10  # fake some temperature
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
