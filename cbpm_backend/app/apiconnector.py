import random
import gmplot
from pathlib import Path
from typing import List

from cbpmtypes import IncidentLocation


def rand(mult: float = 1.0):
    return random.random() * 10 * mult


def get_absolutely_not_faked_weather_data(
    incident_location: str,
) -> (int, float, float, float):

    basetemp = 10  # degrees celsius
    windgeschwindigkeit = 0.1
    wellenhoehe = 0.5
    sichtweite = 1000

    if incident_location == IncidentLocation.bodensee:
        basetemp = 15
        wellenhoehe = rand(0.4)
        windgeschwindigkeit = wellenhoehe * 40
    elif incident_location == IncidentLocation.nordsee:
        basetemp = 13
        wellenhoehe = rand()
        windgeschwindigkeit = wellenhoehe * 20
    elif incident_location == IncidentLocation.ostsee:
        basetemp = 10
        wellenhoehe = rand(0.6)
        windgeschwindigkeit = wellenhoehe * 30
    elif incident_location == IncidentLocation.see:
        basetemp = 17
        wellenhoehe = rand(0.2)
        windgeschwindigkeit = wellenhoehe * 65
    elif incident_location == IncidentLocation.fluss:
        basetemp = 19
        wellenhoehe = rand(0.1)
        windgeschwindigkeit = wellenhoehe * 120

    sichtweite = sichtweite * rand()

    return basetemp, sichtweite, windgeschwindigkeit, wellenhoehe


def __draw_gmap(
    plot_region: tuple,
    latitude_list: List[float],
    longitude_list: List[float],
    html_link: str,
) -> None:
    try:
        # create google maps page
        gmap = gmplot.GoogleMapPlotter(plot_region[0], plot_region[1], plot_region[2])
        # draw gps route
        gmap.plot(latitude_list, longitude_list, "cornflowerblue", edge_width=2.5)
        # generate map
        gmap.draw(html_link)
    except Exception:
        pass


def __obtain_gps_routes(incident_location: str) -> (tuple, List[float], List[float]):
    plot_region = ()  # lat, lon, zoom
    latitude_list = []
    longitude_list = []

    if incident_location == IncidentLocation.bodensee:
        plot_region = (47.580095982950105, 9.50416484137088, 11)
        latitude_list = [47.648760341271604, 47.63719468553636, 47.50392095058772]
        longitude_list = [9.481505539613067, 9.480990555482208, 9.539815667506218]
    elif incident_location == IncidentLocation.nordsee:
        plot_region = (54.133688856512784, 8.33702555329171, 10)
        latitude_list = [
            54.17343242369107,
            53.983978527249185,
            54.036030418457415,
            54.2305100422175,
        ]
        longitude_list = [
            7.894881388490262,
            8.700359950142456,
            8.841122279244019,
            8.470221882564715,
        ]
    elif incident_location == IncidentLocation.ostsee:
        plot_region = (54.39883638525454, 13.105277371005513, 11)
        latitude_list = [
            54.32926909287191,
            54.3288686898761,
            54.398879880078,
            54.456057998978544,
        ]
        longitude_list = [
            13.12195204572879,
            13.101352680494415,
            13.111652363111602,
            13.058784165570387,
        ]
    elif incident_location == IncidentLocation.see:
        plot_region = (47.869995999348944, 12.421645254923192, 11)

        latitude_list = [
            47.88415788778023,
            47.869995999348944,
            47.85513912827168,
            47.84269754289133,
        ]
        longitude_list = [
            12.419241995645848,
            12.421645254923192,
            12.43417653544077,
            12.416667074991551,
        ]
    elif incident_location == IncidentLocation.fluss:
        plot_region = (50.17944057884664, 7.578124637156861, 12)
        latitude_list = [
            50.150300397361605,
            50.16789659426737,
            50.17944057884664,
            50.202749404509845,
            50.232177567014084,
            50.23854600731139,
        ]
        longitude_list = [
            7.7183719821275645,
            7.697429294139283,
            7.643012637645143,
            7.643055552989381,
            7.606277102977174,
            7.578124637156861,
        ]

    return plot_region, latitude_list, longitude_list


def get_totally_real_gps_route(vessel_name: str, incident_location: str) -> str:
    html_link = "{}\\{}.html".format(str(Path.home()), vessel_name)

    plot_region, latitude_list, longitude_list = __obtain_gps_routes(incident_location)
    __draw_gmap(plot_region, latitude_list, longitude_list, html_link)

    return html_link
