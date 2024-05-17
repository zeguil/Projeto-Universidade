from typing import List
from schemas.disciplina import *
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.disciplinaController import DisciplinaController

disciplinaRouter = APIRouter(prefix='/disciplina', tags=['Disciplina'] )

@disciplinaRouter.get("/notas/", response_model=list[DisciplinaBase])
def read_notas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notas = nota_controller.get_notas(db, skip=skip, limit=limit)
    return notas

@disciplinaRouter.get("/notas/{nota_id}", response_model=DisciplinaBase)
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = nota_controller.get_nota(db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@disciplinaRouter.post("/notas/", response_model=DisciplinaBase)
def create_nota(nota: DisciplinaCreate, db: Session = Depends(get_db)):
    return nota_controller.create_nota(db=db, nota=nota)

@disciplinaRouter.put("/notas/{nota_id}", response_model=DisciplinaBase)
def update_nota(nota_id: int, nota: DisciplinaUpdate, db: Session = Depends(get_db)):
    db_nota = nota_controller.update_nota(db=db, nota_id=nota_id, nota=nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@disciplinaRouter.delete("/notas/{nota_id}", response_model=DisciplinaBase)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = nota_controller.delete_nota(db=db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota