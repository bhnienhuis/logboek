from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy import desc
from sqlalchemy.orm import Session
from typing import List
from .. import database, schemas, models, utils, oauth2

router = APIRouter(prefix="/api/report", tags=["Reports"])


@router.get("/totalspilot/{id}", response_model=schemas.PilotTotals)
def get_pilot_totals(id: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    totals = db.query(models.PilotTotals).filter(models.PilotTotals.id_pilot == id).first()
    if not totals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Totals for pilot with id {id} were not found")
    return totals

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

