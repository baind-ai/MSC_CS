from enum import Enum
from pydantic import BaseModel


class IncidentLocation(str, Enum):
    # Bodensee, Nordsee, Ostsee, See, Fluss
    bodensee = "bodensee"
    nordsee = "nordsee"
    ostsee = "ostsee"
    see = "see"
    fluss = "fluss"


class Country(str, Enum):
    germany = "deutschland"
    austria = "oesterreich"
    swiss = "schweiz"


class Investigator(BaseModel):
    name: str
    vname: str
    berufserfahrung: int
    priority: int
