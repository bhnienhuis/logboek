from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from .. import database, schemas, models, utils, oauth2
from ..database import engine

router = APIRouter(prefix="/api/maint", tags=["Authentication"])

def make_update_query(id, table, record):
    setclause = f"UPDATE {table} SET "
    for key in record:
        if key != "ID":
            if record[key] == None: 
                setclause += "Null"
        elif record[key] == 1 or record[key] == 0:
                setclause += f" {key} = "
                setclause += f"{record[key]}, "
        else:
            setclause += f" {key}="
            setclause += f"'{record[key]}', "
    setclause = setclause[:-1]
    setclause += f" WHERE ID = {id}"
    return setclause

def make_insert_query(table, record):
    fields = ""
    values = ""
    for key in record:
        if key != "ID":
            if record[key] == None:
                values += "Null, "
            elif record[key] == 1 or record[key] == 0:
                values += f"{record[key]}, "
            else:
                values += f"'{record[key]}',"
            fields += f"`{key}`,"
    fields = fields[:-1]
    values = values[:-2]

    print("\n", fields, "\n\n", values, "\n")

    query = f"INSERT INTO `{table}` ({fields}) VALUES ({values})"
    return query



@router.get("/flightbyid/{id}",  response_model=List[schemas.AllFlights])
def get_flight_by_id(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    flight = db.query(models.AllFlights).filter(models.AllFlights.ID == id).first()
    if not flight:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Flight with id {id} not found")
    results = []
    results.append(flight)
    return results


@router.get("/pilotfields/{id}", response_model=List[schemas.PilotFields])
def get_totals_year(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    fields = db.query(models.PilotFields).filter(models.PilotFields.id_pilot == id).all()
    if not fields:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No fields for pilot with id {id} were found")
    return fields


@router.get("/pilotplanebyid/{id}")
def get_pilot_plane_by_id(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT * FROM vw_pilot_planes WHERE id_pilot_plane = %s"""
    plane = engine.execute(sql, (id)).first()
    if not plane:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No plane with id {id} was found")
    result = []
    result.append(plane)
    return result


@router.get("/pilottypes/{id}")
def get_pilot_types(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT DISTINCT(name), id_type FROM vw_pilot_planes WHERE id_pilot = %s ORDER BY name"""
    types = engine.execute(sql, (id)).all()
    if not types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No types for pilot with id {id} were found")
    return types



@router.get("/typeregistrations/{id}/{id_type}")
def get_type_registrations(id: int, id_type: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT registration, id_pilot_plane, single FROM vw_pilot_planes WHERE id_pilot = %s and id_type = %s """
    registrations = engine.execute(sql, (id, id_type)).all()
    if not registrations:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No planes for pilot with id {id} were found")
    return registrations


@router.get("/pilotplanes/{id}")
def get_pilot_planes(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT * FROM vw_pilot_planes WHERE id_pilot = %s"""
    planes = engine.execute(sql, (id)).all()
    if not planes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No planes for pilot with id {id} were found")
    return planes


@router.get("/newflightno/{id}")
def get_new_flight_no(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT MAX(flight_no + no_of_flights) as new_flight_no FROM flight WHERE id_pilot = %s"""
    flight_no = engine.execute(sql, (id)).all()
    return flight_no


@router.get("/pilotinstructors/{id}")
def get_pilot_instructors(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT * FROM instructor WHERE id_pilot = %s ORDER BY name"""
    instructors = engine.execute(sql, (id)).all()
    if not instructors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No instructors for pilot with id {id} were found")
    return instructors


@router.post("/insertflight")
def post_flight(payload: dict,db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = make_insert_query('flight', payload)
    sql += " RETURNING flight_no"
    flight_no = engine.execute(sql).first()
    print(flight_no)
    return {"Vlucht aangelegd:", flight_no}


@router.put("/updateflight/{id}")
def post_flight(id: int, payload: dict,db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = make_update_query(id, 'flight', payload)
    flight_no = engine.execute(sql).first()
    print(flight_no)
    return {"Vlucht aangepast:", id}



#################################################################
# patchFlight: (id, data, callBack) => {
#   const query = make_update_query(id, 'flight', data);
#   pool.query(
#     query,
#     (error, results, fields) => {
#       if (error) {
#         return callBack(error);
#       }
#       return callBack(null, results);
#     }
#   );
# },
