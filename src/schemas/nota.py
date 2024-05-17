from pydantic import BaseModel
from typing import Optional
from datetime import date

class NotaBase(BaseModel):
    aluno_id: int
    disciplina_id: int
    n1: Optional[float] = None
    n2: Optional[float] = None
    media: Optional[float] = None
    data_nota: Optional[date] = None

    class Config:
        orm_mode = True

class NotaCreate(NotaBase):
    media: Optional[float] = None

class NotaUpdate(NotaBase):
    media: Optional[float] = None
