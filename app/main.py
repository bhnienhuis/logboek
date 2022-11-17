from fastapi import FastAPI
from fastapi.middleware.cors  import CORSMiddleware
from . import models
from .database import engine
from .routers import pilot, report, maint
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(pilot.router)
app.include_router(report.router)
app.include_router(maint.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello from Logboek"}


