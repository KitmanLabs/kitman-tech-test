from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from data import ATHLETES, SQUADS

app = FastAPI()

# --- Models ---

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    username: str

# --- Endpoints ---

@app.get("/athletes")
def get_athletes():
    return ATHLETES

@app.get("/squads")
def get_squads():
    return SQUADS

@app.post("/session", response_model=LoginResponse)
def login(request: LoginRequest):
    if len(request.username) < 3 or len(request.password) < 3:
        raise HTTPException(status_code=400, detail="Username and password must be at least 3 characters long")
    return {"username": request.username}
