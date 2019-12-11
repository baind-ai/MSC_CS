from starlette.testclient import TestClient
import sys
from pathlib import Path
import datetime
import random
import string
import os

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


def random_string(stringLength=7):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(stringLength))


def remove_file(path):
    try:
        if Path(path).is_file():
            os.remove(path)
    except Exception:
        pass


def test_read_gps_coordinates():
    # test - with incident location
    vessel_name = random_string()
    location = "nordsee"
    response = client.get("/gps/{}?incident_location={}".format(vessel_name, location))
    assert response.status_code == 200
    path = "{}\\{}.html".format(str(Path.home()), vessel_name)
    assert response.json() == path
    assert Path(path).is_file() is True
    remove_file(path)


def test_read_gps_coordinates_wo_location():
    # test - without incident location
    vessel_name2 = random_string()
    response = client.get("/gps/{}".format(vessel_name2))
    assert response.status_code == 200
    path = "{}\\{}.html".format(str(Path.home()), vessel_name2)
    assert response.json() == path
    assert Path(path).is_file() is True
    remove_file(path)


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
