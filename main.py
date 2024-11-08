from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api.ml.ml import ml
import socket 

app = FastAPI()

app.include_router(ml, prefix='/api/v1/ml', tags=['ml'])

@app.get("/")
async def root():
    return {"message": f"Hello World from {socket.gethostname()}"}

instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def startup():
    instrumentator.expose(app)
