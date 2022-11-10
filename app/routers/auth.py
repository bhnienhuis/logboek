from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2

router = APIRouter(prefix="/api/pilot", tags=["Authentication"])

@router.post("/login")
def login(user_credentials: schemas.PilotLogin, db: Session = Depends(database.get_db)):
    pilot = db.query(models.Pilot).filter(models.Pilot.email == user_credentials.email).first()
    if not pilot:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    if not utils.verify(user_credentials.password, pilot.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"id_pilot": pilot.id})
    return {"access_token": access_token, "token_type": "bearer"}

