from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import NotaBase, NotaCreate, NotaUpdate
from controllers.notaController import NotaController

notasRouter = APIRouter(prefix='/nota', tags=['Nota'])

@notasRouter.get("/", response_model=List[NotaBase], status_code=200)
def read_notas(db: Session = Depends(get_db)) -> List[NotaBase]:
    notas = NotaController(db).list_notas()
    return notas

@notasRouter.get("/{nota_id}", response_model=NotaBase)
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = NotaController(db).get_nota(nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@notasRouter.post("/", response_model=NotaBase)
def create_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    return NotaController(db).create_nota(nota)

@notasRouter.put("/{nota_id}", response_model=NotaBase)
def update_nota(nota_id: int, nota: NotaUpdate, db: Session = Depends(get_db)):
    db_nota = NotaController(db).update_nota(nota_id, nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@notasRouter.delete("/{nota_id}", response_model=NotaBase)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = NotaController(db).delete_nota(nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota
