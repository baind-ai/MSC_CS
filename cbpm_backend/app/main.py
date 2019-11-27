from fastapi import FastAPI
import uvicorn
from datetime import datetime

from cbpmtypes import IncidentLocation
from apiconnector import (
    get_absolutely_not_faked_weather_data
)


app = FastAPI()


@app.get("/weather/{incident_location}")
async def read_weather(
        incident_location: IncidentLocation,
        date_time: str = datetime.now().strftime('%X %Y.%m.%d'),
        ):

    temp, sichtweite, windgeschwindigkeit, wellenhoehe = \
            get_absolutely_not_faked_weather_data(
                incident_location.lower()
            )

    return {
        "datetime": date_time,
        # fake temperature
        "temperature": "{:.2f}".format(temp),
        "sichtweite": "{:.2f}".format(sichtweite),
        "windgeschwindigkeit": "{:.2f}".format(windgeschwindigkeit),
        "wellenhoehe": "{:.2f}".format(wellenhoehe)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
