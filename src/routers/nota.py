from typing import List
from schemas.aluno import *
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.notaController import NotaController

notasRouter = APIRouter(prefix='/nota', tags=['Nota'] )

@notasRouter.get("/notas/", response_model=list[nota_schema.Nota])
def read_notas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notas = nota_controller.get_notas(db, skip=skip, limit=limit)
    return notas

@notasRouter.get("/notas/{nota_id}", response_model=nota_schema.Nota)
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = nota_controller.get_nota(db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@notasRouter.post("/notas/", response_model=nota_schema.Nota)
def create_nota(nota: nota_schema.NotaCreate, db: Session = Depends(get_db)):
    return nota_controller.create_nota(db=db, nota=nota)

@notasRouter.put("/notas/{nota_id}", response_model=nota_schema.Nota)
def update_nota(nota_id: int, nota: nota_schema.NotaUpdate, db: Session = Depends(get_db)):
    db_nota = nota_controller.update_nota(db=db, nota_id=nota_id, nota=nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@notasRouter.delete("/notas/{nota_id}", response_model=nota_schema.Nota)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = nota_controller.delete_nota(db=db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota