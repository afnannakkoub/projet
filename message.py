from fastapi import APIRouter, Depends
from .. import crud, schemas
from ..dependencies import get_db, get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=schemas.MessageOut)
def send_msg(data: schemas.MessageCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.post_message(db, data, user)

@router.get("/", response_model=list[schemas.MessageOut])
def read_msgs(db: Session = Depends(get_db)):
    return crud.get_messages(db)
