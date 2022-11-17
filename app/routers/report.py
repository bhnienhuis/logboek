from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy import desc
from sqlalchemy.orm import Session
from typing import List
from .. import database, schemas, models, utils, oauth2

router = APIRouter(prefix="/api/report", tags=["Reports"])


@router.get("/totalspilot/{id}", response_model=List[schemas.PilotTotals])
def get_pilot_totals(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.PilotTotals).filter(models.PilotTotals.id_pilot == id).first()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    result_list = []
    result_list.append(totals)
    return result_list

@router.get("/twentyflights/{id}", response_model=List[schemas.AllFlights])
def get_twenty_flights(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    flights = db.query(models.AllFlights).filter(models.AllFlights.id_pilot == id).order_by(models.AllFlights.ID.desc()).limit(10).all()
    if not flights:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return flights


@router.get("/totalsyear/{id}", response_model=List[schemas.TotalsYear])
def get_totals_year(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsYear).filter(models.TotalsYear.id_pilot == id).order_by(models.TotalsYear.jaar.desc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalstype/{id}", response_model=List[schemas.TotalsType])
def get_totals_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsType).filter(models.TotalsType.id_pilot == id).order_by(models.TotalsType.type.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalsplane/{id}", response_model=List[schemas.TotalsPlane])
def get_totals_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsPlane).filter(models.TotalsPlane.id_pilot == id).order_by(models.TotalsPlane.type.asc(), models.TotalsPlane.registratie.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalsfield/{id}", response_model=List[schemas.TotalsField])
def get_totals_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsField).filter(models.TotalsField.id_pilot == id).order_by(models.TotalsField.veld.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalsinstructor/{id}", response_model=List[schemas.TotalsInstructor])
def get_totals_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsInstructor).filter(models.TotalsInstructor.id_pilot == id).order_by(models.TotalsInstructor.instructeur.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalsmethod/{id}", response_model=List[schemas.TotalsMethod])
def get_totals_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsMethod).filter(models.TotalsMethod.id_pilot == id).order_by(models.TotalsMethod.methode.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/allflights/{id}", response_model=List[schemas.AllFlights])
def get_all_flights(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    flights = db.query(models.AllFlights).filter(models.AllFlights.id_pilot == id).order_by(models.AllFlights.ID.desc()).all()
    if not flights:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return flights

@router.get("/crosscountry/{id}", response_model=List[schemas.AllFlights])
def get_all_flights(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    flights = db.query(models.AllFlights).filter(models.AllFlights.id_pilot == id).filter(models.AllFlights.cross_country == 1).order_by(models.AllFlights.ID.desc()).all()
    if not flights:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return flights

@router.get("/totalstypeyear/{id}", response_model=List[schemas.TotalsYearType])
def get_totals_year_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsYearType).filter(models.TotalsYearType.id_pilot == id).order_by(models.TotalsYearType.jaar.desc(), models.TotalsYearType.type.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalsfieldyear/{id}", response_model=List[schemas.TotalsYearField])
def get_totals_year_type(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsYearField).filter(models.TotalsYearField.id_pilot == id).order_by(models.TotalsYearField.jaar.desc(), models.TotalsYearField.veld.asc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

@router.get("/totalsyearinstruction/{id}", response_model=List[schemas.TotalsYearInstruction])
def get_totals_year(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.TotalsYearInstruction).filter(models.TotalsYearInstruction.id_pilot == id).order_by(models.TotalsYearInstruction.jaar.desc()).all()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

