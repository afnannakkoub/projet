from fastapi import APIRouter, Depends
from .. import crud, schemas
from ..dependencies import get_db, get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=schemas.MoodOut)
def add_mood(data: schemas.MoodCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_mood(db, data, user)

@router.get("/", response_model=list[schemas.MoodOut])
def list_moods(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.get_user_moods(db, user)
