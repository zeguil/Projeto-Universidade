from pydantic import BaseModel
from typing import Optional

class NotaBase(BaseModel):
    aluno_id: int
    disciplina_id: int

    class Config:
        orm_mode = True

class NotaCreateN1(NotaBase):
    n1: float

class NotaCreateN2(NotaBase):
    n2: float

class NotaUpdate(NotaBase):
    n2: Optional[float] = None
