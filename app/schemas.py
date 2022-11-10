from typing import Optional
from pydantic import BaseModel

########
# AUTH #
########
class PilotLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]


##########
# REPORT #
##########
class PilotTotals(BaseModel):
    starts: int
    uren: int
    id_pilot: int

    class Config:
        orm_mode = True


class AllFlights(BaseModel):
    ID: Optional[int]
    id_pilot: Optional[int]
    flight_no: Optional[int]
    date: Optional[str]
    name_field_start: Optional[str]
    time_start: Optional[str]
    name_field_landing: Optional[str]
    time_landing: Optional[str]
    name_type: Optional[str]
    registration: Optional[str]
    launch_method: Optional[str]
    duration: Optional[str]
    no_of_flights: Optional[int]
    duration_pic: Optional[str]
    duration_dual: Optional[str]
    duration_instructor: Optional[str]
    remark: Optional[str]
    cross_country: Optional[int]
    distance: Optional[int]
    olc: Optional[str]
    instructor: Optional[str]

    class Config:
        orm_mode = True


class TotalsYear(BaseModel):
    jaar: int
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True
