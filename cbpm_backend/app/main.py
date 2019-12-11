from fastapi import FastAPI
import uvicorn
from datetime import datetime
from typing import List
import logging

from cbpmtypes import IncidentLocation, Country, Investigator
from apiconnector import (
    get_absolutely_not_faked_weather_data,
    get_totally_real_gps_route,
    fetch_available_investigators,
    get_applicable_laws,
)


app = FastAPI()


@app.get("/weather/{incident_location}")
def read_weather(
    incident_location: IncidentLocation,
    date_time: str = datetime.now().strftime("%X %Y.%m.%d"),
) -> dict:

    (
        temp,
        sichtweite,
        windgeschwindigkeit,
        wellenhoehe,
    ) = get_absolutely_not_faked_weather_data(incident_location.lower())

    return {
        "datetime": date_time,
        # fake temperature
        "temperature": "{:.2f}".format(temp),
        "sichtweite": "{:.2f}".format(sichtweite),
        "windgeschwindigkeit": "{:.2f}".format(windgeschwindigkeit),
        "wellenhoehe": "{:.2f}".format(wellenhoehe),
    }


@app.get("/gps/{vessel_name}")
def read_gps_coordinates(
    vessel_name: str, incident_location: IncidentLocation = None
) -> str:
    return get_totally_real_gps_route(vessel_name, incident_location)


@app.get("/investigators/all")
def get_applicable_investigators() -> List[Investigator]:
    return fetch_available_investigators()


@app.get("/investigators/check/{investigator_name}")
def check_proposed_investigator(investigator_name: str) -> bool:
    if investigator_name in [inv.name for inv in fetch_available_investigators()]:
        return True
    else:
        return False


@app.get("/jurisdiction/{country}")
def get_jurisdication_data(country: Country) -> str:
    return get_applicable_laws(country)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
