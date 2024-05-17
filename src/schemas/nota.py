from pydantic import BaseModel
from typing import Optional
from datetime import date

class NotaBase(BaseModel):
    aluno_id: int
    disciplina_id: int
    n1: float
    n2: Optional[float] = None
    data_nota: Optional[date] = None

class NotaCreate(NotaBase):
    aluno_id: int
    disciplina_id: int
    n1: float

class NotaUpdate(NotaBase):
    pass

class Nota(NotaBase):
    id: int
    media: Optional[float] = None

    class Config:
        orm_mode = True
