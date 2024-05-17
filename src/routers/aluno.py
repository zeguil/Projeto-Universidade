from typing import List
from schemas.aluno import *
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.AlunoController import AlunoController

alunoRouter = APIRouter(prefix='/aluno', tags=['Aluno'] )

@alunoRouter.get("/", response_model=list[AlunoBase])
def read_notas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notas = AlunoController.get_notas(db, skip=skip, limit=limit)
    return notas

@alunoRouter.get("/{nota_id}", response_model=AlunoBase)
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = AlunoController.get_nota(db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@alunoRouter.post("/", response_model=AlunoBase)
def create_nota(nota: AlunoBaseCreate, db: Session = Depends(get_db)):
    return AlunoController.create_nota(db=db, nota=nota)

@alunoRouter.put("/{nota_id}", response_model=AlunoBase)
def update_nota(nota_id: int, nota: AlunoUpdate, db: Session = Depends(get_db)):
    db_nota = AlunoController.update_nota(db=db, nota_id=nota_id, nota=nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@alunoRouter.delete("/{nota_id}", response_model=AlunoBase)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = AlunoController.delete_nota(db=db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota