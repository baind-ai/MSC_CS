from enum import Enum


class IncidentLocation(str, Enum):
    # Bodensee, Nordsee, Ostsee, See, Fluss
    bodensee = "bodensee"
    nordsee = "nordsee"
    ostsee = "ostsee"
    see = "see"
    fluss = "fluss"
