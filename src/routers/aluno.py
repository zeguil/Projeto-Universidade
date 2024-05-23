from typing import List
from schemas.aluno import *
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.alunoController import AlunoController

alunoRouter = APIRouter(prefix='/aluno', tags=['Aluno'] )

@alunoRouter.get("/", response_model=List[AlunoBase], status_code=200)
def read_alunos(db: Session = Depends(get_db)) -> List[AlunoBase]:
    users = AlunoController(db).list_alunos()
    return users

@alunoRouter.post("/", response_model=AlunoBase)
def create_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    return AlunoController(db).create_aluno(aluno)

@alunoRouter.put("/{aluno_id}", response_model=AlunoBase)
def update_aluno(aluno_id: int, aluno: AlunoUpdate, db: Session = Depends(get_db)):
    db_aluno = AlunoController(db).update_aluno(aluno_id, aluno)
    return db_aluno

@alunoRouter.delete("/{aluno_id}", response_model=AlunoBase)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = AlunoController(db).delete_aluno(aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="aluno not found")
    return db_aluno