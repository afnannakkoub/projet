from fastapi import APIRouter, Depends
from .. import crud, schemas
from ..dependencies import get_db, require_admin
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=schemas.ResourceOut)
def add_resource(data: schemas.ResourceCreate, db: Session = Depends(get_db), user=Depends(require_admin)):
    return crud.create_resource(db, data, user)

@router.get("/", response_model=list[schemas.ResourceOut])
def list_resources(db: Session = Depends(get_db)):
    return crud.get_resources(db)

@router.delete("/{id}")
def remove_resource(id: int, db: Session = Depends(get_db), user=Depends(require_admin)):
    crud.delete_resource(db, id)
    return {"detail": "Deleted"}
