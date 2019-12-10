from starlette.testclient import TestClient
import sys
from pathlib import Path
import datetime

sys.path.append("./app/")
from main import app  # noqa: E402


client = TestClient(app)


def test_read_weather():
    response = client.get("/weather/nordsee")
    data = response.json()
    assert (
        type(datetime.datetime.strptime(data["datetime"], "%H:%M:%S %Y.%m.%d"))
        is datetime.datetime
    )
    assert type(float(data["temperature"])) is float
    assert type(float(data["sichtweite"])) is float
    assert type(float(data["windgeschwindigkeit"])) is float
    assert type(float(data["wellenhoehe"])) is float


def test_read_gps_coordinates():
    vessel_name = "vessel123"
    location = "nordsee"
    response = client.get("/gps/{}?incident_location={}".format(vessel_name, location))
    assert response.status_code == 200
    assert response.json() == "{}\\{}.html".format(str(Path.home()), vessel_name)


def test_get_applicable_investigators():
    response = client.get("/investigators/all")
    assert len(response.json()) == 5


def test_check_proposed_investigator():
    response = client.get("/investigators/check/Maier")
    assert response.status_code == 200
    assert response.json() is True


def test_get_jurisdication_data():
    response = client.get("/jurisdiction/schweiz")
    assert response.json() == "Schweizer Wurstsalat"
