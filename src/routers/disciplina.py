from typing import List
from schemas.disciplina import DisciplinaBase, DisciplinaCreate, DisciplinaUpdate
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.disciplinaController import DisciplinaController

disciplinaRouter = APIRouter(prefix='/disciplina', tags=['Disciplina'])

@disciplinaRouter.get("/", response_model=List[DisciplinaBase], status_code=200)
def read_disciplinas(db: Session = Depends(get_db)) -> List[DisciplinaBase]:
    disciplinas = DisciplinaController(db).list_disciplinas()
    return disciplinas

@disciplinaRouter.post("/", response_model=DisciplinaBase)
def create_disciplina(disciplina: DisciplinaCreate, db: Session = Depends(get_db)):
    return DisciplinaController(db).create_disciplina(disciplina)

@disciplinaRouter.put("/{disciplina_id}", response_model=DisciplinaBase)
def update_disciplina(disciplina_id: int, disciplina: DisciplinaUpdate, db: Session = Depends(get_db)):
    db_disciplina = DisciplinaController(db).update_disciplina(disciplina_id, disciplina)
    if db_disciplina is None:
        raise HTTPException(status_code=404, detail="Disciplina not found")
    return db_disciplina

@disciplinaRouter.delete("/{disciplina_id}", response_model=DisciplinaBase)
def delete_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    db_disciplina = DisciplinaController(db).delete_disciplina(disciplina_id)
    if db_disciplina is None:
        raise HTTPException(status_code=404, detail="Disciplina not found")
    return db_disciplina
