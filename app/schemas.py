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
    ID: Optional[str]


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

class TotalsType(BaseModel):
    type: str
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsPlane(BaseModel):
    registratie: str
    type: str
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsField(BaseModel):
    veld: str
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsInstructor(BaseModel):
    instructeur: str
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsMethod(BaseModel):
    methode: str
    lier: Optional[int]
    sleep: Optional[int]
    self: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsYearType(BaseModel):
    jaar: int
    type: str
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsYearField(BaseModel):
    jaar: int
    veld: str
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    tmg: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True


class TotalsYearInstruction(BaseModel):
    jaar: int
    totaal: int
    lier: Optional[int]
    sleep: Optional[int]
    duur: int
    id_pilot: int

    class Config:
        orm_mode = True

class PilotFields(BaseModel):
    id: int
    id_pilot: int
    name: str

    class Config:
        orm_mode = True
