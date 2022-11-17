from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2
from ..database import engine

router = APIRouter(prefix="/api/pilot", tags=["Authentication"])

@router.post("/login")
def login(user_credentials: schemas.PilotLogin, db: Session = Depends(database.get_db)):
    pilot = db.query(models.Pilot).filter(models.Pilot.email == user_credentials.email).first()
    if not pilot:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    if not utils.verify(user_credentials.password, pilot.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    print(pilot.first_name)
    access_token = oauth2.create_access_token(data={"id_pilot": pilot.ID})
    return {"success": 1,
            "message": "Login successfully", 
            "token": access_token,
            "pilot": {
                "id_pilot": pilot.ID,
                "first_name": pilot.first_name,
                "last_name": pilot.last_name,
                "email": pilot.email,
                "img_name": pilot.img_name,
                "instructor": pilot.instructor
            }
        }


@router.get("/pagetotals/{id}/{flight_no}")
def get_page_totals(id: int, flight_no: int, db: Session = Depends(database.get_db), current_pilot: int = Depends(oauth2.get_current_pilot)):
    sql = """SELECT sum(time_to_sec(duration)) AS flight_time, sum(no_of_flights) as landings, 
        sum(time_to_sec(duration_pic)) AS PIC,
        sum(time_to_sec(duration_dual)) AS DBO,
        sum(time_to_sec(duration_instructor)) AS instructor
        FROM flight WHERE id_pilot=%s and flight_no<=%s"""
    result = engine.execute(sql, (id, flight_no)).first()
    return result

