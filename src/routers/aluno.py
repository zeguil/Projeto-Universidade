from typing import List
from schemas.aluno import *
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.AlunoController import AlunoController

alunoRouter = APIRouter(prefix='/aluno', tags=['Aluno'] )

@alunoRouter.get("/", response_model=List[AlunoBase], status_code=200)
def read_alunos(db: Session = Depends(get_db)) -> List[AlunoBase]:
    users = AlunoController(db).list_users()
    return users

@alunoRouter.get("/{nota_id}", response_model=AlunoBase)
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = AlunoController(db).get_nota(nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@alunoRouter.post("/", response_model=AlunoBase)
def create_nota(nota: AlunoCreate, db: Session = Depends(get_db)):
    return AlunoController(db).create_nota(nota)

@alunoRouter.put("/{nota_id}", response_model=AlunoBase)
def update_nota(nota_id: int, nota: AlunoUpdate, db: Session = Depends(get_db)):
    db_nota = AlunoController(db).update_nota(nota_id, nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@alunoRouter.delete("/{nota_id}", response_model=AlunoBase)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = AlunoController(db).delete_nota(nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota