import random

from cbpmtypes import IncidentLocation


def rand():
    return random.random() * 10


def get_absolutely_not_faked_weather_data(incident_location):
    basetemp = 10  # degrees celsius
    windgeschwindigkeit = 0.1
    wellenhoehe = 0.5
    sichtweite = 1000

    if incident_location == IncidentLocation.bodensee:
        basetemp = 15
        wellenhoehe = rand() * 0.5
    elif incident_location == IncidentLocation.nordsee:
        basetemp = 13
        wellenhoehe = rand() * 0.8
    elif incident_location == IncidentLocation.ostsee:
        basetemp = 10
        wellenhoehe = rand() + 1
    elif incident_location == IncidentLocation.see:
        basetemp = 17
        wellenhoehe = rand()
    elif incident_location == IncidentLocation.fluss:
        basetemp = 19
        wellenhoehe = rand() * 0.5

    windgeschwindigkeit = wellenhoehe * 10
    sichtweite = sichtweite * rand()

    return basetemp, sichtweite, windgeschwindigkeit, wellenhoehe
