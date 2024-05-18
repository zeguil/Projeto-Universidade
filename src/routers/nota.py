from typing import List
from schemas.nota import NotaBase, NotaCreate, NotaUpdate
from database.config import Session
from fastapi import APIRouter, Depends, HTTPException
from database.dependencies import get_db
from controllers.notaController import NotaController

notaRouter = APIRouter(prefix='/nota', tags=['Nota'])

@notaRouter.get("/", response_model=List[NotaBase], status_code=200)
def read_notas(db: Session = Depends(get_db)) -> List[NotaBase]:
    notas = NotaController(db).list_notas()
    return notas

@notaRouter.post("/n1", response_model=NotaBase)
def create_n1(nota: NotaCreate, db: Session = Depends(get_db)):
    return NotaController(db).create_n1(nota)

@notaRouter.put("/n2", response_model=NotaBase)
def create_n2(aluno_id: int, disciplina_id: int, n2: float, db: Session = Depends(get_db)):
    return NotaController(db).create_n2(aluno_id, disciplina_id, n2)

@notaRouter.put("/{nota_id}", response_model=NotaBase)
def update_nota(nota_id: int, nota: NotaUpdate, db: Session = Depends(get_db)):
    db_nota = NotaController(db).update_nota(nota_id, nota)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@notaRouter.delete("/{nota_id}", response_model=NotaBase)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = NotaController(db).delete_nota(nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota
