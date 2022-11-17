from sqlalchemy import Column, Integer, SmallInteger, String
from sqlalchemy.sql.expression import text
from .database import Base

class Pilot(Base):
    __tablename__ = "pilot"

    ID = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    img_name = Column(String, nullable=True)
    instructor = Column(SmallInteger, default=0)


class PilotTotals(Base):
    __tablename__ = "vw_totals_pilot"

    starts = Column(Integer)
    uren = Column(Integer)
    id_pilot = Column(Integer, primary_key=True, nullable=False)


class AllFlights(Base):
    __tablename__ = "vw_all_flights"

    ID = Column(Integer, primary_key=True, nullable=False)
    id_pilot = Column(Integer)
    flight_no = Column(Integer)
    date = Column(String)
    name_field_start = Column(String)
    time_start = Column(String)
    name_field_landing = Column(String)
    time_landing = Column(String)
    name_type = Column(String)
    registration = Column(String)
    launch_method = Column(String)
    duration = Column(String)
    no_of_flights = Column(Integer)
    duration_pic = Column(String, nullable=True)
    duration_dual = Column(String, nullable=True)
    duration_instructor = Column(String, nullable=True)
    remark = Column(String, nullable=True)
    cross_country = Column(Integer, nullable=True)
    distance = Column(Integer, nullable=True)
    olc = Column(String, nullable=True)
    instructor = Column(String, nullable=True)


class TotalsYear(Base):
    __tablename__ = "vw_totals_year"

    jaar = Column(Integer, primary_key=True)
    totaal = Column(Integer, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)


class TotalsType(Base):
    __tablename__ = "vw_totals_type"

    type = Column(String, primary_key=True)
    totaal = Column(Integer, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)


class TotalsPlane(Base):
    __tablename__ = "vw_totals_plane"

    registratie = Column(String, primary_key=True)
    type = Column(String)
    totaal = Column(Integer, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)


class TotalsYearType(Base):
    __tablename__ = "vw_totals_year_type"

    jaar = Column(Integer, primary_key=True)
    type = Column(String, primary_key=True)
    totaal = Column(Integer)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)

class TotalsYearField(Base):
    __tablename__ = "vw_totals_year_field"

    jaar = Column(Integer, primary_key=True)
    veld = Column(String, primary_key=True)
    totaal = Column(Integer)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)

class TotalsField(Base):
    __tablename__ = "vw_totals_field"

    veld = Column(String, primary_key=True)
    totaal = Column(Integer, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)


class TotalsInstructor(Base):
    __tablename__ = "vw_totals_instructor"

    instructeur = Column(String, primary_key=True)
    totaal = Column(Integer, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)


class TotalsMethod(Base):
    __tablename__ = "vw_totals_method"

    methode = Column(String, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    self = Column(Integer, nullable=True)
    tmg = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)


class TotalsYearInstruction(Base):
    __tablename__ = "vw_totals_year_instruction"

    jaar = Column(Integer, primary_key=True)
    totaal = Column(Integer, primary_key=True)
    lier = Column(Integer, nullable=True)
    sleep = Column(Integer, nullable=True)
    duur = Column(Integer)
    id_pilot = Column(Integer)

class PilotFields(Base):
    __tablename__ = "vw_pilot_fields"

    id = Column(Integer, primary_key=True)
    id_pilot = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)





