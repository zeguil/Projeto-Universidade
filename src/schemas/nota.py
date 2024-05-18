from pydantic import BaseModel
from typing import Optional
from datetime import date

class NotaBase(BaseModel):
    aluno_id: int
    disciplina_id: int
    n1: Optional[float] = None
    n2: Optional[float] = None
    media: Optional[float] = None

    class Config:
        orm_mode = True

class NotaCreate(NotaBase):
    n1: float

class NotaUpdate(NotaBase):
    n1: Optional[float] = None
    n2: Optional[float] = None
